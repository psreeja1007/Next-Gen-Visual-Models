* **Make Pneumonia or Normal classifier based on Chest X-Ray**
> It will take time in training!
* Download data from [here](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
* Or if you are using google colab GPU or even colab, you can load data in google colab by running following
```
!pip install kaggle
!mkdir ~/.kaggle
!mv kaggle.json ~/.kaggle/
!kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
!unzip chest-xray-pneumonia.zip
```
> **Accuracy on testing data should be more than 60%**


## Description of Assignment:

- Used a CNN model on a dataset of **pneumonia** and **normal** X-rays.
- Applied **data augmentation** for better generalization.
- Added **batch normalization** to stabilize training.

## Results
- Achieved **80.13% accuracy** on the test set.