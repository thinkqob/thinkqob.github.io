#!/usr/bin/ python3
# videocollection v0.1.1
# date：20161006
# Collect videos from each folder after xunlei download

import os, shutil

file_format = ['mp4', 'avi', 'mkv', 'wmv']
path = os.getcwd()
folders = os.listdir()

for folder in folders:
    moved = False
    downloaded = True
    if os.path.isdir(folder):
        os.chdir(folder)
        files = os.listdir()
        for file in files:
            if os.path.getsize(file) > 500000000 and file.split('.').pop() in file_format:
                shutil.move(file, path)
                moved = True
            elif file.split('.').pop() == 'td':
                downloaded = False
        os.chdir(path)
    if moved == True and downloaded == True:
        shutil.rmtree(folder)
