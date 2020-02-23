import os
import glob as glob
import os
from imutils import paths
import random
import shutil
import numpy as np

orig_data_dir='E:/breast_cancer_brakhis/breast_data/'
base_path='E:/breast_cancer_brakhis/prep_data1/'

imagepath=list(paths.list_images(orig_data_dir))

random.shuffle(imagepath)
random.seed(4)
i=int(len(imagepath) * 0.8)
train_img_paths=imagepath[:i]
test_img_paths=imagepath[i:]
i=int(len(train_img_paths)*0.1)
val_img_paths=train_img_paths[:i]
train_img_paths=train_img_paths[i:]

train_path=os.path.sep.join([base_path,"train"])
valid_path=os.path.sep.join([base_path,"valid"])
test_path=os.path.sep.join([base_path,"test"])
print(train_path,valid_path,test_path)

datasets=[
    ("training",train_img_paths,train_path),
    ("validation",val_img_paths,valid_path),
    ("testing",test_img_paths,test_path)]

for (dType,imagePaths,baseOutput) in datasets:
    print("[INFO] building '{}'split".format(dType))

    if not os.path.exists(baseOutput):
        print("[INFO] creating '{}' directory".format(baseOutput))
        os.makedirs(baseOutput)

    for inputPath in imagePaths:

        filename=inputPath.split(os.path.sep)[-1]
        label=filename.split('_')[2].split('-')[0]

        labelPath=os.path.sep.join([baseOutput,label])

        if not os.path.exists(labelPath):
            print("[INFO] creating '{}' directory".format(labelPath))
            os.makedirs(labelPath)

        p=os.path.sep.join([labelPath,filename])
        shutil.copy2(inputPath,p)
        
