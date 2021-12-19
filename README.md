# Intro to CV final project 

## Identification of cars from different teams
### Problem description
During the broadcast of the helicopter shooting, it is necessary to automatically identify the racing car and its belonging to the team in the frame.



### CV methods which we use
- YOLO

We  train YOLO to recognize one class of racing cars and plate with number

How to run YOLO model for detection:

`
git clone https://github.com/EvgeniaKomleva/Intro2CV.git`

`cd Intro2CV`

`pip install -qr requirements.txt  `

For cars detecion:

`python detect.py --weights ./runs/train/exp24/weights/best.pt --img 416 --conf 0.4 --source data/images/cars
`
For numbers detection:

`python detect.py --weights ./runs/train/exp26/weights/best.pt --img 416 --conf 0.4 --source data/images/cars
`

- Histogram for color determination

Get three RGB numbers for each car. You can also not average the color over the entire box, but divide the box into smaller parts and determine the color in them, then get a vector with all the numbers.
Then cluster all cars and relate more similar vectors (for example, by cosine distance) to one cluster.
- Determining the number

The team number is written on a plate on the hood and door of the car, but it is not visible in all frames. We want to find the number and recognize it using a neural network (like it was in the 2nd task)
- Tracking 

Use https://github.com/adipandas/multi-object-tracker 



