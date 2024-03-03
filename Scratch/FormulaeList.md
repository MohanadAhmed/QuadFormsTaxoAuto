# Khammassi 2023
## Original Formulation
$$x \sim \mathcal{CN}(0, \Sigma), \quad \Sigma \in \mathbb{R}^{n\times n}$$
$$ g_i = |x_i| $$

### Formula

### Code

### Pseudocode

### Typical M & N

## Standardized Formulation
### Form
$$Y_i = x^H E_{ii} x, \quad x \sim \mathcal{CN}(0, \Sigma),\quad \Sigma \in \mathbb{R}^{N\times N}, \quad i = 1 \ldots M$$

### Formula
$$
\begin{aligned}
    &F_{\hat{Y}_1,\ldots,\hat{Y}_N}(\hat{y}_1,\ldots,\hat{y}_N)\\ = &\int_{-\infty}^\infty\ldots\int_{-\infty}^\infty G(a,b,\epsilon\text{-rank})\nonumber
    \prod_{k=1}^N\left(1-Q_1\left(\dfrac{\sqrt{\tilde{a}^2 + \tilde{b}^2}}{\tilde{\sigma}(\epsilon\text{-rank})},\dfrac{\sqrt{2\hat{y}_k}}{{\sigma}(\epsilon\text{-rank})}\right)\right)
    da_1\ldots da_{{\epsilon\text{-rank}}}db_1\ldots db_{{\epsilon\text{-rank}}} \\
    &\tilde{\sigma}(r) = \sqrt{\sigma^2 - \sum_{l = 1}^r \lambda_l u_{k, l}^2} \quad
    \tilde{a} = 2\left(\displaystyle\sum_{\ell=1}^{\epsilon\text{-rank}}\sqrt{\lambda_\ell u_{k,\ell}a_\ell}\right) \quad 
    \tilde{b} = 2\left(\displaystyle\sum_{\ell=1}^{\epsilon\text{-rank}}\sqrt{\lambda_\ell u_{k,\ell}b_\ell}\right) \\
    &G(a,b,\epsilon\text{-rank}) = \left[\prod_{\ell=1}^{\epsilon\text{-rank}}\dfrac{1}{\pi}\exp(-(a_\ell^2+b_\ell^2))\right]
\end{aligned} 
$$

