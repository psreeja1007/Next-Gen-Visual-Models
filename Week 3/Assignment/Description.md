# Model Performance Analysis

## Overview  
In this experiment, I implemented and compared different Variational Autoencoder (VAE) architectures on the MNIST dataset. The focus was on evaluating how replacing the **encoder** and/or **decoder** with an **encoder-decoder architecture** affects performance.

## Observations  
- **Model 1 (Vanilla VAE)** and **Model 3 (Decoder with Encoder-Decoder Architecture)** performed almost similarly, with **Model 3 slightly outperforming Model 1**.  
- **Model 2 (Encoder with Encoder-Decoder Architecture)** and **Model 4 (Both Encoder & Decoder replaced with Encoder-Decoder Architecture)** showed the **worst performance**.  
- **Reconstruction Loss** was the major contributor to the overall loss, indicating that **optimizing the decoder** is crucial for improving model performance.

## Implementation Details  
- Used a **CNN-based encoder** with progressively downsampling.  
- Used a **CNN-based decoder** with progressively upsampling. 
- Applied **Batch Normalization** and **Leaky ReLU** for stable training.  
- Trained the model for **30 epochs** with a batch size of **128**.  
- Used **Binary Crossentropy** as the reconstruction loss and **KL Divergence** as the regularization term.  
- The dataset used was **MNIST**, with images resized accordingly.  
- **Took reference from the GeeksforGeeks website** for understanding key concepts of VAEs.

## Conclusion  
This study highlights the importance of **decoder optimization**, as it plays a significant role in **reducing reconstruction loss** and improving the overall VAE performance.