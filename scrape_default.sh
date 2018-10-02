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
