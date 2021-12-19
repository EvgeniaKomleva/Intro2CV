from os import listdir
from os.path import isfile, join
from shutil import copyfile
import os

list_of_dir = ["26/", "27/", '39/', "46/", "69/"]
output_dir = "car_dataset/"
count = 0

for dir in list_of_dir:
    path_to_json = 'car_data/'+dir
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    print("__________")
    print(dir, json_files)  # for me this prints ['foo.json']
    for file in json_files:
        name = str(count).zfill(8)
        img_file = file[:-4]+"jpg"
        print(name)
        copyfile('/home/komleva/yolov5_new/'+path_to_json+"/" + file, output_dir + name+".json")
        copyfile('/home/komleva/yolov5_new/' + path_to_json + "/" + img_file, output_dir + name+".jpg")
        count = count + 1
print("TOTAL", count)