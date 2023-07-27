# Skittle-Colour-Classification

 In this project, I aimed to classify and detect the different colours/flavours of skittles, and detect how many of each colour are in a pack. I chose to tackle this problem with ai, as I watched a video of someone colourblind attempting to sort skittles by their colours, and ended up finding it very difficult to differentiate between them. This proejct can help those who are colourblind, differentiate between these different flavoured skittles.
 
 I have also had a thought that the flavours of skittles in a pack are sometimes skewed towards favouring certain colours, as I occasiaonaly get far more of one colour than another. 
 
 This ai can help me detect this, as it can differentiate between the different flavours. As I am in the UK, the 5 different colours/flavours of a standards skittles pack is: Green(Apple), Orange(Orange), Red(Strawberry), Purple(Blackcurrant) and Yellow(Lemon).

![Here is an image of an assortment of skittles, showcasing the 5 different colours I will be detecting in this project:](https://hips.hearstapps.com/hmg-prod/images/skittles-candy-3-pound-bag-1613163635.jpg)

## The Algorithm

This project makes use of the jetson nano to test our ai model, and I made a retrained version of resnet-18, as the base AI program. The dataset used for the retrained model, I made myself, by taking pictures of individual skittles of each colour, and groups of different colours of skittles. These images/skittles are seperated and labeled by their colours. When we run the program, imagenet.py will take an inputted image of a skittle, and it will output what colour it think the skittle is, as the trained model of resnet-18 can differentiate between the 5 different colours of skittle (Red, Green, Orange, Purple, Yellow).

## Running this project

Required Libraries:
-resnet-18
-imagenet

1. Log into your jetson nano on VScode
2. Make sure you have jetson-inference installed
3. install the project: git clone https://github.com/MikeyMictan1/Skittle-Colour-Detection.git
4. Get into the directory with the project by doing: ```cd project_file_folder/Classification```
5. Run in the terminal: ```python3 my-imagenet.py /dev/video0 rtp://your_ip_address:1234```
6. Make sure your camera is on, make sure the camera feed is ran through a .sdp file
7. Put a skittle in front of the camera, and it can detect the 5 different colours/flavours of skittle (red, green, yellow, orange, purple)

[View a video explanation here](https://www.youtube.com/watch?v=1UHk__i9R7w)
