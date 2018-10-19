#!/bin/bash

#
#
# This bash script takes the scraped images
# and automatically resizes the images, and 
# trains the CNN model.
#
#

sudo ./clean_all_but_scraped.py
python3 image_list.py
python3 image_noise.py
mv resized3 resized
python3 image_list_resized.py
python3 create_data.py
python3 train_model.py --learning_rate 0.0001
python3 remove_dropout.py




