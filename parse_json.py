import json
from shutil import copyfile
import os
path_to_json = "car_dataset/"
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
for json_file_ in json_files[200:]:
    with open(path_to_json+json_file_) as json_file:
        f = open("car_dataset/val/"+json_file_[:-4] +"txt", "a")

        data = json.load(json_file)
        for p in data['shapes']:
            print(p['points'])
            max_x = 0
            max_y = 0
            min_x = 20000
            min_y = 20000
            for point in p['points']:
                if point[0]>max_x:
                    max_x = point[0]
                if point[1]>max_y:
                    max_y = point[1]
                if point[0]<min_x:
                    min_x = point[0]
                if point[1]<min_y:
                    min_y = point[1]
            print(max_x, max_y, min_x, min_y)
            center_x = ((max_x -min_x) / 2 + min_x)/1920
            center_y = ((max_y - min_y) / 2 + min_y)/1080
            width = (max_x -min_x)/1920
            height =(max_y - min_y)/1080
            f.write("0 "+ str(center_x)+" "+str(center_y)+" "+str(width)+" "+str(height))
            f.write("\n")
            img_file = json_file_[:-4] + "jpg"
            copyfile('/home/komleva/yolov5_new/' + path_to_json + "/" + img_file, "car_dataset/val/" + img_file)
        f.close()