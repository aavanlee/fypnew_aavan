

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
extractcmd = "python scenedetect.py --min-scene-len 2s --input "+file+" detect-content --threshold 29 list-scenes save-images"
os.system(extractcmd)
#output to ./frames

current_time = time.time()
keyframe_time = current_time - start_time
previous_time = current_time


#sys.exit("Stopped")
#start_time = time.time()



####---------------------------------IMAGE CAPTION----------------------------------------------------------------------------------------------------####
#Ensure model checkpoint and wordmap in working directory
#os.system('python predict.py --img-dir "frames" --model result/model_50000 --rnn nsteplstm --max-caption-length 30 --gpu 0 --dataset-name mscoco --out prediction.json')
print("\nGenerating Captions...")
os.system('python caption.py --model="model_checkpoint.pth.tar" --word_map="wordmap.json" --beam_size=3')

current_time = time.time()
caption_time = current_time - previous_time
previous_time = current_time

####------------------------------FORMATTING DATAFRAME------------------------------------------------------------------------------------------------####
pd.options.display.max_colwidth = 100
f = os.path.splitext(vidname)
csvfilename = f[0] +"-Scenes.csv"
# Read in key frame timestamp data
full_scenes_df = pd.read_csv(csvfilename)
scenes_df = full_scenes_df[['Scene Number', 'Start Time (seconds)', 'Length (seconds)']].copy()
# Read in image caption data
path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, "prediction.json")
with open(path_to_file) as mydata:
    prediction_dict = json.load(mydata)
# Formatting image caption data
prediction_df = pd.DataFrame(list(prediction_dict.items()), columns = ['Frame', 'Caption'])
prediction_df.sort_values(by=['Frame'], inplace=True, ascending=True)
prediction_df.reset_index(inplace=True, drop = True)
# Concatenating timestamps with image captions
scenes_df['Caption'] = pd.Series(prediction_df['Caption'])
scenes_df.columns = ['frame#', 'stime', 'dur(s)', 'caption']
# Print data
print(scenes_df)
#print('\n')

current_time = time.time()
format_time = current_time - previous_time
previous_time = current_time

####---------------------REMOVE ADJACENT DUPLICATE CAPTIONS-------------------------------------------------------------------------------------------####
##checks captions for similar adjacent captions and remove
def removeadj(threshold):
    droplist = []
    count = 0
    if threshold == 0:
        for i in range(1, len(scenes_df)):              
            if scenes_df['caption'][i] == scenes_df['caption'][i-1]:
                count = count + 1
                scenes_df.at[i-count,'dur(s)'] = scenes_df['dur(s)'][i-count] + scenes_df['dur(s)'][i]
                droplist.append(i)
            else:
                count = 0
    return droplist

droplist = removeadj(0)

if droplist != []:
    print("\nAdjacent duplicate caption(s) found.")
    droplist_frame_num = [j + 1 for j in droplist]
    print("frame# to be dropped: ", droplist_frame_num)
    scenes_df.drop(scenes_df.index[droplist], inplace = True)
    #frame# not reset so frame images can still be easily found
    print(scenes_df)

current_time = time.time()
dupremove_time = current_time - previous_time
previous_time = current_time

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
cleanup_time = end_time - previous_time
total_time = end_time - start_time
print("\nTime taken(s) for...")
print("Keyframe detection: ", keyframe_time)
print("Image captioning: ", caption_time)
print("Formatting: ", format_time)
print("Removing adjacent duplicates: ", dupremove_time)
print("Output and cleanup: ", cleanup_time)
print("Total time: ", total_time)
print("Output saved as: ", outputfile)
print("\n")


