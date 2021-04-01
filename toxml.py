import json
import csv
import os
import pandas as pd
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET


filename = "shooting-Scenes.csv"



# Read in the data
full_scenes_df = pd.read_csv(filename)
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
print(scenes_df)
print('\n')
scenes_df.columns = ['framenum', 'stime', 'dursec', 'caption']


    
def xml_encode(row):
    xmlItem = ['<ImageSegment']
    for ImageSegment in row.index:
        xmlItem.append('{0}="{1}"'.format(ImageSegment, row[ImageSegment]))
    xmlItem.append('</ImageSegment>')
    return ' '.join(xmlItem)

temp = '\n'.join(scenes_df.apply(xml_encode, axis=1))
#print(temp)
temp = '<AudioDoc name="' +"filename"+'">\n<ImageCaptionList>\n'+temp +"\n</ImageCaptionList>\n</AudioDoc>"
print(temp)

tree = ET.XML(temp)

with open("OUTPUT.xml", "w") as f:
    f.write(ET.tostring(tree))


