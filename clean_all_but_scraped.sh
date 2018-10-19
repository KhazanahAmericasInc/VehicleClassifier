#!/bin/bash

#
#
# This bash script cleans all files except
# scraped_images
#
#

rm -Rf resized2
rm -Rf resized3
rm -Rf output
rm -Rf resized

rm classhistogram.png datasummary.txt imagelist.csv nodropout.pb data.p
find . -name '*.csv' -type f -delete
