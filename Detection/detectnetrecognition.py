#!/usr/bin/env python3

import sys
import argparse

from jetson_inference import detectNet
import jetson_utils
from jetson_utils import videoSource, videoOutput, logUsage

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage() + logUsage())

parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="ssd-inception-v2", help="pre-trained model to load (see below for options)")


is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

opt = parser.parse_args()

img = jetson_utils.loadImage(opt.filename)
# load the object detection network
#net = detectNet(args.network, sys.argv)


# note: to hard-code the paths to load a model, the following API can be used:
#
net = detectNet(model="resnet18.onnx", labels="labels.txt", 
                 input_blob="input_0", output_blob="output_0")

detections = net.Detect(img)
items = []
print("detected {:d} objects in image".format(len(detections)))

for detection in detections:
    stringout = net.GetClassDesc(detection.ClassID)
    print(f"One object was a: {stringout}")
    items.append(stringout)
    
net.PrintProfilerTimes()

if "person" and "bird" in  items:
    print("There is a person and a bird in the image! chirp chirp")

else:
    print("no joy")