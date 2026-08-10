# CS231n Deep Learning for Computer Vision

## Goals

In this assignment, you will implement language networks and apply them to image captioning on the COCO dataset. Then you will be introduced to self-supervised learning to automatically learn the visual representations of an unlabeled dataset. Next, you will implement diffusion models (DDPMs) and apply them to image generation. Finally, you will explore CLIP and DINO, two self-supervised learning methods that leverage large amounts of unlabeled data to learn visual representations.

The goals of this assignment are as follows:

- Understand and implement Transformer networks. Combine them with CNN networks for image captioning.
- Understand how to leverage self-supervised learning techniques to help with image classification tasks.
- Implement and understand diffusion models (DDPMs) and apply them to image generation.
- Implement and understand CLIP and DINO, two self-supervised learning methods that leverage large amounts of unlabeled data to learn visual representations.
- You will use PyTorch for the majority of this homework.

## Q1: Image Captioning with Transformers

The notebook [Transformer_Captioning.ipynb](Transformer_Captioning.ipynb) will walk you through the implementation of a Transformer model and apply it to image captioning on COCO.

## Q2: Self-Supervised Learning for Image Classification

In the notebook [Self_Supervised_Learning.ipynb](Self_Supervised_Learning.ipynb), you will learn how to leverage self-supervised pretraining to obtain better performance on image classification tasks. When first opening the notebook, go to Runtime > Change runtime type and set Hardware accelerator to GPU.

## Q3: Denoising Diffusion Probabilistic Models

In the notebook [DDPM.ipynb](DDPM.ipynb), you will implement a Denoising Diffusion Probabilistic Model (DDPM) and apply it to image generation.

## Q4: CLIP and Dino

In the notebook [CLIP_DINO.ipynb](DDPM.ipynb), you will implement CLIP and DINO, two self-supervised learning methods that leverage large amounts of unlabeled data to learn visual representations.
