# Clustering, Dimensionality Reduction & Feature Selection

_Machine Learning — University of Tehran_

This project explores a broad spectrum of unsupervised learning techniques and feature engineering strategies. It covers the theoretical foundations and practical applications of clustering algorithms (K-Means, Agglomerative, GMM), dimensionality reduction methods (PCA, Kernel PCA, LDA), and various feature selection paradigms (Filter, Wrapper, and Embedded).

## Tasks

1.  **Clustering Analysis**
    -   **K-Means**: Manual execution of a full iteration, including point assignment based on Euclidean distance and centroid updating.
    -   **Hierarchical Clustering**: Comparison of linkage strategies (Single vs. Complete), focusing on computational complexity and robustness to outliers.
    -   **Agglomerative Implementation**: Manual construction of a dendrogram using complete linkage for a 2D dataset.
    -   **Image Segmentation**: Applying K-Means and Gaussian Mixture Models (GMM) using the EM algorithm to segment color images based on 5D feature vectors (spatial coordinates + RGB values).

2.  **Dimensionality Reduction**
    -   **Linear Methods**: Implementation of PCA on the Iris dataset and manual computation of Linear Discriminant Analysis (LDA), including within-class and between-class scatter matrices.
    -   **Nonlinear Methods**: Utilizing Kernel PCA with RBF kernels to unfold nonlinear manifolds, such as concentric circles, where standard PCA fails.
    -   **Formal Theory**: Mathematical proofs regarding the maximum number of discriminant directions in LDA and the derivation of the kernel eigenvalue problem in Kernel PCA.

3.  **Feature Selection & Engineering**
    -   **Filter Methods**: Exploratory analysis of real-world data (Heart Disease dataset) using correlation-based filtering and Mutual Information ranking.
    -   **Wrapper Methods**: Implementation of Sequential Forward/Backward Selection and Recursive Feature Elimination (RFE/RFECV) to capture feature interactions.
    -   **Embedded Methods**: Analysis of L1-regularized (Lasso) models for automated feature sparsity and importance ranking.

## Project Report
_A detailed **Report** with mathematical proofs, hierarchical dendrograms, and image segmentation visualizations is available here: [Report.pdf](./Report.pdf)_

## Acknowledgements

Developed under the supervision of **Mohammadreza A. Dehaqani, Babak N. Arabi, and Mostafa Tavassolipour**.  
Special thanks to **Amir Naddaf Fahmideh and Kasra Hajiheidari** for project design and assistance.
