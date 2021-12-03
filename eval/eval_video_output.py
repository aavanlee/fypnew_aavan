import json
import os
import pandas as pd
import sys
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap

vidname = str(sys.argv[1])
file = vidname + '-OUTPUT.json'
path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, file)

with open(path_to_file) as mydata:
    data = json.load(mydata)
df = pd.DataFrame(data[0:],columns=data[0])
df.drop('stime', axis=1, inplace=True)
df.drop('dur(s)', axis=1, inplace=True)
df.columns = ['image_id', 'caption']
print(df)
out = df.to_json(orient='records')
outputfile = vidname + '-coco_OUTPUT.json'
with open(outputfile, 'w') as f:
    f.write(out)

annotation_file = vidname + '-coco_captions.json'
results_file = vidname + '-coco_OUTPUT.json'
# PyCocoEval
coco = COCO(annotation_file)
coco_result = coco.loadRes(results_file)
coco_eval = COCOEvalCap(coco, coco_result)
coco_eval.params['image_id'] = coco_result.getImgIds()
coco_eval.evaluate()
print("\nEvaluation Scores:")
for metric, score in coco_eval.eval.items():
    print(f'{metric}: {score:.3f}')


####CLEANUP
deletethis = vidname + '-coco_OUTPUT.json'

## If file exists, delete it ##
if os.path.isfile(deletethis):
    os.remove(deletethis)
else:    ## Show an error ##
    print("Error: %s file not found" % deletethis)

print("\n")
