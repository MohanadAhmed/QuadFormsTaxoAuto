Consider the formula:
$$F\left(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma}\right)=|\mathrm{v} \mathbf{\Sigma}|^{-\alpha} \operatorname{etr}\left(-\mathbf{\Delta} \mathbf{\Sigma}^{-1}\right)(2 \pi)^{-p} \int_{\mathcal{C}_p} \frac{\operatorname{etr}\left(\mathrm{\mathbf{Y}}^{-1}\left(\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right)^{-1} \mathbf{D}\right)}{\left|\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right|^\alpha} \prod_{j=1}^p \mathcal{G}_\alpha\left(\mathrm{v} x_j, y_j\right) d \varphi_j$$

Initial simulations/calculations show that the funciton looks nice enough (smooth). Can we utilize this to reduce the number of evaluation points we need? Note that using a step size $h$ with number of steps $N$, we need to evaluate the intgerand above at $N^p$ points. It would be great if we can significantly reduce this to avoid the curse of dimensionality. After all montecarlo can do it?

## Side Question: Where is the maxima?
Call the integrand $f(x,y)$ with $x = \begin{bmatrix} x_1 & x_2 & \ldots & x_p\end{bmatrix}$ and $y = \begin{bmatrix} y_1 & y_2 & \ldots & y_p\end{bmatrix}$. Note that $y_i = re^{j\varphi_i}$. Also note that $\mathbf{Y} = \text{diag}\begin{pmatrix} y_1 & y_2 & \ldots & y_p\end{pmatrix}$

Can we find the gradient of this monstrosity and equate it to zero?

$$ f(x, y) = \frac{\operatorname{etr}\left(\mathrm{\mathbf{Y}}^{-1}\left(\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right)^{-1} \mathbf{D}\right)}{\left|\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right|^\alpha} \prod_{j=1}^p \mathcal{G}_\alpha\left(v x_j, y_j\right) $$

We want to compute $$\nabla_y f(x, y) = \begin{bmatrix} \dfrac{\partial f}{\partial y_1} & \dfrac{\partial f}{\partial y_2} \ldots & \dfrac{\partial f}{\partial y_p} \end{bmatrix}^T$$

Hence we need $$\dfrac{\partial f}{\partial y_i}$$

First we write $f(x, y)$ as $$ f(x, y) = \frac{\operatorname{etr}
    \left(\left( Y + B \right)^{-1} D \right)
}{
    \left|I_p + B Y^{-1}\right|^\alpha
} \prod_{j=1}^p \mathcal{G}_\alpha\left(v x_j, y_j\right)  $$