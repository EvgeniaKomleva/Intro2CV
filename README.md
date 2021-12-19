# Intro to CV final project 

## Identification of cars from different teams
### Problem description
During the broadcast of the helicopter shooting, it is necessary to automatically identify the racing car and its belonging to the team in the frame.



### CV methods which we use
- YOLO

We plan to train YOLO to recognize one class of racing cars

- Histogram for color determination

Get three RGB numbers for each car. You can also not average the color over the entire box, but divide the box into smaller parts and determine the color in them, then get a vector with all the numbers.
Then cluster all cars and relate more similar vectors (for example, by cosine distance) to one cluster.
- Determining the number

The team number is written on a plate on the hood and door of the car, but it is not visible in all frames. We want to find the number and recognize it using a neural network (like it was in the 2nd task)
- Tracking 

Use https://github.com/adipandas/multi-object-tracker 



