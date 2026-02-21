# Support Vector Machines & Decision Trees

_Machine Learning — University of Tehran_

This project explores two pillars of supervised learning: Support Vector Machines (SVM) and Decision Trees. It combines theoretical analysis of kernel methods and information theory with hands-on implementation, including building an ID3 classifier from scratch and solving the SVM primal formulation using quadratic programming.

## Tasks

1.  **Support Vector Machines (SVM)**
    -   **Conceptual Analysis**: Investigation of the dual formulation, the significance of support vectors, and the mathematical intuition behind the **Kernel Trick** in infinite-dimensional Hilbert spaces.
    -   **Manual Derivation**: Solving a symmetric 4-point classification problem to find optimal dual variables ($\alpha_i$) and primal parameters ($w$, $b$) for a hard-margin SVM.
    -   **Kernel Exploration**: Deriving explicit feature maps for polynomial kernels and analyzing the effects of **Linear, RBF, and Polynomial** kernels on model capacity and overfitting.

2.  **Decision Tree Learning (ID3)**
    -   **Splitting Mechanics**: Manual calculation of **Entropy** and **Information Gain** to determine root node selection in the ID3 algorithm.
    -   **Mathematical Proofs**: Using **Jensen's Inequality** to prove the non-negativity of Information Gain and demonstrating the concavity of the entropy function.
    -   **Search Bias**: Analyzing the failure of greedy search in **XOR problems** and distinguishing between "Preference Bias" and "Restriction Bias."

3.  **Programming & Implementation**
    -   **SVM Pipeline**: Building a diabetes diagnosis classifier using the Pima Indians dataset, featuring median imputation for missing values, feature scaling, and hyperparameter tuning via **GridSearchCV**.
    -   **Custom QP-SVM**: Implementing a Soft-Margin SVM from scratch by transforming the primal objective into a **Quadratic Programming** problem solved via `cvxpy`.
    -   **ID3 from Scratch**: Developing a full decision tree classifier that handles both discrete and continuous features, including a **Post-Pruning** experiment to analyze the trade-off between tree complexity and generalization.

## Project Report
_A detailed **Report** with mathematical derivations, decision boundary visualizations, and pruning analysis is available here: [Report.pdf](./Report.pdf)_

## Acknowledgements

Developed under the supervision of **Babak N. Arabi, Mohammadreza A. Dehaqani, and Mostafa Tavassolipour**.  
Special thanks to **Hamed Soltani and Parisa Mohammadi** for project design and assistance.
