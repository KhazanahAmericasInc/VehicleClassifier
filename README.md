
# Vehicle Classifier
This is a hard-fork and re-organization of the *SensortowerCNNClassifier* Repository.

## Classification Quickstart
1. Clone the repository 
2. Create a folder with images of vehicles
3. Run the following command:
```
python3 cnn_v1.py --test_data="<PATH_TO_VEHICLE_IMAGES>"
```

## Contents

| Script Name | Flags | Description |
|:------------|:------------|:-----------|
| cnn_v1.py | <ul><li> model_file - set a custom path to the trained model </li> <li> test_data - set a custom path to the folder containing vehicle images </li> </ul> | A visual run of the classifier. Classifies the images in "./img" by default, and shows the images as they are inferenced.|
| cnn_v2.py | <ul><li> model_file - set acustom path to the trained model </li> <li> test_data - set a custom path to the folder containing vehicle images </li> <li> output_file - set the path to the output file of the inference results </li> | A non-visual run of the classifier, the output is sent to the output file ("./net_output.txt") by default.|
