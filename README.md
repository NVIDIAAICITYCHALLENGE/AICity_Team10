# AICity_Team10
The model is based on the YOLO v2.
You can find the related information in https://pjreddie.com/darknet/yolo/. Please install the YOLO first.
And replace the related files then.

The files below are used to postprocess the files.
The change.py is used for processing the output of 
YOLO, which can rivise the prediction out of range and remove the wrong prediction in logic.
The input of change.py is the output of YOLO in the format of imagenet and the txt file as the mapping_480.txt.
The imagenet-detection.txt is a result in the format of imagenet.
The file_count.py is used to count the files.
The mapping_create.py is used to creat mapping_480.txt with val.
The compare.py is used to compare files'name in 2 folders.
The line_count.py is used to count the lines in a file.
The above 4 files are used specially in the challenge.

These files are used for aic480. The codes for aic1080 and aic540 is similar to them.

For training, the command is as "./darknet detector train cfg/voc.data cfg/yolo-voc.2.0.cfg darknet19_448.conv.23".
For validating and testing, the command is as "./darknet detector valid cfg/voc.data cfg/yolo-voc.2.0.cfg /workspace/darknet/backup/yolo-voc.backup".
For testing, the command is as "./darknet detector recall cfg/voc.data cfg/yolo-voc.2.0.cfg /workspace/darknet/backup/yolo-voc.backup".
Please download darknet19_448.conv.23 from  https://pjreddie.com/darknet/yolo/.
