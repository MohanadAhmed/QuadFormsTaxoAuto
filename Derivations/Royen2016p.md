# Royen 2016 p-variate

## Aim

The aim is to invert the Laplace transform (of the multivariate gamma distribution) $$\hat{f}(\mathbf{T})=\left|\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right|^{-\alpha} \operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\right)$$ where $\mathbf{T}=\operatorname{diag}(t_1,t_2,\ldots,t_p)$ and get the CDF $$F(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma})$$

## Formula 
$$F\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=|\mathrm{v} \mathbf{\Sigma}|^{-\alpha} \operatorname{etr}\left(-\mathbf{\Delta} \mathbf{\Sigma}^{-1}\right)(2 \pi)^{-p} \int_{\mathcal{C}_p} \frac{\operatorname{etr}\left(\mathrm{\mathbf{Y}}^{-1}\left(\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right)^{-1} \mathbf{D}\right)}{\left|\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right|^\alpha} \prod_{j=1}^p \mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$
where the arbitrary scale parameter $\mathrm{v}$ is chosen such that $\|\mathbf{B}\|<1$, with $\mathbf{B}=(\mathrm{v}\mathbf{\Sigma})^{-1}-\mathbf{I}_p$, $\mathbf{D}=\mathrm{v}^{-1}\mathbf{\Sigma}^{-1}\mathbf{\Delta}\mathbf{\Sigma}^{-1}$, $\mathbf{Y}=\operatorname{diag}(y_1,y_2,\ldots,y_p)$ with $y_j=re^{i\phi_j}$, $r$ is arbitrarily chosen so that $r>\|\mathbf{B}\|$.

## Proof Sketch

The uniqueness of the Laplace transform (or similar theorems) provide that if two functions have the same Laplace transform, then they are the same. This is the same as the Levy Uniqueness theorem for characteristic functions. The proof consists of showing that if from the proposed CDF, we obtain a PDF by differentiation and apply the laplace transform then it can be shown to be equivalent to the known laplace transform of the multivariate gamma (chi-square).

There is a function $b(S)$ that Royen obtained somehow. 

- PART A: Starting from the known Laplace transform of MV-$\Gamma$ , $\hat{f}$ manipulate it so that $b(.)$ appears. Argue that $b(.)$ is analytic and expand it in a power series. Show that the expanded series of $\hat{f}$ (with $z_j=(1+\mathrm{v}^{-1}t_j)^{-1}$) is given by: $$\hat{f}(t_1, \ldots, t_p) = \left(\prod_{j=1}z_j^\alpha\right)\sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p)\prod_{j = 1}z_j^{n_j} $$  With $\beta$ being the coefficients of the taylor expansion of $b(.)$

- PART B: Differentiate the proposed CDF to obtain the PDF. Manipulate the PDF so that the function $b(.)$ appears and then expand it.

$$ f_1 = \frac{\partial^p}{\partial x_1 \ldots x_p} F (x_1, \ldots x_p) = \sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p) \prod_{j = 1}^p\mathrm{v}g_{\alpha+n_j}(\mathrm{v}x_j)$$

- Recall that $\mathcal{L}\{vg_\alpha(vx_j)\} = (1 + v^{-1}t_j)^{-\alpha} = z_j^{\alpha}$. Hence we can Laplace transfrom the pdf from PART B into: $$\hat{f}_1(t_1, \ldots, t_p) = \left(\prod_{j=1}z_j^\alpha\right)\sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p)\prod_{j = 1}z_j^{n_j}$$

- Since $\hat{f}_1$ and $\hat{f}$ are the same we argue that their inverse transformed versions $f, f_1$ are equal.

### Part A

1. The laplace transform of the MV-Gamma is: $$\hat{f}(\mathbf{T})=\left|\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right|^{-\alpha} \operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\right)$$

    1. With $\mathbf{Z}=(\mathbf{I}_p+\mathrm{v}^{-1}\mathbf{T})^{-1}$ Show that: $$\mathbf{I}_p+\mathbf{\Sigma T} = \mathrm{v}\mathbf{\Sigma}(\mathbf{B}+\mathbf{Z}^{-1})$$

    2. Show that: $$\left|\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right|=|\mathrm{v}\mathbf{\Sigma}|\; |\mathbf{Z}^{-1}|\;|\mathbf{B}\mathbf{Z}+\mathbf{I}_p|.$$

    3. Rewrite: $$\operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\right)=\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}\right).$$

    4. Hence we obtain that: $$\begin{aligned}\hat{f}(\mathbf{T}) &= &\left|\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right|^{-\alpha} &\operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\right)
    \\ &= &|\mathrm{v}\mathbf{\Sigma}|^{-\alpha}\; |\mathbf{Z}|^\alpha \; |\mathbf{B}\mathbf{Z}+\mathbf{I}_p|^{-\alpha} &\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}\right) \\ & &|\mathbf{Z}|^\alpha & b(\mathbf{Z}) \end{aligned}$$ With $$ b(\mathbf{Z})=|\mathrm{v}\mathbf{\Sigma}|^{-\alpha} \; |\mathbf{B}\mathbf{Z}+\mathbf{I}_p|^{-\alpha}\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(\mathbf{Z}(\mathbf{B}\mathbf{Z}+\mathbf{I}_p)^{-1}\mathbf{D}\right) $$

2. Expand in an infinite series using the analyticity of the function $b(Z)$. Under condition of $\|BZ\|<1$. $$b(Z) = \sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p)\prod_{j = 1}z_j^{n_j} = \sum_{\mathbf{n} \in \mathbb{N}^p}\beta_{\mathbf{n}}\mathbf{z}^\mathbf{n}$$

### Part B
1. The proposed CDF is given by:
$$F\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=|\mathrm{v} \mathbf{\Sigma}|^{-\alpha} \operatorname{etr}\left(-\mathbf{\Delta} \mathbf{\Sigma}^{-1}\right)(2 \pi)^{-p} \int_{\mathcal{C}_p} \frac{\operatorname{etr}\left(\mathrm{\mathbf{Y}}^{-1}\left(\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right)^{-1} \mathbf{D}\right)}{\left|\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right|^\alpha} \prod_{j=1}^p \mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$   
2. Note that the proposed CDF can be rewritten using the function $b(.)$ as $$F\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=(2 \pi)^{-p} \int_{\mathcal{C}_p} b(\mathbf{Y}^{-1}) \prod_{j=1}^p \mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$
2. Differentiate it with repsect to $x_1,\ldots,x_p$ to get the PDF: $$f\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=(2 \pi)^{-p} \int_{\mathcal{C}_p} b(\mathbf{Y}^{-1}) \prod_{j=1}^p \dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$ <span style="color:red"> Needs to be checked: interchange of derivatives and integral </span>
2. Recall that $\mathcal{G}_\alpha(x,y)=\displaystyle\sum_{n=0}^\infty G_{\alpha+n}(x)y^n$, where $G_\alpha$ is the CDF associated to $g_\alpha(x)=\dfrac{1}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-x}$. Then $$\dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right)=\displaystyle\sum_{n_j=0}^\infty \mathrm{v}g_{\alpha}\left(\mathrm{v} x_j\right)  y_j^{n_j}$$
5. We then obtain: $$ \prod_{j=1}^p \dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) = \prod_{j=1}^p  \sum_{n_j=0}^\infty \mathrm{v}g_{\alpha}\left(\mathrm{v} x_j\right)  y_j^{n_j} = \sum_{n_1, \ldots, n_p \geq 0} \prod_{j = 1}^p \mathrm{v}g_{\alpha}\left(\mathrm{v} x_j\right)  y_j^{n_j} $$

6. We expand $b(Y^{-1})$. Under condition of $\|BY^{-1}\|<1 $. THis is satisfied if $\|B\| \|Y^{-1}\| < 1$. This is equivalent to $r > \|B\|$. $$b(Y^{-1}) = \sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p)\prod_{j = 1}y_j^{-n_j} = \sum_{\mathbf{n} \in \mathbb{N}^p}\beta_{\mathbf{n}}\mathbf{y}^\mathbf{-n}$$

7. Using 5 and 6 in 3 we obtain the integrand: 
$$\begin{aligned} &\sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p)\prod_{j = 1}y_j^{-n_j} \sum_{m_1, \ldots, m_p \geq 0} \prod_{k = 1}^p \mathrm{v}g_{\alpha}\left(\mathrm{v} x_k\right)  y_k^{m_k} \\ = 
&\sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p) \sum_{m_1, \ldots, m_p \geq 0} \prod_{j = 1}^p \prod_{k = 1}^p \mathrm{v}g_{\alpha}\left(\mathrm{v} x_k\right)  y_k^{m_k} y_j^{-n_j}   \end{aligned}$$

8. Applying the integration over $\mathcal{C}_p$ to the "non-constant" part we obtain: $$ \int_{\mathcal{C}_p} \prod_{j = 1}^p \prod_{k = 1}^p \mathrm{v}g_{\alpha}\left(\mathrm{v} x_k\right)  y_k^{m_k} y_j^{-n_j} d\varphi_j = \begin{cases} (2\pi)^p \quad \text{ if } \forall j\; m_j = n_j \\0 \quad\text{ otherwise } \end{cases}$$

9. This collapses the "double" sum in step 7 to a "single" sum. Hence the pdf reduces to: $$ f\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right) = \sum_{n_1, \ldots, n_p} \beta(n_1, n_2, \ldots, n_p) \prod_{j = 1}^p\mathrm{v}g_\alpha(\mathrm{v}x_j) $$ 

10. Applying the Lapce transform to the PDF in the last step and noting that $\mathcal{L}\{vg_\alpha(vx_j)\} = (1 + v^{-1}t_j)^{-\alpha} = z_j^{-\alpha}$

<!-- 1. Perform algebraic manipulations on the Laplace transform, introducing the arbitrary parameter $\mathrm{v}$ and defining the matrices $\mathbf{B}$ and $\mathbf{D}$.

2. Express the Laplace transform as $\hat{f}(\mathbf{T})=|\mathbf{Z}|^\alpha b(\mathbf{Z})$, where $b(.)$ is an analytical function whenver defined. 

3. Start from the CDF formula and write the equivalent formula of the PDF deriving wrt $x_1,x_2,\ldots,x_j$.

4. Simplify the PDF.

5. Get its Laplace transform; compare with Laplace transform from thw first step. -->

## Proof 
1. Perform algebraic manipulations on the Laplace transform, introducing the arbitrary parameter $\mathrm{v}$ and defining the matrices $\mathbf{B}$ and $\mathbf{D}$:

    1. The expression $(\mathbf{I}_p+\mathbf{\Sigma T})$ appears twice in the Laplace transform. Write: $$\begin{aligned}\mathbf{I}_p+\mathbf{\Sigma T}&=\mathbf{I}_p+\mathrm{v}\mathbf{\Sigma}\mathrm{v}^{-1}\mathbf{T}\\
    &= \mathrm{v}\mathbf{\Sigma}\left[(\mathrm{v}\mathbf{\Sigma})^{-1}+\mathrm{v}^{-1}\mathbf{T}\right]\\
    &= \mathrm{v}\mathbf{\Sigma}\left[(\mathrm{v}\mathbf{\Sigma})^{-1}-\mathbf{I}_p+\mathbf{I}_p+\mathrm{v}^{-1}\mathbf{T}\right]\\
    &=\mathrm{v}\mathbf{\Sigma}(\mathbf{B}+\mathbf{Z}^{-1}).\end{aligned}$$ where $\mathbf{Z}=(\mathbf{I}_p+\mathrm{v}^{-1}\mathbf{T})^{-1}$, which is obviously diagonal with elements $z_j=(1+\mathrm{v}^{-1}t_j)^{-1}$.

    2. Rewrite the determinant: $$\left|\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right|=|\mathrm{v}\mathbf{\Sigma}|\; |\mathbf{Z}^{-1}|\;|\mathbf{B}\mathbf{Z}+\mathbf{I}_p|.$$

    3. Consider the identity ( we may use the definition of an inverse) $$\mathbf{T}(\mathbf{I}_p+\mathbf{\Sigma T})^{-1}=\mathbf{\Sigma}^{-1}-\mathbf{\Sigma}^{-1}(\mathbf{I}_p+\mathbf{\Sigma T})^{-1}.$$

    4. Rewrite the trace using its linearity and $\operatorname{tr}(\mathbf{AB})=\operatorname{tr}(\mathbf{BA})$: $$\operatorname{tr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\right)=\operatorname{tr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})+\operatorname{tr}\left(\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}\right).$$

    5. Write $\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}=(\mathbf{B}+\mathbf{Z}^{-1})^{-1}(\mathrm{v}\mathbf{\Sigma})^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}=(\mathbf{B}+\mathbf{Z}^{-1})^{-1}\mathbf{D}=\mathbf{Z}(\mathbf{B}\mathbf{Z}+\mathbf{I}_p)^{-1}\mathbf{D}$, where $\mathbf{D}=\mathrm{v}^{-1}\mathbf{\Sigma}^{-1}\mathbf{\Delta}\mathbf{\Sigma}^{-1}$.

    6. Hence the Laplace transform is given by: $$\begin{aligned}\hat{f}(\mathbf{T})&=|\mathrm{v}\mathbf{\Sigma}|^{-\alpha}\; |\mathbf{Z}|^\alpha \; |\mathbf{B}\mathbf{Z}+\mathbf{I}_p|^{-\alpha}\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(-\mathbf{T}\left(\mathbf{I}_p+\mathbf{\Sigma} \mathbf{T}\right)^{-1} \mathbf{\Delta}\mathbf{\Sigma}^{-1}\right)\\
    &=|\mathrm{v}\mathbf{\Sigma}|^{-\alpha}\; |\mathbf{Z}|^\alpha \; |\mathbf{B}\mathbf{Z}+\mathbf{I}_p|^{-\alpha}\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(\mathbf{Z}(\mathbf{B}\mathbf{Z}+\mathbf{I}_p)^{-1}\mathbf{D}\right).
    \end{aligned}$$ 

2. Express the Laplace transform as $\hat{f}(\mathbf{T})=|\mathbf{Z}|^\alpha b(\mathbf{Z})$, where $b(.)$ is an analytical function whenver defined: 

    1. Write $\hat{f}(\mathbf{T})=|\mathbf{Z}|^\alpha b(\mathbf{Z})\left[\prod_{j=1}^pz_j^\alpha\right]b(\mathbf{Z})$, where $$b(\mathbf{Z})=|\mathrm{v}\mathbf{\Sigma}|^{-\alpha} \; |\mathbf{B}\mathbf{Z}+\mathbf{I}_p|^{-\alpha}\operatorname{etr}(-\mathbf{\Delta}\mathbf{\Sigma}^{-1})\operatorname{etr}\left(\mathbf{Z}(\mathbf{B}\mathbf{Z}+\mathbf{I}_p)^{-1}\mathbf{D}\right).$$

    2. Since $b(.)$ is a composition of elementary function with $(\mathbf{I}_p+\mathbf{BZ})^{-1}$, hence it is analytical for $\|\mathbf{BZ}\|<1$, a sufficient condition for is $\|\mathbf{Z}\|<\|\mathbf{B}\|^{-1}$, equivalently $\max z_j<\|\mathbf{B}\|^{-1}$:
    $$\hat{f}(\mathbf{T})=|\mathbf{Z}|^\alpha\sum\beta(n_1,\ldots,n_p)\prod z_j^{n_j}$$

2. Now work on the formula.
    
    1. Note that the proposed CDF can be rewritten using the function $b(.)$ as $$F\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=(2 \pi)^{-p} \int_{\mathcal{C}_p} b(\mathbf{Y}^{-1}) \prod_{j=1}^p \mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$
    2. Derive it with repsect to $x_1,\ldots,x_j$ to get the PDF: $$f\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=(2 \pi)^{-p} \int_{\mathcal{C}_p} b(\mathbf{Y}^{-1}) \prod_{j=1}^p \dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$ <span style="color:red"> Needs to be checked: interchange of derivatives and integral </span>
    2. Recall that $\mathcal{G}_\alpha(x,y)=\displaystyle\sum_{n=0}^\infty G_{\alpha+n}(x)y^n$, where $G_\alpha$ is the CDF associated to $g_\alpha(x)=\dfrac{1}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-x}$. Then $\dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right)=\displaystyle\sum_{n=0}^\infty \mathrm{v}g_{\alpha}\left(\mathrm{v} x_j, y_j\right)$
    3. Then the PDF is given by: $$f\left(\mathbf{x}\right)=(2 \pi)^{-p} \int_{\mathcal{C}_p} b(\mathbf{Y}^{-1}) \prod_{j=1}^p \dfrac{\partial}{\partial x_j}\mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$

 Recall that $(1+\theta t)^{-k}$ is the Laplace transform of the gamma PDF $\dfrac{1}{\Gamma(k)\theta^k}x^{k-1}\mathrm{e}^{-x/\theta}$ (see [Wikipedia](https://en.wikipedia.org/wiki/Gamma_distribution)). Then $\mathrm{v}g_\alpha(\mathrm{v}x_j)=\dfrac{d}{dx_j}G_\alpha(vx_j)$ is the PDF associated to the Laplace transform $z_j^\alpha=(1+v^{-1}t_j)^{-\alpha}$.