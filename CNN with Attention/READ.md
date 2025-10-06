# CIFAR-10 CNN with Attention Mechanism

This repository contains the implementation of a Convolutional Neural Network (CNN) with an attention mechanism for the CIFAR-10 dataset. The model achieves a test accuracy of 92.2% on unseen data.

## Overview

The architecture is designed to classify 10,000 test images from the CIFAR-10 dataset (10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck). It uses a modular block-based structure with parallel convolutional layers within each block and sequential stacking of blocks. Attention weights are computed to emphasize important sub-network outputs.

Key features:
- Parallel convolutional layers inside "Intermediate Blocks" for feature extraction.
- Attention mechanism via weighted combination of block outputs.
- Data augmentation for improved generalisation.
- Skip connections and max pooling for deeper training stability.

## Architecture

The code accompanying this report follows the basic architecture wherein the Convolutional Neural Network layers are inside a composite unit referred to as “Intermediate block”. These layers receive the same input i.e. the in channels for the layers in a block is the same. In the code, it is 3 for the first block. This type of architectural arrangement of the layers is parallel as the layers in a block have the same input. The blocks however, are arranged in a sequential manner making the output channels from a block, say A, become the in channels for block B. To summarise, the blocks are sequential with each block consisting of convolutional layers arranged in parallel.

The second part of the basic architecture is the computation of the weight vector. The weight vector here represents the attention weights that give an estimate of how significant the outputs from each sub-network(convolutional layer + any modifications if needed) is in regards to the final output of the block. It is given by:

$x = a_1 C_1(z) + a_2 C_2(z) + \dots + a_L C_L(z)$, 

where $L$ = number of convolutional layers,

$a$ = vector computed by the block,

$C$ = Convolutional layer
