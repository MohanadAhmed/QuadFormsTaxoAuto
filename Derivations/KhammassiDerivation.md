# Khammassi's Derivation

**Problem Formulation:** Consider the random vector $\mathbf{g}=[g_1,\ldots,g_N]^H\sim\mathcal{CN}(\mathbf{0},\bm{\Sigma})$. The sought distribution is that of $[|g_1|,\ldots,|g_N|]$, which is correlated Rayleigh. Without loss of generality, we suppose that all the variances are equal: $\forall i \in \{1,\ldots, N\},\;\Sigma_{ii}=\sigma_{ii}^2=\sigma^2$.

**Major Steps:** 

1. Approximate $\mathbf{g}$ by $\mathbf{\hat{g}}=\mathbf{\hat{g}}(\epsilon)$ which converges in distribution to $\mathbf{g}$ as $\epsilon$ tends to zero. 
2. Calculate the CDF of $\mathbf{\hat{g}}$; this is the approximate CDF of $\mathbf{g}$.

# Approximation of $\mathbf{g}$

1. <u>Express $\mathbf{g}$ in terms of standard complex normal vector: </u>
SInce $\mathbf{g}\sim\mathcal{CN}(\mathbf{0},\bm{\Sigma})$, it is equal in distribution to $\bm{\Sigma}^{1/2}\mathbf{h}$ where $\mathbf{h}\sim\mathcal{CN}(\mathbf{0},\mathbf{I}_N)$.
2. Unitarily eigendecompose the covariance matrix: $\bm{\Sigma}=\mathbf{UD}\mathbf{U}^H$, $\mathbf{U}\mathbf{U}^H=\mathbf{I}_N$. Hence $\mathbf{g}=\mathbf{U}\mathbf{D}^{1/2}\mathbf{U}^H\mathbf{h}$. Now, since $\mathbf{U}^H$ is unitary, $\mathbf{U}^H\mathbf{h}$ is a standard complex normal randm vector. Let its $k$-th component be $a_k+jb_k$, where $a_k$ and $b_k$ are i.i.d. $\mathcal{N}(0,\frac12)$. Let $\mathbf{U}=[\mathbf{u}_1,\ldots,\mathbf{u}_N]$, where each eigenvector is written as $\mathbf{u_k}=[u_{1,k},\ldots,u_{N,k}]^H$. Let $\mathbf{D}=\texttt{diag}(s_1,\ldots,s_N)$. Assume $s_1\geq s_2\geq \ldots \geq s_N$. Then the $k$-th component of $\mathbf{g}$ can be written as $$g_k=\sum_{\ell=1}^N u_{k,\ell}\sqrt{s_\ell}(a_\ell+jb_\ell)$$
2. <u> Express the variance in terms of eigenvalues and eigenvectors: </u>
Reconsider the equality $\bm{\Sigma}=\mathbf{UD}\mathbf{U}^H$, and equate the $(k,k)$ entries of both sides: $$\begin{aligned}
\sigma^2=\sum_{\ell=1}^N\sum_{m=1}^N u_{k,\ell}d_{\ell,m}u_{k,\ell}
=\sum_{\ell=1}^N s_\ell u_{k,\ell}^2
\end{aligned}$$
3. <u> Define the approximative vector $\mathbf{\hat{g}}$: </u> The $k$-th componnet is given by: $$\hat{g}_k=\sqrt{\sigma^2-\sum_{\ell=1}^{\epsilon-\texttt{rank}}s_\ell u_{k,\ell}^2}(x_k+jy_k)+\sum_{\ell=1}^{\epsilon-\texttt{rank}} u_{k,\ell}\sqrt{s_\ell}(a_\ell+jb_\ell)$$ where $\epsilon-\texttt{rank}=\#\{s_i:s_i>\epsilon\}=\max_{s_i>\epsilon}i$, and $x_k,y_k,a_k,b_k$ are i.i.d. $\mathcal{N}(0,1)$. Actuallly, this is a lower rank approximation, in which we used $\epsilon-\texttt{rank}+1$ complex variabes intead of $N$ ones.
4. <u> Prove that $\mathbf{\hat{g}}$ converges in distribution to $\mathbf{g}$: </u> Firstly, it's clear that $\epsilon-\texttt{rank}=N$ for $\epsilon < s_N$. So, using 2. and 1., $\hat{g}_k$ converges to $g_k$ in distribution as $\epsilon$ tends to zero. 

# Calculation of the CDF

1. <u> Conition over $\mathbf{a},\mathbf{b}$ and compute the CDF: </u>
Fixing $\mathbf{a},\mathbf{b}$, the components of $\hat{g}$ are independent, since $(x_k,y_k)$ are independent. So each component is a non-central complex normal variable, whose modulus is thus a Rician variable. In particular, the mean of $\hat{g}_k$ is $\sum_{\ell=1}^{\epsilon-\texttt{rank}} u_{k,\ell}\sqrt{s_\ell}(a_\ell+jb_\ell)$ and its  variance is $\sigma^2-\sum_{\ell=1}^{\epsilon-\texttt{rank}}s_\ell u_{k,\ell}^2$. Recall that the CDF of a Rician variable, which is the modulus of $\mathcal{CN}(\mu,\sigma^2)$ is given by $F(x)=1-Q\left(\frac{\mu}{\sigma/\sqrt{2}},\frac{x}{\sigma/\sqrt{2}}\right)$. Hence the CDF of $|\hat{g}_k|$, conditioned on $\mathbf{a},\mathbf{b}$, is given by $$F_{|\hat{g}_k|}(r_k)=1-Q\left(\frac{\sqrt{2}\sum_{\ell=1}^{\epsilon-\texttt{rank}} u_{k,\ell}\sqrt{s_\ell}(a_\ell+jb_\ell)}{\sqrt{\sigma^2-\sum_{\ell=1}^{\epsilon-\texttt{rank}}s_\ell u_{k,\ell}^2}},\frac{\sqrt{2}r_k}{\sqrt{\sigma^2-\sum_{\ell=1}^{\epsilon-\texttt{rank}}s_\ell u_{k,\ell}^2}}\right)$$
2. <u> Integrate ove the distribution of $\mathbf{a},\mathbf{b}$: </u> Use the formula $$F_X(x)=\int F_{X|Y}(x)f_Y(y)dy$$ Now $(a_k+jb_k)$ are i.i.d. $\mathcal{CN}(0,1)$, so their joint pdf is given by $$f(a_1,\ldots,a_{\epsilon-\texttt{rank}},b_1,\ldots,b_{\epsilon-\texttt{rank}})=\frac{1}{\pi^{\epsilon-\texttt{rank}}}\exp\left(\sum_{\ell=1}^{\epsilon-\texttt{rank}}(a_\ell^2+b_\ell^2)\right)$$ 
Integrating over $\mathbf{a},\mathbf{b}$, we get $$\begin{aligned}
& F_{\left|\hat{g}_1\right|,\left|\hat{g}_2\right|, \ldots,\left|\hat{g}_N\right|}\left(r_1, r_2, \ldots, r_N\right) \\
& =\int \cdots \int \prod_{l=1}^{\epsilon-\text { rank }} \frac{1}{\pi} \exp \left(-\left(a_l^2+b_l^2\right)\right) \\
& \prod_{k=1}^N\left(1-Q_1\left(\frac{\sqrt{2\left(\sum_{l=1}^{\epsilon-\text { rank }} \sqrt{s_l} u_{k, l} a_l\right)^2+2\left(\sum_{l=1}^{\epsilon-\text { rank }} \sqrt{s_l} u_{k, l} b_l\right)^2}}{\sqrt{\sigma^2-\sum_{l=1}^{\epsilon-\text { rank }} s_l u_{k, l}^2}}, \frac{\sqrt{2} r_k}{\sqrt{\sigma^2-\sum_{l=1}^{\epsilon-\text { rank }} s_l u_{k, l}^2}}\right)\right) \\
& d a_1 \ldots d a_{\epsilon-\text { rank }} d b_1 \ldots d b_{\epsilon-\text { rank }} .
\end{aligned}$$