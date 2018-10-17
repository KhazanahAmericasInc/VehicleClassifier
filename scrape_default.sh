#!/bin/bash

#
#
# This bash script scrapes dogs/pugs/puppies
# and automatically resizes the images to the
# appropriate training size.
#
#

./clean.sh
python3 scrape_image.py
python3 image_list.py
python3 image_noise.py
mv resized3 resized
python3 image_list_resized.py
python3 create_data.py
python3 train_model.py --learning_rate 0.001
python3 remove_dropout.py
