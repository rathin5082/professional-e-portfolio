# CIFAR-10 CNN with Attention Mechanism

This repository contains the implementation of a Convolutional Neural Network (CNN) with an attention mechanism for the CIFAR-10 dataset. The model achieves a test accuracy of 92.2% on unseen data.

## Overview

The architecture is designed to classify 10,000 test images from the CIFAR-10 dataset (10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck). It uses a modular block-based structure with parallel convolutional layers within each block and sequential stacking of blocks. Attention weights are computed to emphasize important sub-network outputs.

Key features:
*Parallel convolutional layers inside "Intermediate Blocks" for feature extraction.
