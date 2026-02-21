# Spoken Language Identification (SLID)

_Machine Learning — University of Tehran_

This final project implements a comprehensive **Spoken Language Identification (SLID)** system, transitioning from raw data collection to advanced supervised and unsupervised modeling. The project demonstrates a complete machine learning workflow: building a multilingual speech corpus, engineering acoustic features, and evaluating both classification and clustering paradigms to distinguish between German, Italian, Korean, and Spanish.

## Project Phases

### Phase 1: Data Acquisition & Theoretical Foundation
The initial phase focuses on the challenges of speech data engineering and the theoretical mechanics of audio signals.
* **Dataset Construction**: Collaborative collection of raw audio from audiobook and podcast sources.
* **Manual Processing**: Extracting ~1-minute clips adhering to sentence boundaries to preserve natural prosody.
* **Theoretical Analysis**: In-depth study of feature extraction techniques such as MFCCs, Log-Mel Spectrograms, and Linear Predictive Coding (LPC).
* **Metric Learning**: Exploration of similarity learning using Contrastive and Triplet loss functions for language embedding.

### Phase 2: Implementation & Pattern Recognition
The second phase involves the practical application of machine learning algorithms to the refined dataset of 712 audio clips.

1.  **Audio Standardization & Cleaning**
    * Resampling to **16 kHz**, mono conversion, and energy-based **silence trimming**.
    * Amplitude normalization to ensure consistent input across different recording conditions.

2.  **Feature Engineering**
    * Extraction of 56 total features including **13 MFCCs**, **Chroma features**, **Spectral Centroid**, and **Zero-Crossing Rate (ZCR)**.
    * Application of temporal statistics (mean and standard deviation) to generate fixed-length feature vectors.

3.  **Supervised Classification**
    * Dimensionality reduction using **Linear Discriminant Analysis (LDA)** to maximize class separability.
    * Evaluation of five models: **SVM (RBF)**, **MLP (Neural Network)**, **Random Forest**, **Decision Tree**, and **Gaussian Naive Bayes**.
    * Achieved near-perfect classification performance using **GridSearchCV** for hyperparameter optimization.

4.  **Unsupervised Clustering**
    * Identification of natural groupings using **K-Means** (verified by the **Elbow Method**) and **DBSCAN**.
    * **K-Means** achieved perfect cluster purity (1.0), while **DBSCAN** successfully identified core language groups while filtering outliers as noise.
    * Visualization of high-dimensional feature spaces using **t-SNE** and **PCA**.


## Acknowledgements
 project design team: **Mostafa Kermani Nia, Faezeh Mozaffari, and Mahan Osouli**.
