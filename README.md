## Video Captioning
Program to generate captions for the keyframes of a video, given a video file as input. 

![alt text](https://github.com/aavanlee/vidcaption_aavan/blob/master/architecture.png?raw=true)

## Installation
Usage steps for Ubuntu 16.04:

Downloads
1. Download/clone this repository
2. Download the file "model_checkpint.pth.tar" from https://drive.google.com/file/d/1OMnMuMuxEtKVmws2zNAlB3nhCVnwUTS4/view?usp=sharing
3. Place the file "model_checkpint.pth.tar" in the repo directory
4. model checkpoint source: https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning

Ubuntu python setup
1. sudo apt-get update
2. sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
3. cd /opt
4. sudo wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
5. sudo tar xzf Python-3.8.5.tgz
6. cd Python-3.8.5
7. sudo ./configure --enable-optimizations
8. sudo make -j 4
9. sudo make altinstall
10. cd /opt
11. sudo rm -f Python-3.8.5.tgz

Ubuntu setup
1. Change Directory to vidcaption_aavan
2. python3.8 -m pip install virtualenv
3. virtualenv -p python3.8 venv-vidcap
4. source venv-vidcap/bin/activate

Installing requirements
1. pip install -r requirements.txt

OR
1. pip install pandas
2. pip install torch
3. pip install opencv-python
4. pip install click
5. pip install torchvision
6. pip install matplotlib
7. pip install scikit-image
8. pip install Flask (API)
9. pip install pycocotools (evaluation)
10. pip install pycocoevalcap (evaluation)

## Video Download
Videos can be downloaded using the PyTube based video downloading script. Videos downloaded using this method are automatically saved as mp4 to the "video_uploads" folder. 

Run from terminal using $ python download_video.py <youtube_URL> <name_to_save_as_without_extension>
Example: python download_video.py https://www.youtube.com/watch?v=DocxmW2bOdc&t=80s singapore_dorm_cases

## Video Captioning

Video keyframe extraction supports most video formats including: mp4, ts, MOV, avi, y4m, mkv, flv, wmv.

Running without API:

0. Activate venv: $ source venv-vidcap/bin/activate
1. Put videos to caption in "video_uploads" folder
2. Run from terminal using $ python caption_video.py <videofile_name>
3. Example: python caption_video.py elsa.mp4 
4. To keep the video frames, run from terminal using $ python caption_video.py <videofile_name> keepframes
5. Example: python caption_video.py elsa.mp4 keepframes

Running with API:

0. Activate venv: $ source venv-vidcap/bin/activate
1. Run from terminal using $ python api_start.py 
2. Go to http://127.0.0.1:5001/captionvideo on browser
3. Browse disk for video file
4. Click upload
5. Uploaded videos will be saved to video_uploads directory

## Evaluation
If not evaluating, eval directory can be removed.

To caption and evaluate against custom dataset in COCO format:

0. pip install pycocoevalcap
1. Move model checkpoint file and wordmap into "eval" directory (default: model_checkpint.pth.tar and wordmap.json) 
2. Put folder with images to caption into "eval" directory
3. Change directory to "eval"
4. Ensure caption file in COCO format(for images to be captioned) is in "eval" directory, eg: "DATASET_coco_captions.json"
5. Run from terminal using $ python caption_and_eval.py <directory_name>
6. Example: python caption_and_eval.py DATASET
7. To keep output file of captioning, run from terminal using $ python caption_and_eval.py <directory_name> keepoutput
8. Example: python caption_and_eval.py DATASET keepoutput


To evaluate against video captions in COCO format, using video captioning output(output from caption_video.py):

1. Move the output file eg: covid.mp4-OUTPUT.json to eval directory
2. Change directory to "eval"
3. Ensure caption file in COCO format is in "eval" directory, eg: "covid.mp4-coco_captions.json"
4. Run from terminal using $python eval_video_output.py <videofile_name> 
5. Example: python eval_video_output.py covid.mp4

