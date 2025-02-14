* Load a pre-trained model (either VGG16 or VGG19 or InceptionV3)
* Check its accuracy using weights of `imagnet` dataset only on CIFAR10 dataset.
> Problem you will face, try to resolve it as well : imagnet had 1000 classes whereas CIFAR10 has only 10 classes
* Transfer Learning : Fine-Tune the chosen pre-trained model on CIFAR10 and then compare them
  

# Description of Assignment:

- Used pre-trained **VGG19** (ImageNet weights) and added extra layers.
- Compared performance with and without pre-trained weights.

## Results
| Model | Accuracy |
|-------|----------|
| Pre-trained | 0.04 |
| From scratch | 0.8311 |