#SETUP
#cocoapi/PythonAPI
#pip install -e .

import io
import os
import subprocess
from subprocess import check_output
import re
import time
import json
import csv
import pandas as pd
#from dicttoxml import dicttoxml
import sys
import shutil

start_time = time.time()
vidname = str(sys.argv[1])
file = "./videos/" +vidname
#file = video.mp4 

#extract keyframe
extractcmd = "python scenedetect.py --input " +file +" detect-content list-scenes save-images"
os.system(extractcmd)
#output to ./frames

#image caption
#os.system('python predict.py --img-dir "frames" --model result/model_50000 --rnn nsteplstm --max-caption-length 30 --gpu 0 --dataset-name mscoco --out prediction.json')
os.system('python caption.py --model="model_checkpoint.pth.tar" --word_map="wordmap.json" --beam_size=5')

#toxml
f = os.path.splitext(vidname)
csvfilename = f[0] +"-Scenes.csv"

# Read in the data
full_scenes_df = pd.read_csv(csvfilename)
scenes_df = full_scenes_df[['Scene Number', 'Start Timecode', 'Length (seconds)']].copy()
scene_count = scenes_df.shape[0]
#print(scene_count)
#print(scenes_df.head(5))

path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, "prediction.json")
with open(path_to_file) as mydata:
    prediction_dict = json.load(mydata)

prediction_df = pd.DataFrame(list(prediction_dict.items()), columns = ['Frame', 'Caption'])
prediction_df.sort_values(by=['Frame'], inplace=True, ascending=True)
prediction_df.reset_index(inplace=True, drop = True)
#print(prediction_df)
scenes_df['Caption'] = pd.Series(prediction_df['Caption'])
scenes_df.columns = ['frame#', 'stime', 'dur(s)', 'caption']
print('\n')
print(scenes_df)
#print('\n')

out = scenes_df.to_json(orient='records')
outputfile = vidname + '-OUTPUT.json'
with open(outputfile, 'w') as f:
    f.write(out)


end_time = time.time()
req_time = end_time - start_time
print("time taken: ", req_time)

####CLEANUP
deletethis = "prediction.json"
deletealso = csvfilename

## If file exists, delete it ##
if os.path.isfile(deletethis):
    os.remove(deletethis)
else:    ## Show an error ##
    print("Error: %s file not found" % deletethis)

if os.path.isfile(deletealso):
    os.remove(deletealso)
else:    ## Show an error ##
    print("Error: %s file not found" % deletealso)

##REMOVING FRAMES
dir_path = './frames'
try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))
