#!/bin/bash

#
#
# This script cleans all of the training data and
# scraped images from the directory.
#
#

rm -Rf scraped_images
rm -Rf resized2
rm -Rf resized3
rm -Rf output
rm -Rf resized

rm classhistogram.png datasummary.txt imagelist.csv nodropout.pb data.p
