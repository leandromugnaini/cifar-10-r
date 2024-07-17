## CIFAR10-R(endition)

CIFAR10-R is a downsampled variant of [ImageNet-R(endition)](https://github.com/hendrycks/imagenet-r). The images are resized to CIFAR10-like size, 32x32. Compared to CIFAR10, it contains two types of distribution shifts: CIFAR10 to ImageNet and ImageNet to ImageNet-R.

This repository aims to use the data provided by Mr. Li ([original repository](https://github.com/TreeLLi/cifar10-r)) to create a numpy file (.npz) so it can be easily used with neural architectures.

### Steps to run

1. If you want to just use the adversarial attack data, you can just load the ```cifar-10-r.npz``` file
2. If you want to reproduce the steps to create the dataset, follow the ```Reproducibility``` section

Note: always remember to apply the transformations of the original dataset to the CIFAR10-R data. The example code in the ```cifar_10_r_evaluation_example.ipynb``` notebook shows a case of how it can be used to evaluate a model (TensorFlow/Keras background). For a quick evaluation, I recommend using Google Colab so you don't have to worry about installing packages.

### Reproducibility

1. Delete or rename the ```cifar-10-r.npz``` file
2. Extract the file ```cifar-10-r.zip```
3. If you want, you can delete the original .zip file after extraction
4. Create a ```data``` folder
5. Place the extracted content in the data folder. Make sure you move the folders for each class. Remove empty folders if you want. The final file tree should look like this (hierarchical and alphabetical order):
```
├── data/
│   ├── automobile/
│   ├── bird/
│   ├── cat/
│   ├── deer/
│   ├── dog/
│   ├── frog/
│   ├── ship/
│   └── truck/
├── cifar_10_r_evaluation_example.ipynb
├── LICENSE
├── prepare_data.py
└── README.md
```
6. Run the ```prepare_data.py``` script (code adapted from code provided by Prof. Artur ([GitHub](https://github.com/arturjordao))). It will generate the ```cifar-10-r.npz``` file.
7. Use the ```cifar-10-r.npz``` as needed

Note: (note repeated for emphasis) always remember to apply the transformations of the original dataset to the CIFAR10-R data. The example code in the ```cifar_10_r_evaluation_example.ipynb``` notebook shows a case of how it can be used to evaluate a model (TensorFlow/Keras background). For a quick evaluation, I recommend using Google Colab so you don't have to worry about installing packages.

