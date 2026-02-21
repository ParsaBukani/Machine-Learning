# Deep Learning Foundations & Neural Architectures

_Machine Learning — University of Tehran_

This project provides a rigorous exploration of deep learning, ranging from theoretical proofs in estimation theory and optimization to the practical implementation of transfer learning. It covers the mathematical mechanics of neural networks, including weight initialization stability, the "Dead ReLU" phenomenon, and representational capacity, while empirically comparing shallow architectures with deep convolutional networks (VGG-11) on image classification tasks.

## Tasks

1.  **Estimation & Optimization Theory**
    -   **Maximum Likelihood Estimation (MLE)**: Analytical derivation of the MLE for a parametric distribution and verification of its global maximum using second-order derivatives.
    -   **Logistic Regression**: Derivation of the Stochastic Gradient Descent (SGD) update rule for a single-feature binary classifier using the cross-entropy loss function.
    -   **Newton's Method**: Formal proof demonstrating that for $L_2$-regularized linear regression, a single Newton step reaches the global minimizer regardless of the initial weights.

2.  **Neural Network Mechanics**
    -   **Representational Capacity**: Analysis of various ReLU computation graphs to identify which continuous piecewise linear functions they can represent, highlighting the differences between deep narrow chains and parallel architectures.
    -   **Dead ReLU Analysis**: Mathematical proof of the "zero-gradient" problem in ReLU neurons. Derivation of activation probabilities based on bias initialization and Gaussian pre-activations.
    -   **Variance Preservation**: Derivation of **Xavier (Glorot) Initialization** by solving symmetric constraints for forward and backward passes to prevent exponential signal amplification or decay in deep networks.

3.  **Advanced Loss Functions**
    -   Derivation of the equivalence between MLE and multi-class Cross-Entropy.
    -   Analysis of **Noisy Labels**: Constructing robust error functions for binary classification where labels may be flipped with a certain probability.
    -   Implementation of alternative target encodings ($t \in \{-1, 1\}$) and the corresponding hyperbolic tangent ($tanh$) activation strategy.

4.  **Transfer Learning & CNNs**
    -   Comparison of three models on the **CIFAR-10** dataset: a flattened MLP baseline, a Frozen VGG-11 (pre-trained on ImageNet), and a Fine-Tuned VGG-11.
    -   Investigation of **Spatial Inductive Bias** in CNNs (local receptive fields and weight sharing) versus the independent pixel processing of MLPs.
    -   Evaluation of optimization stability and convergence speed provided by pre-trained weight initialization.

## Project Report
_A detailed **Report** with mathematical proofs, variance stability analysis, and VGG-11 performance plots is available here: [Report.pdf](https://github.com/ParsaBukani/Machine-Learning/blob/main/HW5/Content/Report.pdf)_

## Acknowledgements

Developed under the supervision of **Mohammadreza A. Dehaqani and Babak N. Arabi**.  
Special thanks to **Alireza Akhoundi, Parisa Yahyapour, Mehdi Moosavi, and Hossein Noroozi** for project design and assistance.
