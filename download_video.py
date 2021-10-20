import os
import sys
import shutil

video_folder_path = "./video_uploads"
video_url = str(sys.argv[1])
video_new_name = str(sys.argv[2]) + ".mp4"
download_cmd = "pytube " + video_url
os.system(download_cmd)

for file in os.listdir("."):
    if file.endswith(".mp4"):
        filename = file
        break

os.rename(file, video_new_name)

shutil.move(video_new_name, video_folder_path)