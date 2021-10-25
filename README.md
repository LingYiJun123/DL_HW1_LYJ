## DL_HW1_LYJ
Deep Learning homework


# Step by step procedure to recreate answer.txt

0.) Requirements, the usual: https://pytorch.org/get-started/locally/

1.) Clone github repo

2.) Download model8.pt into the 'models' folder using the given google drive link in link.txt.

3.) Download testing images and put it in a folder named "testing_images"

4.) Delete contents in answer.txt (or else the answer will be appended with the existing contents)

5.) Run python inference.py, that's all. No other modification needed. 

# Step by step procedures to recreate Model8.pt

1.) Create folder named "training_images", download all the training images there.

2.) Run the .py files in train and val folders (run mkdirscript.py [to make the class directories] first, followed by mvimgscript.py [to move the training images into the respective class labels] ).

3.) Then run python train.py
