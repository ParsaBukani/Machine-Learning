
# Optimization Techniques in Machine Learning

_Machine Learning — University of Tehran_

This project covers a comprehensive exploration of fundamental and advanced optimization techniques essential for machine learning. It spans from first-order methods like Gradient Descent to second-order methods like Newton's algorithm, while also addressing constrained optimization, multi-objective Pareto frontiers, and heuristic approaches such as Genetic Algorithms.

## Tasks

1.  **First-Order Optimization & Line Search**
    -   Analysis of **Line-Search** algorithms, focusing on the roles of search direction ($p_k$) and step length ($\alpha_k$).
    -   Implementation and proof of the **Steepest Descent** direction using first-order Taylor approximations.
    -   Comparison of **Batch Gradient Descent (BGD)** and **Stochastic Gradient Descent (SGD)** regarding computational load, gradient noise, and stability.
    -   Evaluation of step-size strategies including **Fixed Step**, **Backtracking (Armijo Rule)**, and adaptive methods like **AdaGrad**.

2.  **Second-Order & Quasi-Newton Methods**
    -   Implementation of **Newton's Method** for quadratic convergence, utilizing Hessian information for local curvature.
    -   Theoretical study of **Quasi-Newton** methods (BFGS/DFP) and the **Secant Equation** to approximate the Hessian without explicit second derivatives.
    -   Experimental comparison of GD vs. Newton’s Method on the non-convex **Rosenbrock function**.

3.  **Constrained & Multi-Objective Optimization**
    -   **Support Vector Machines (SVM)**: Derivation of Primal, Lagrangian Dual, and KKT conditions for hard and soft-margin classifiers, including **Kernelization**.
    -   **Bilevel Optimization**: Solving leader-follower problems through analytical reduction and substitution.
    -   **Multi-Objective Optimization**: Deriving the **Pareto Front** using weighted-sum scalarization and $\epsilon$-constraint methods.
    -   **Equality Constraints**: Solving non-linear systems via **Lagrange Multipliers** and the **Newton-Raphson** method.

4.  **Heuristic Search (Genetic Algorithm)**
    -   Development of a **Jigsaw Puzzle Solver** using a Genetic Algorithm.
    -   Design of edge-compatibility **Fit Scores**, tournament selection, and a custom **kernel-based crossover** to preserve 2D spatial structures.

## Project Report
_A detailed **Report** with mathematical proofs, convergence plots, and algorithm analysis is available here: [Report.pdf](./Report.pdf)_

## Acknowledgements

Developed under the supervision of **Babak N. Arabi, Mohammadreza A. Dehaqani, and Mostafa Tavassolipour**.  
Special thanks to **Parsa Daghig and Samar Nikfarjad** for project design and assistance.
