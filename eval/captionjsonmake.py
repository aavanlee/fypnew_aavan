import json

data = []
data.append({
    'filename':"DSET_001.jpg",
    'caption1':"a curly haired dog laying on shoes",
    'caption2':"a poodle laying on a shoe rack",
    'caption3':"a shoe rack and a dog",
    'caption4':"a teddy bear on a shoe rack"
})
data.append({
    'filename':"DSET_002.jpg",
    'caption1':"a table with wine glasses and a few bottles of wine",
    'caption2':"some wine glasses and wine bottles and bread on a table",
    'caption3':"several bottles glasses of wine on a table",
    'caption4':"a plate of bread and wine glasses and liquor bottles"
})
data.append({
    'filename':"DSET_003.jpg",
    'caption1':"a close up of a boy taking a video on his phone",
    'caption2':"a boy is photographing a plane takeoff on his phone",
    'caption3':"a boy using his phone to take a picture",
    'caption4':"a boy taking a photo on his camera"
})
data.append({
    'filename':"DSET_004.jpg",
    'caption1':"a white dog laying on a sidewalk",
    'caption2':"a dog laying beside a parked bicycle in the street",
    'caption3':"a dog is sleeping on the street",
    'caption4':"a dog is laying on the pavement beside a road"
})

print(json.dumps(data, indent=4))

with open('captionsraw.json', 'w') as outfile:
    json.dump(data, outfile)
