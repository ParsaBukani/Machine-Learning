# Machine Learning Basics

_Machine Learning — University of Tehran_

This project explores the fundamental principles of Bayesian decision theory, maximum likelihood estimation (MLE), and probabilistic classification. It covers theoretical derivations of Bayes risk and decision boundaries, as well as practical implementations of Naive Bayes for text classification and a custom color-based image classifier for identifying cloudy versus clear skies.

## Tasks

1.  **Bayesian Decision Theory**
    -   Analysis of **Bayes Rule** versus **Randomized Decision Rules**, proving that randomized rules cannot yield a smaller risk than the deterministic Bayes rule.
    -   Derivation of optimal thresholds for Gaussian distributions under the zero-one loss function.
    -   Calculation of linear and quadratic **decision boundaries** for two-class recognition problems based on feature means, covariances, and prior probabilities.

2.  **Maximum Likelihood Estimation (MLE)**
    -   Derivation of MLEs for **Bernoulli distributions** in the context of Naive Bayes parameter estimation.
    -   Application of **Poisson distributions** to model event frequencies (e.g., goals scored per game) and predicting future outcomes based on sample means.
    -   Proving the mathematical connection between maximizing log-likelihood and minimizing the **Mean Squared Error (MSE)** in linear regression.

3.  **Classification Implementation**
    -   **Naive Bayes**: Development of a spam filter using a subset of the TREC Public Spam Corpus. Implementation includes Laplace/m-estimate smoothing and log-probability comparison to handle numerical precision.
    -   **Image Classification**: Design of a custom rule-based classifier for "Cloudy vs. Clear Sky" images using **HSV color space** features (Saturation and Brightness).
    -   Performance evaluation using Confusion Matrices, Precision, Recall, and Accuracy metrics.

## Project Report
_A detailed **Report** with mathematical derivations, decision boundary plots, and classification analysis is available here: [Report.pdf](./Report.pdf)_

## Acknowledgements

Developed under the supervision of **Mohammadreza A. Dehaqani, Babak N. Arabi, and Mostafa Tavassolipour**.  
Special thanks to **Aidin Kazemi and Taha Majlesi** for project design and assistance.
