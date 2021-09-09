

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
file = "./video_uploads/" +vidname
#file = video.mp4 


####-------------------------------EXTRACT KEYFRAME---------------------------------------------------------------------------------------------------####
extractcmd = "python scenedetect.py -m 2s --input " +file +" detect-content --threshold 29 list-scenes save-images"
os.system(extractcmd)
#output to ./frames


#sys.exit("Stopped")
#start_time = time.time()



####---------------------------------IMAGE CAPTION----------------------------------------------------------------------------------------------------####
#Ensure model checkpoint and wordmap in working directory
#os.system('python predict.py --img-dir "frames" --model result/model_50000 --rnn nsteplstm --max-caption-length 30 --gpu 0 --dataset-name mscoco --out prediction.json')
os.system('python caption.py --model="model_checkpoint.pth.tar" --word_map="wordmap.json" --beam_size=5')


####------------------------------FORMATTING DATAFRAME------------------------------------------------------------------------------------------------####
f = os.path.splitext(vidname)
csvfilename = f[0] +"-Scenes.csv"

# Read in the data
full_scenes_df = pd.read_csv(csvfilename)
scenes_df = full_scenes_df[['Scene Number', 'Start Time (seconds)', 'Length (seconds)']].copy()
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


####---------------------REMOVE ADJACENT DUPLICATE CAPTIONS-------------------------------------------------------------------------------------------####
##checks captions for similar adjacent captions and remove
def removeadj(threshold):
    droplist = []
    if threshold == 0:
        for i in range(1, len(scenes_df)):              
            if scenes_df['caption'][i] == scenes_df['caption'][i-1]:
                print("Adjacent duplicate caption found.")
                scenes_df.at[i-1,'dur(s)'] = scenes_df['dur(s)'][i-1] + scenes_df['dur(s)'][i]
                droplist.append(i)
    return droplist

droplist = removeadj(0)
print("Index numbers(frame#-1) to be dropped: ", droplist)
for i in range(len(droplist)):
    scenes_df.drop(scenes_df.index[droplist[i]], inplace = True)
#frame# not reset so frame images can still be easily found 

print(scenes_df)

####--------------------------OUTPUT TO JSON----------------------------------------------------------------------------------------------------------####
out = scenes_df.to_json(orient='records')
outputfile = vidname + '-OUTPUT.json'
with open(outputfile, 'w') as f:
    f.write(out)




####-----------------------------CLEANUP--------------------------------------------------------------------------------------------------------------####
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

## removing frames
try:
    if str(sys.argv[2]) == "keepframes":
        print("Frames kept")
except:
    dir_path = './frames'
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
    print("Frames removed")

    

end_time = time.time()
req_time = end_time - start_time
print("time taken: ", req_time)


