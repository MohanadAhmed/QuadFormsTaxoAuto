1. Khammassi (2022) (CDF) $M = N$ : $$Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma),\quad \Sigma \in \mathbb{R}^{N\times N}, \quad i = 1 \ldots M$$

2. Laverny (2021) (PDF) $$Y_i = x^T A_i x,\quad | x \sim \mathcal{N}(0, \Sigma), \quad$$ $$ \exists P | P(\Sigma^{\frac12} A_i \Sigma^{\frac12})P^T = D_i, \forall i\in[1, M], PP^T =I $$ $D_i \succ 0$ is diagonal.

3. Tekinay (2020) (Moments, PDF, CDF) $M = N = 4$ $$\begin{gathered} Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma), \Sigma \in \mathbb{R}^{N\times N}, \quad i = 1 \ldots 4 \\ \text{Correlation Matrix is Toeplitz i.e.  } \dfrac{\mathbb{E}[x_i^*x_j]}{\mathbb{E}[|x_i|^2]\mathbb{E}[|x_j|^2]}=\dfrac{\mathbb{E}[x_{i+k}^*x_{j+k}]}{\mathbb{E}[|x_{i+k}|^2]\mathbb{E}[|x_{j+k}|^2]}\end{gathered}$$

4. Bithas (2019) (PDF, CDF) $M = N$: $$Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(\mu, \Sigma), \quad \Sigma \in \mathbb{R}^{N\times N} \quad i = 1 \ldots M$$ $$\exists v \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T$$ **Condition 3**
*The paper shows rician variables with underlying guassians. that imposes a structure on the mean vector.  Closer inspection reveals this structure can be satsified by any vector ==> NO CONDITION*

5. Wiegand (PDF) (2019) $M = N$: $$ Y_i = x^H E_{ii} x, , \quad x \sim \mathcal{CN}(0, \Sigma), \quad \Sigma \in \mathbb{R}^{N\times N} \quad i = 1 \ldots M $$

6. Wiegand (PDF) (2018) $M = N$: $$\begin{gathered}Y_i = x^H E_{ii} x, , \quad x \sim \mathcal{CN}(0, \Sigma), \quad \Sigma \in \mathbb{R}^{N\times N}, \quad i = 1 \ldots M,\quad \\ \text{Correlation Matrix is Toeplitz i.e.  } \dfrac{\mathbb{E}[x_i^*x_j]}{\mathbb{E}[|x_i|^2]\mathbb{E}[|x_j|^2]}=\dfrac{\mathbb{E}[x_{i+k}^*x_{j+k}]}{\mathbb{E}[|x_{i+k}|^2]\mathbb{E}[|x_{j+k}|^2]}\end{gathered}$$

7. Bealieu 3D (PDF) (2017) $M = N = 3$ : $$Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma), \quad \Sigma \in \mathbb{R}^{N\times N} \quad i = 1 \ldots M$$

    Bealiue 4D (PDF) $M = N = 4$ : $$Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma), \quad \Sigma \in \mathbb{R}^{N\times N} \quad i = 1 \ldots M$$

8. Lassere (2017) (CDF,ProbContent) $$Y_i = g_i(x), \quad x \sim \mathcal{N}(\mu, \Sigma),\quad i = 1 \ldots M \quad g_i(x) \text{ is polynomial in } x$$

9. Royen (2016) (CDF) ($N = K \times M$): $$Y_i = x^T (I_K\otimes E_{ii}) x, \quad x \sim \mathcal{N}(\mu, \Sigma),\quad \Sigma = I_K \otimes \Sigma_M, E_{ii} \in \mathbb{R}^{KM \times KM}$$

10. Bealieu (2011) 2D Rician $M = N = 2$: $$\begin{gathered}Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(\mu, \Sigma),\quad \Sigma \in \mathbb{R}^{2\times 2}, \quad i = 1 \ldots 2\\ \rho = \Sigma_{12}/\sqrt{\Sigma_{22}\Sigma_{11}}, \quad \exists z \in \mathbb{C}, a \in \mathbb{R}\; | \; \mu = z \begin{bmatrix} a \Sigma_{12}/\Sigma_{22} & \rho\Sigma_{12}/(\Sigma_{11}a)\end{bmatrix}^T\end{gathered}$$

11. Bealieu (2011)
    - A: (CDF, PDF) $M = N$ : $$\begin{gathered}Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma), \quad i = 1 \ldots M \\ \quad \Sigma \in \mathbb{R}^{N\times N}, \exists v \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T\end{gathered}$$
    - B: (CDF, PDF) $M = N$ : $$\begin{gathered}Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(\mu, \Sigma), \quad i = 1 \ldots M \\ \quad \Sigma \in \mathbb{R}^{N\times N}, \exists v=[\lambda_1, \lambda_2,\ldots,\lambda_N] \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T\\ 
    \exists z \in \mathbb{C}\;|\; \mu = z\begin{bmatrix}\sqrt{\Sigma_{11}}\lambda_1 & \sqrt{\Sigma_{22}}\lambda_2 & \ldots \sqrt{\Sigma_{MM}}\lambda_M \end{bmatrix}\end{gathered}$$
    - C (CDF, PDF) $N = mM$ : $$\begin{gathered}Y_i = x^H (I_m\otimes E_{ii}) x, \quad x \sim \mathcal{CN}(0, I_m \otimes \Sigma), \quad i = 1 \ldots M \\ \quad \Sigma \in \mathbb{R}^{M\times M}, \exists v=[\lambda_1, \lambda_2,\ldots,\lambda_M] \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T\\ 
    \end{gathered}$$
    - D (CDF, PDF) $N = mM$ : $$\begin{gathered}Y_i = x^H (I_m\otimes E_{ii}) x, \quad x \sim \mathcal{CN}(\mu, I_m \otimes \Sigma), \quad i = 1 \ldots M \\ \quad \Sigma \in \mathbb{R}^{M \times M}, \exists v=[\lambda_1, \lambda_2,\ldots,\lambda_M] \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T\\ 
    \mu = \begin{bmatrix}\mu_1 & \mu_2 \ldots \mu_m \end{bmatrix} \\
    \exists z_k \in \mathbb{C}, k = 1 \ldots m\;|\;  \mu_k = z_k \begin{bmatrix}\sqrt{\Sigma_{11}}\lambda_1 & \sqrt{\Sigma_{22}}\lambda_2 & \ldots \sqrt{\Sigma_{MM}}\lambda_M \end{bmatrix}
    \end{gathered}$$

12. Morales-Jimenez (2011) (CDF) ($N = K \times M$): $$Y_i = x^H (I_K\otimes E_{ii}) x, \quad x \sim \mathcal{CN}(0, I_K \otimes \Sigma_M),\quad E_{ii} \in \mathbb{R}^{M \times M}$$

13. Dharmawansa & McKay (PDF, CDF, CHF) (2009) ($M = 3, N = 3K$): $$\begin{gathered}Y_i = x^H (I_K \otimes E_{ii}) x,\quad x \sim \mathcal{CN}(\mu \otimes \mathbf{1}_3, I_K \otimes \Sigma), \mathbf{1}_3 = [1, 1 ,1]^T \\ (\Sigma^{-1})_{13} = 0 \end{gathered}$$

14. Dharmawansa & Rajatheva & Tellambura (PDF) (2009) ($M = 3, N = 3K$): $$\begin{gathered}Y_i = x^T (I_K \otimes E_{ii}) x,\quad x \sim \mathcal{N}(\mu \otimes \mathbf{1}_3, I_K \otimes \Sigma), \mathbf{1}_3 = [1, 1 ,1]^T \\ (\Sigma^{-1})_{13} = 0 \end{gathered}$$

15. Peppas (2009) (CDF) $M = 3, N = 3K$: $$Y_i = x^H (I_K \otimes E_{ii}) x,\quad x \sim \mathcal{CN}(0, I_K \otimes \Sigma), \quad \Sigma \in \mathbb{R}^{3 \times 3}$$

16. Royen (2007) $N = KM$: $$Y_i = x^T (I_k \otimes E_{ii}) x,\quad x \sim \mathcal{N}(0, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$

19. Royen (2007) $N = KM = \sum_{g = 1}^G K_g$ $$Y_i = x^T A_i x,\quad x \sim \mathcal{N}(\mu, \Sigma) \quad i = 1 \ldots M $$ $$A_i = \text{diag}\begin{pmatrix}A_i^{(1)} & A_i^{(2)} & \ldots & A_i^{(G)}\end{pmatrix}, A_i^{(g)} = I_{K_g} \otimes E_{ii} $$ $$ \Sigma = \text{diag}\begin{pmatrix}\Sigma^{(1)} & \Sigma^{(1)} & \ldots & \Sigma^{(1)}\end{pmatrix} $$

20. Tavares and Tavares (2007) $M = 2, N = 2K$:
$$Y_i = x^T A_i x$$ 

$$(A_1) = \begin{cases} 1 \quad (i = j) \leq K \\ -1 \quad i = j > K\\ 0 \quad \text{otherwise}\end{cases}\quad (A_2)_{ij} = \begin{cases} 1 \quad |i - j| = K\\ 0 \quad \text{otherwise}\end{cases}$$

21. Hagedorn (2006) 
    - $M = 3, N = 3K$: $$Y_i = x^H (I_K \otimes E_{ii}) x,\quad x \sim \mathcal{CN}(0, I_K \otimes \Sigma) $$

    - $M = 2, N = 2K$: $$Y_i = x^H (I_K \otimes E_{ii}) x,\quad x \sim \mathcal{CN}(0, I_K \otimes \Sigma) $$

22. Chen and Tellambura (2005):
    - $M = 3, N = 3$: $$Y_i = x^H (E_{ii}) x,\quad x \sim \mathcal{CN}(0, \Sigma) $$
    $\Sigma$ is allowed to be complex (hermitian of course)
    - $M = 4, N = 4$: $$Y_i = x^H (E_{ii}) x,\quad x \sim \mathcal{CN}(0, \Sigma) $$ $$(\Sigma^{-1})_{14} = 0$$

23. Schone and Schmid (2000): 
    - $M = 2$: $$Y_1 = x^TA x, \; Y_2 = b^Tx, \quad x \sim \mathcal{N}(0, \Sigma),$$  $$P^T\Sigma^{\frac12}A\Sigma^{\frac12}P = \text{diag}$$ $$\text{rank}(A) > 4  \text{ or }\; \left\{\text{rank}(A) > 2  \;\exists j > \text{rank}(A)\; | \; (P^T\Sigma^{\frac12}b)_j \neq 0  \right\}$$

24. Royen (1995):
    - One factorial Non-central: $N = KM$: $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(\mu, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$ $$ \begin{gathered} \exists v \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T \text{ or } \\ \Sigma = D - vv^T\end{gathered} $$
    - One factorial non-central with a condition $N = KM$:
    $$\exists \; u \in \mathbb{R}^{M \times 1}, v ^ {K \times 1}$$
    $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(v \otimes u, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$
    $$ \begin{gathered} \exists v \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T \text{ or } \\ \Sigma = D - vv^T\end{gathered} $$
    - Two factorial central $N = KM$: $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(0, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$
$$ \begin{gathered} \exists V \in \mathbb{C}^{M \times 2}, D = \text{Diag}\; |\; \Sigma = D + VV^T\end{gathered} $$

25. Royen (1994): $N = KM$: $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(0, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$
$\Sigma$ or $\Sigma^{-1}$ must represent a tree

26. Royen (1991) - Multivariate Chi-Square: $N = KM$: $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(0, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$

27. Royen (1991) - One Factorial Gamma: $N = KM$: $$Y_i = x^T (I_k \otimes \Sigma) x,\quad x \sim \mathcal{N}(0, I_K \otimes \Sigma), \Sigma \in \mathbb{R}^{M \times M}$$
$$ \begin{gathered} \exists v \in \mathbb{R}^{M \times 1}, D = \text{Diag}\; |\; \Sigma = D + vv^T \text{ or } \\ \Sigma = D - vv^T\end{gathered} $$

Need some revision
