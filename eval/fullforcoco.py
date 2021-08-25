

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

#image caption
#os.system('python predict.py --img-dir "frames" --model result/model_50000 --rnn nsteplstm --max-caption-length 30 --gpu 0 --dataset-name mscoco --out prediction.json')
os.system('python captionforcoco.py --model="model_checkpoint.pth.tar" --word_map="wordmap.json" --beam_size=5')

path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, "predictionforcoco.json")
with open(path_to_file) as mydata:
    prediction_dict = json.load(mydata)

prediction_df = pd.DataFrame(list(prediction_dict.items()), columns = ['image_id', 'caption'])
prediction_df.sort_values(by=['image_id'], inplace=True, ascending=True)
prediction_df.reset_index(inplace=True, drop = True)
#print(prediction_df)
#prediction_df['image_id'] = prediction_df['image_id'].str[19:-4]
#[19:-4] deletes str values and extension for coco val2014
prediction_df['image_id'] = prediction_df['image_id'].str[5:-4]
#[5:-4] deletes str values and extension for DSET
prediction_df['image_id'] = pd.to_numeric(prediction_df['image_id'])
print(prediction_df)
#scenes_df['Caption'] = pd.Series(prediction_df['Caption'])
#scenes_df.columns = ['frame#', 'stime', 'dur(s)', 'caption']
#print('\n')
#print(scenes_df)
#print('\n')

out = prediction_df.to_json(orient='records')
outputfile = 'coco-OUTPUT.json'
with open(outputfile, 'w') as f:
    f.write(out)

####CLEANUP
deletethis = "predictionforcoco.json"

## If file exists, delete it ##
if os.path.isfile(deletethis):
    os.remove(deletethis)
else:    ## Show an error ##
    print("Error: %s file not found" % deletethis)

#using pycocoevalcap eval
os.system('python coco_eval.py')


end_time = time.time()
req_time = end_time - start_time
print("time taken: ", req_time)


