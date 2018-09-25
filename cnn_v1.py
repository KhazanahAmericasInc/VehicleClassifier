import tensorflow as tf
import numpy as np
import os
import sys
import argparse
import cv2

###
# This script uses a trained CNN model to predict the classes of input images. The input argument includes a folder
# which will be searched for images. The classification of all images will be displayed in a window along with the image.
# The window requires a key press to move on to the next image. 
### 

# Global Variables
INPUTOPERATION = "input"
OUTPUTOPERATION = "output"
IMAGESHAPE = 64
LABELS = ("SUV", "SEDAN", "TRUCK")

# Given a file path to a tensorflow model, it loads the graph.
def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

# This function takes an image and a pixel size. It resizes the largest dimension to the desired size and then pads
# the remaining pixels with padColor to create a square image. It returns the square image.
def resizeAndPad(img, size, padColor=128):

    h, w = img.shape[:2]
    sh = size
    sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
        pad_horz = (sw-new_w)/2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    else: # square image
        new_h, new_w = sh, sw
        pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

    padColor = [padColor]*3

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    return scaled_img

# Main function: Takes the input command arguments and loads the tensorflow model. It iterates through all the images
# in the input directory and displays the image with the label.
def main(args):
    graph = load_graph(args.model_file)

    print ("Graph Loaded")

    # Finds the input and output nodes
    input_name = "import/" + INPUTOPERATION
    output_name = "import/" + OUTPUTOPERATION
    input_operate = graph.get_operation_by_name(input_name)
    output_operate = graph.get_operation_by_name(output_name)

    cwd = os.getcwd()
    test_dir = os.path.join(cwd, args.test_data)
    files = os.listdir(test_dir)
    
    with tf.Session(graph = graph) as sess:
        
        # Iterates through all the images
        for path in files:
            label_img = np.zeros((100, 300), dtype=np.uint8)
            imagepath = os.path.join(test_dir, path) 
            image = cv2.imread(imagepath)
            if image is None:
                print("INVALED IMAGE PATH: " + imagepath)
                continue
            resized = resizeAndPad(image, IMAGESHAPE)

            x = resized[:, :, ::-1]
            x = x.astype('float32')
            x_in = (x - 128.) / 128.
            x_in = np.reshape(x_in, (-1, IMAGESHAPE, IMAGESHAPE, 3))
            results = sess.run(output_operate.outputs[0], {input_operate.outputs[0]: x_in})
            results = np.squeeze(results)

            index = np.argmax(results)

            # check confidence level, for negative classification
            fLabel = LABELS[index] if results[index] >= 0.995 else "Unknown"
            print("Label",LABELS[index],"Confidence:",results[index],"Final Label:", fLabel)

            cv2.putText(label_img, fLabel , (10, 75), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, 255, 1, 8, False)

            # Shows a window with the image and the label. Waits for key press
            cv2.imshow('label', label_img)
            cv2.imshow('frame', image)
            cv2.waitKey(5000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_file", default="model.pb", help="name of file containing trained model")
    parser.add_argument("--test_data", default="img", help="name of folder containing test images")
    args = parser.parse_args()
    main(args)
