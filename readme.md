
# Vehicle Classifier
This is a hard-fork and re-organization of the *SensortowerCNNClassifier* Repository.

## Dependencies
The following list of dependencies are required for the classifier and training scripts to function.
- Python 3
	- Tensorflow
	- Numpy
	- OpenCV
	- Pillow
	- Matplotlib
	- BeautifulSoup4
	- Urllib3


## Classification Quickstart
1. Clone the repository 
2. Create a folder with images of vehicles
3. Run the following command in the terminal:
```
python3 cnn_v1.py --test_data="<PATH_TO_VEHICLE_IMAGES>"
```

## Create-your-own Classifier Quickstart
1. Clone the repository
2. Create a folder named "scraped_images" in the root of the project directory
3. Create folders for each class in "scraped_images" (i.e. "./scraped_images/dogs", "./scraped_images/cats"
4. Modify the hyper-parameters defined in train_model.py
5. Run the "./auto.sh" bash script
6. Modify cnn_v1.py to contain the custom class labels
7. run cnn_v1.py with the new model


## Contents

### Bash Scripts
To use a bash script, add give the user permission to execute the file by typing the following command in the terminal:
```
chmod u+x <ScriptName>
```
For Example:
```
chmod u+x auto.sh
```
Then type the following command to run the script:
```
sudo ./<ScriptName>
```
For Example:
```
./auto.sh
```


| Script Name | Description |
|:------------|:------------|
|scrape_default.sh|Automatically scrapes the default dataset (dogs, pugs, puppies), resizes, creates data, trains neural net and trains it.|
|auto.sh|Given a custom dataset placed in ./scraped_images/, with images separated by class folders, it will automatically resize and train the neural net with the hyper-parameters defined in train_model.py|
|clean.sh|Cleans the repository of images and the default generated neural net.|
|rename.sh|Removes some non-image files obtained from google images, and renames the image files to be parsable by the python scripts. Works within it's own directory, i.e. must be copied to the specific class folder before used. |

For more detailed information, please open to view the script files themselves.


### Python Scripts

| Script Name | Flags | Description |
|:------------|:------------|:-----------|
| cnn_v1.py | <ul><li> *model_file* - set a custom path to the trained model </li> <li> *test_data* - set a custom path to the folder containing vehicle images </li> </ul> | A visual run of the classifier. Classifies the images in "./img" by default, and shows the images as they are inferenced.|
| cnn_v2.py | <ul><li> *model_file* - set a custom path to the trained model </li> <li> *test_data* - set a custom path to the folder containing vehicle images </li> <li> *output_file* - set the path to the output file of the inference results </li> | A non-visual run of the classifier, the output is sent to the output file ("./net_output.txt") by default.|
| scrape_image.py | <ul><li> *query* - set a list of keywords for the google search </li> <li> *folder_name* - set a custom folder path for the output images to be stored in</li> | This script scrapes images on google images based on the input query list.|
| image_list.py | <ul><li> *output_list_file* - set a custom name for the output ".csv" file </li> <li> *output_summary_file* - set a custom name for the output ".txt" file </li> <li> *output_class_hist* - set an output name for the histogram </li> <li> *maxsample* - set the max number of images to take per class, default is -1 for all images</li></ul>| This script creates a ".csv" list of all images in "./scraped_images", a ".txt" with the number of images per class and an image that shows the class distribution in a bar graph. |
| image_resize.py | <ul><li> *input_list_file\** - set the path of the ".csv" file that contains the images to process </li> <li> *input_directory\** - set the path of the directory that contains the images </li> <li>*output_directory\** - set the output directory to save processed images</li> <li>*image_size* - set the size of the resized images, default is 64x64</li></ul> | This script resizes the images from the training set. |
| image_noise.py | <ul><li> *input_list_file\** - set the path of the ".csv" file that contains the images to process </li> <li> *input_directory\** - set the path of the directory that contains the images </li> <li>*output_directory\** - set the output directory to save processed images</li> <li>*image_size* - set the size of the resized images, default is 64x64</li></ul> | This script resizes the image and also tries to replace the background pixels for randomized noise. |
| create_data.py | <ul><li> *input_list_file\** - set the name of the ".csv" file that contains the images to process"</li><li> *input_directory\** - set the name of the directory that contains the pre-processed images </li> <li> *out_file\** - set the name of the output binary file </li> <li> *num_channel[1 or 3]* - sets colour schema, where 1 is grayscale and 3 is three-channel RGB</li> <li> *shuffle* - shuffle order of the images for possibly better training </li><ul> | Generates a binary file of the training data. |
| train_model.py | <ul><li>*train_data* - set the path to the binary file from create_data.py </li> <li> *output_model_name\** - set the name of the trained output model</li> <li> *output_directory\** - set the name of the output directory that stores the model </li> <li> *previous_model* - set the path to the previous model to continue training </li> <li> *learning_rate\** - set the learning rate of the training set, 0.0001 is suggested by tensorflow </li></ul>| Trains the CNN and outputs a model. |
| remove_dropout.py | <ul><li>*model_directory_name* - set the name of the directory the model is saved in</li><li> *model_file* - set the name of the model file</li> <li>*output_model_file* - set the filename of the output model</li> | This script removes the redundant layers of the trained model. |

\* - required flag

### Pre-trained Neural Network Models

| Script Name | Labels |
|:------------|:------:|
| model.pb | ("SUV", "SEDAN", "TRUCK") |
| multi_trucksmodel.pb | ("SUV", "FREIGHT TRUCK", "TIMBER TRUCK", "SEDAN", "PICKUP TRUCK", "OIL TRUCK") |
| trucksmodel.pb | ("SEDAN", "TIMBER TRUCK", "OIL TRUCK") |
## Image Scraping
To scrape more than 100 images, please use the following tool: [googleimagesdownload](https://github.com/hardikvasa/google-images-download#troubleshooting-errors-issues)

Please follow the tutorial in the googleimagesdownload README.md on downloading more than 100 images.

#### Example Command
```
googleimagesdownload --keywords "Freight Truck" --chromedriver ./chromedriver --limit 1000
```