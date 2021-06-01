Usage steps for Ubuntu 16.04:

Downloads
1. Download/clone this repository
2. Download the folder "annotations" from https://www.dropbox.com/sh/fg1timcbrcdyhye/AAAs6z-ggS02ZFsVKhSLIUEEa?dl=0
3. Place the folder "annotations" in "data" folder
4. Download the file "model_50000" from https://www.dropbox.com/s/4rq62ru3ec9wdjk/model_50000?dl=0
5. Place the file "model_50000" in "result" folder

Ubuntu python setup
1. sudo apt-get update
2. sudo apt-get install build-essential checkinstall 
   if error, might have to wait for process to complete, OR sudo apt --fix-broken install
3. sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
4. cd /opt
5. sudo wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
6. sudo tar xzf Python-3.8.5.tgz
7. cd Python-3.8.5
8. sudo ./configure --enable-optimizations
9. sudo make -j 4
10. sudo make altinstall
11. cd /opt
12. sudo rm -f Python-3.8.5.tgz

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
2. pip install dicttoxml
3. pip install opencv-python
4. pip install click
5. pip install Pillow
6. pip install chainer
7. sudo -i
8. echo 1 > /proc/sys/vm/overcommit_memory
9. exit
10. cd cocoapi
11. cd PythonAPI
12. pip install -e.
13. cd ..
14. cd ..

Run
1. Put videos in "videos" folder, existing videos are: "airplane.mp4, bees.mp4, covid.mp4,"
2. Run from terminal using $ python full.py <videofile_name>
3. Example: python full.py bees.mp4