# Traffic Sign Dataset
Dataset with Italian Traffic Signs, helpful for YOLO

This dataset was created by four students of University of Roma 3 for a project on 
Machine Learning and Sistemi Intelligenti per Internet.\
Images were collected from Google Maps and they were labelize with https://github.com/tzutalin/labelImg in a format helpful
for training a YOLO neural network.

Before you start using the dataset there is a script (TrainTestFiles.py) into root of project who is helpful for create the train.txt and test.txt files.\
Before to start the script you can modify TrainTestFiles.json where you can set the percentual of images used for train and test set, default is 70% for train and 30% for test.\
\
You can launch the script with:
```
python TrainTestFiles.py
```
\
You can add more images at the dataset, at the end you must modify the key `txts_size` in TrainTestFiles.json.

If you use the dataset please to add a star at the project :)
