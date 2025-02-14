![GAN-Assignment](https://github.com/shoryasethia/Next-Gen-Visual-Models/blob/main/Week4/Assignment/GANs-Assignment.png)

# DCGAN Implementation on Cats Dataset

## Overview  
In this assignment, I implemented a **Deep Convolutional Generative Adversarial Network (DCGAN)** to generate realistic images of cats. The dataset was sourced from **Kaggle**.

## Experiment Details  
- Used a **CNN-based generator** with **Transposed Convolutions** to upscale images.  
- Used a **CNN-based discriminator** with **Batch Normalization** and **Leaky ReLU**.  
- Trained the model with **Binary Crossentropy loss** and **Adam optimizer**.  
- Compared **two different models** with varying architectures and hyperparameters.

## Results  
| Model | Generator Loss | Discriminator Loss |
|-------|---------------|--------------------|
| First Model | 0.91 | 0.06 |
| Second Model | 0.77 | 0.14 |

- The **Generator loss** decreased from **0.91 to 0.77**, indicating improved image generation quality.  
- The **Discriminator loss** increased from **0.06 to 0.14**, suggesting better ability to distinguish real vs. fake images.  

## Conclusion  
This study demonstrates the importance of **fine-tuning architectures and hyperparameters** in GANs. The second model showed improved performance with a **better balance between Generator and Discriminator** losses.

**References:** I used the **Kaggle Cats dataset**  
