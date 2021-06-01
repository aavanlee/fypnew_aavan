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
1. Change Directory to captionfyp_aavan
2. python3.8 -m pip install virtualenv
3. virtualenv -p python3.8 venv
4. source venv/bin/activate

Installing requirements
1. pip install -r requirements.txt
2. sudo -i
3. echo 1 > /proc/sys/vm/overcommit_memory
4. exit

OR
1. pip install pandas
2. pip install torch
3. pip install opencv-python
4. pip install click
5. pip install torchvision
6. pip install matplotlib
7. pip install scikit-image
8. pip install Flask

Running without API
1. Put videos in "videos" folder, existing videos are: "airplane.mp4, bees.mp4, covid.mp4, rocket.mp4, fire.mp4, shooting.mp4"
2. Run from terminal using $ python full.py <videofile_name>
3. Example: python full.py airplane.mp4

Running with API
1.
