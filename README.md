Usage steps for Ubuntu 16.04:

Downloads
1. Download/clone this repository
2. Download the file "model_checkpint.pth.tar" from https://drive.google.com/file/d/1OMnMuMuxEtKVmws2zNAlB3nhCVnwUTS4/view?usp=sharing
3. Place the file "model_checkpint.pth.tar" in the repo directory

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
1. Change Directory to fypnew_aavan
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
8. pip install Flask

Running without API:

0. Activate venv: $ source venv-vidcap/bin/activate
1. Put videos to test in "video_uploads" folder
2. Run from terminal using $ python full.py <videofile_name>
3. Example: python full.py airplane.mp4

Running with API:

0. Activate venv: $ source venv-vidcap/bin/activate
1. Run from terminal using $ python apistart.py 
2. Go to http://127.0.0.1:5001/captionvideo on browser
3. Browse disk for video file
4. Click upload
5. Uploaded videos will be saved to video_uploads directory

To evaluate against coco dataset format:

0. pip install pycocoevalcap
1. Move model checkpoint file and wordmap into "eval" directory (default: model_checkpint.pth.tar and wordmap.json) 
2. Change directory to "eval"
3. Put images to evaluate against into folder named "val2014" (default for evaluating against COCO val2014 set)
4. Run from terminal using $ python fullforcoco.py
5. Output file coco-OUTPUT.json is used to evaluate against caption json file in COCO format 
