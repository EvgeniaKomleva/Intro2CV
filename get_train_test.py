from os import listdir
from os.path import isfile, join
from shutil import copyfile


#f = open("all.txt", "a")
with open('/home/komleva/reflective-clothes-detect-yolov5/val.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#onlyfiles = [f for f in listdir("labels") if isfile(join("labels", f))]
for file in lines:
    print("train/"+file)
    copyfile('/home/komleva/reflective-clothes-detect-yolov5/train/'+file, "val_new/"+ file)
    #f.write("/home/komleva/yolov5/hat/" +file)
    #f.write("\n")
#f.close()
