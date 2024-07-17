import numpy as np
import sys
import os
from PIL import Image
from numpy import asarray
from sklearn import preprocessing
import h5py
from sklearn.model_selection import train_test_split

# Create a dictionary based on the provided mapping
label_dict = {
    "airplane": 0,
    "automobile": 1,
    "bird": 2,
    "cat": 3,
    "deer": 4,
    "dog": 5,
    "frog": 6,
    "horse": 7,
    "ship": 8,
    "truck": 9
}

def to_categorical(y, num_classes):
    return np.eye(num_classes)[y]

def folder_to_npz(path=''):
    X = []
    y = []
    dirnames = os.listdir(path)
    for dir in dirnames:
        images = os.listdir(os.path.join(path, dir))
        for image in images:
            img = Image.open(os.path.join(path, dir, image))
            # Uncomment the following lines if you want to see the images
            # import matplotlib.pyplot as plt
            # plt.imshow(img)

            # Uncomment the following line if you need to resize the images
            # img = img.resize((224, 224))
            # plt.imshow(img)

            X.append(np.array(img))
            y.append(label_dict[dir])

    X = np.array(X)
    y = np.array(y)
    y = to_categorical(y, num_classes=len(label_dict))
    print('Data format from', path)
    print(X.shape)
    print(y.shape)
    return X, y


if __name__ == '__main__':
    np.random.seed(12227)

    X, y = folder_to_npz('Dataset1/Grouped_select')

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.3, random_state=42)

    np.savez_compressed('Dataset1', X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)