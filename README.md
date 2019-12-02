# traffic_light_detection
Traffic Light Detection - Using Bosch Small Traffic Lights Dataset

This repository has the Google Colab Script that can be used to set up a VM to build and train using Darknet.

I have tried training the Bosch Traffic Light Dataset and seen that the training runs file.

I have used the darknet repository from https://github.com/AlexeyAB/darknet and follwed the instruction from this repos readme file.

PRE-REQUISITE IN YOUR LAPTOP/DESKTOP

1. PYTHON 3.7
2. PyYAML and lxml packages.

Steps that I followed are:

1. Download the Bosch dataset from https://hci.iwr.uni-heidelberg.de/node/6132
2. UnZip the RGB based training dataset. Name the extracted folder as "train_rgb".
3. UnZip the RBG based test dataset. Name the extracted folder as "test_rgb".
4. Copy the bosch_to_pascal.py script to the same level as "train_rgb" and "test_rgb" folder.
5. Create folders called "labels", "train_rgb_pascal" and "test_rgb_pascal" in the same level as "train_rgb" and "test_rgb" folder.
6. Run the script bosch_to_pascal.py with the following arguments. This sript shall parse the YAML file that has the annotation details and generate XML for each of the annotated image in the dataset.
"python bosch_to_pascal.py train_rgb/train.yaml train_rgb_pascal"
"python bosch_to_pascal.py test_rgb/test.yaml test_rgb_pascal"
7. You should see several xml files under "train_rgb_pascal" and "test_rgb_pascal" folder respective with the same name as training and test images of the dataset.
6. Now run the "my_voc_label.py" script:
"python my_voc_label.py"
7. You should see several .txt files under labels/train_rgb and labels/test_rgb respectively with the same name as training and test images of the dataset.
8. You should also see a file called "obj.names" created at the same level as "labels" folder. This file is also available in the repo.

Over to Google Colab:

1. Run the "yolov3_traffic_lights.ipynb" in the Google Colab Notebock environment with GPU runtime type.
2. You would be asked to mount yout Google Drive. Please do so.
3. After the execution completes; you should see darknet_linux folder in your Google Drive.
4. Now copy the "darknet/yolov3_traffic_lights.cfg" from this repo to <GOOGLE DRIVE>/darknet_linux/.
5. Now copy the "darknet/obj.data" from the repo to <GOOGLE DRIVE>/darknet_linux/.
6. Now copy the "darknet/obj.names" from the repo to <GOOGLE DRIVE>/darknet_linux/.
7. Now copy the "darknet/data/train.txt" from the repo to <GOOGLE DRIVE>/darknet_linux/data/.
8. Create a directory called "obj" under <GOOGLE DRIVE>/darknet_linux/data/.
9. Copy all the .txt label files of the training images from your PC to <GOOGLE DRIVE>/darknet/data/obj.
10. Copy all the training .png images to <GOOGLE DRIVE>/darknet/data/obj
  
Running training in Google Colab manually:
1. Run the followng command to train using darknet in Google Colab prompt. "cd" to <GOOGLE DRIVE>/darknet_linux.
  "!./darknet detector train obj.data yolov3_traffic_lights.cfg darknet53.conv.74 -dont_show"
  
This should create the .weights file under <GOOGLE DRIVE>/darknet_linux/backup
  
How to test this weight files?
1. This repo also has a folder called "workspace". This folder has a VS2015 project which extends the OpenCV "object_detection" sample to read images recursively from a folder and use YOLOv3 for object detection.
2. Checkout the sample project and update the following project settings as per your development environment. Need opencv development environment as pre-requisite.

  a) Add additional include directories to opencv include directory.
  b) Add additional lib directories to opencv lib directory.
  c) Ensure the path to opencv dll files are added to the global environment path variable.
  d) Update the startup command line arguments to reflect the path to the argument based on your development environment.
  
Example:
-@alias=small -input=D:\object_detection\train_rgb\rgb\train -model=D:\object_detection\yolov3_traffic_lights_last.weights -config=D:\object_detection\darknet\yolov3_traffic_lights.cfg -classes=D:\object_detection\darknet\obj.names -backend=3 -target=0 --scale=0.00392 -width=416 -height=416

-input - This is that path to the test image files
-model - This is the path to the YOLOv3 weight files generated after training.
-config - This is the path to YOLOv3 cfg files used during training.
-classes - This is the path to the list of object class names used during training. 

3) Restart the visual studio and rebuild.
4) Happy Testing!
