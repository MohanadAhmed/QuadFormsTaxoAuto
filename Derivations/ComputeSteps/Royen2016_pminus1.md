# Inputs:
1. $\alpha$: Half the degrees of freedom. 

2. $\mathbf{\Delta}$: Non-centrality parameter ($\times 2$)

3. $\mathbf{\Sigma}$: Covariance matrix of the indepenently sampled vectors ($\times 2$)

# Output:
The CDF of the Multivariate gamma distribution at point $(x_1, x_2, \ldots, x_p)$: $$F_{X_1, X_2, \ldots, X_p}(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma})$$

# Steps:

1. Choose the arbitrary scale matrix $\mathbf{W}=\operatorname{diag}(w_1,w_2,\ldots,w_p)$ so that $\|\mathbf{B}(\mathbf{W})\|\geq 1$, where $\mathbf{B}(\mathbf{W}):=(\mathbf{W\Sigma W})^{-1}-\mathbf{I}$, I suggest:

    1. Start with $\mathbf{B}(\mathbf{W})=\mathbf{B}(\mathbf{I})=\mathbf{\Sigma}^{-1}-\mathbf{I}$.
    2. While $\|\mathbf{B}(\mathbf{W})\|< 1$:
        1. Multiply $\mathbf{W}=0.9\mathbf{W}$.
        2. Calculate $\mathbf{B}(\mathbf{W})=(\mathbf{W\Sigma W})^{-1}-\mathbf{I}$.

2. Choose an arbitrary positive parameter $r$ so that $r>\|\mathbf{B}\|$.

3. Compute $\mathbf{D}(\mathbf{W})=\mathbf{W}^{-1}\mathbf{\Sigma}^{-1}\mathbf{\Delta}\mathbf{\Sigma}^{-1}\mathbf{W}^{-1}$.

4. Partition $$\mathbf{B}(\mathbf{W})=\begin{bmatrix}
\mathbf{B}_{pp} & \mathbf{b}_p\\
\mathbf{b}_p^T & b_{pp}
\end{bmatrix} \text{and } \mathbf{D}(\mathbf{W})=\begin{bmatrix}
\mathbf{D}_{pp} & \mathbf{d}_p\\
\mathbf{d}^p & d_{pp}
\end{bmatrix}$$

5. Set $F=0$.

5. Choose the number of steps $z$.

6. Numerical integration loop: For $(\phi_1,\phi_2,\ldots,\phi_{p-1}):=[-\pi+\dfrac{2\pi}{z}:\dfrac{2\pi}{z}:\pi]^{p-1}$:

    1. For $i=1 : p-1$
        - Evaluate $y_i=r\mathrm{e}^{j\phi_i}$
        - Evaluate $G_i=\mathcal{G}_\alpha\left(w_i^2x_i, y_i\right)$ (using the frequently used functions).


    2. Calculate $G=\prod_{i=1}^{p-1}G_i$.

    3. Write $\mathbf{Y}_{pp}=\operatorname{diag}(y_1,\ldots,y_{p-1})$

    4. Calculate $$y_0=y_0\left(y_1, \ldots, y_{p-1}\right)=\mathbf{b}_p^{T}\left(\mathbf{Y}_{p p}+\mathbf{B}_{p p}\right)^{-1} \mathbf{b}_p-b_{p p}$$

    5. Calculate $$q=q\left(y_1, \ldots, y_{p-1}\right)=\left[\mathbf{b}_p^{T}\left(\mathbf{Y}_{p p}+\mathbf{B}_{p p}\right)^{-1},-1\right] \mathbf{D}\left[\begin{array}{c}\left(\mathbf{Y}_{p p}+\mathbf{B}_{p p}\right)^{-1} \mathbf{b}_p \\-1\end{array}\right]$$

    6. Calculate $G_{\text{outer}}=G^{*}_\alpha\left(w_p^2 x_p(1-y_0), \dfrac{q}{1-y_0}\right)$ (using the frequently used functions).
 
    7. Calculate $$L_\alpha\left(y_1, \ldots, y_{p-1}\right)=\operatorname{etr}\left(\left(\mathbf{Y}_{p p}+\mathbf{B}_{p p}\right)^{-1} \mathbf{D}_{p p}\right)\left|\mathbf{I}+\mathbf{B}_{p p} \mathbf{Y}_{p p}^{-1}\right|^{-\alpha}$$ 

    8. Add: $F+=G_{outer}L_\alpha\left(y_1, \ldots, y_{p-1}\right) G$.

7. Multiply: $F*=|v\mathbf{\Sigma}|^{-\alpha} \operatorname{etr}\left(-\mathbf{\Delta} \mathbf{\Sigma}^{-1}\right)(2 \pi)^{-(p-1)}$.

8. Finally: $F=F*\text{hypervolume of subdivision}$

## Frequently Used Functions




1. $\mathcal{G}_\alpha(x, y)=\left\{\begin{array}{lll}
\dfrac{1}{1-y}\left(G_\alpha(x)-y^{1-\alpha} e^{(y-1) x} G_\alpha(x y)\right), & y \neq 1, & \alpha>0 \\
x g_\alpha(x)+(1+x-\alpha) G_\alpha(x), & y=1 &
\end{array}\right.$

2. $g_\alpha(x)=\dfrac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}$

3. $G_\alpha(x)=\int_0^xg_\alpha(t)dt=\dfrac{\gamma(\alpha,x)}{\Gamma(\alpha)}=\begin{cases}
    1-e^{-x}\sum_{j=0}^{\alpha-1}\dfrac{x^j}{j!}&2\alpha \text{ is even}\\
    \operatorname{erf}(x^{1/2})-e^{-x}\sum_{j=1}^{\alpha-1/2}\dfrac{x^{j-1/2}}{\Gamma(j+\frac{1}{2})}&2\alpha \text{ is odd}
\end{cases}$

4. $G_\alpha(x, y)=e^{-y} \sum_{n=0}^{\infty} G_{\alpha+n}(x) \dfrac{y^n}{n !}$