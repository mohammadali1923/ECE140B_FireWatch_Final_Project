# ECE140B_FireWatch_Final_Project

#Computer Vision
 - Need a raspberry pi with an sd card running raspbian with a minimum of 4 GB (Preferably over 8GB) running headless preferably in order to save space (You could use Rasbian Buster Lite here and flash it on the SD card using BalenaEtcher https://www.raspberrypi.org/downloads/raspbian/).
 - First, access the raspberry pi and make sure pip3 and python3 are installed.
 - Next, pull from this repository. It has everything needed including python files that run for mp4 files.
 - https://github.com/tobybreckon/fire-detection-cnn
 - This is a very large repo a little bit over 2 GB, make sure to install the models installation, but delete the test mp4 video in models as the video file is extremely large and unnecessary. Just follow the instructions in the readme file and it should be good. Again, make sure to download the sh ./download-models.sh part, but delete the video as you DO NOT need it and is unnecessary and a waste of space.
 - Next, set up the virtual environment using this site https://www.tensorflow.org/install/pip to install tensorflow and be sure to make sure that you use pip3 (maybe sudo pip3 if it does not work) install tensorflow==1.14 and make sure it is not tensorflow 2.0 or else it will not work. Also install pip3 install opencv and pip3 install opencv-contrib-python. If you receive errors in installation, I would google it and I found most of the problems solved from forums like stack overflow where people have the same issue.
 - Next, put the firenet_2.py from this rep into the one pulled earlier with all the tensorflow files.
 - Lastly, run this line to access the live camera and view the fire detection    python3 firenet_2.py.
