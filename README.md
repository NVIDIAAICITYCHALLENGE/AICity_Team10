# AICity_Team10
The model is based on the YOLO v2.
You can find the related information in https://pjreddie.com/darknet/yolo/.
The related file are yolo-voc.2.0.cfg and voc.data in cfg folder and voc.names 
in /data folder.

The change.py in the folder of postprocessing is used for processing the output of 
YOLO, which can rivise the prediction out of range and remove the wrong prediction in logic.
The input of change.py is the output of YOLO in the format of imagenet 
and the txt file as the mapping_1080.txt.
