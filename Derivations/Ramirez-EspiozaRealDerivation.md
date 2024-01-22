# Ramirez-Espinoza Real

# Quadratic Form
This method works for positive definite forms, i.e., linear ccombinations of independent non-central chhi-squares with positive coefficients: $$Y\sim \sum_{i=1}^N\lambda_i\chi_1^2(h_i^2)$$

# Sequence of Gamma Variates
The sequence of randm variables $\xi_m$, $m \in \mathbb{N}$ is given by their pdfs $$f_{\xi_m}(u)=\dfrac{(m-1)^m}{\Gamma(m)}u^{m-1}e^{-(m-1)u}\quad u>0$$ which corresponds to a $\Gamma(\alpha,\beta)$, for shape parameter $\alpha=m$ and rate parameter $\beta=(m-1)$. 

**Claim:** The sequence $\xi_m$ converges in diistribution to $1$. 
**Proof:** The MGF is given by [Wikipedia](https://en.wikipedia.org/wiki/Gamma_distribution) $$M_{\xi_m}(s)=\left(1-\dfrac{s}{m-1}\right)^{-m},\quad \Re(s)<m-1$$ which converges to $e^s$ as $m$ tends to infinity. The latter MGF is that of the constant random variable $1$, hence, due to the uniqueness of the MGF (with tech conditions), the sequence $\xi_m$ converges in MGF, hence in distribution, to $1$. 

# Approximative Quadratic Form

The sequence of approximative random variables is given by: 
$$Y_m=\dfrac{Y}{\xi_m}$$

# CDF of the Approximative Random Variable

1. The CDF of the gamma variate $\xi_m$ can be written as [Wikipedia](https://en.wikipedia.org/wiki/Gamma_distribution) $$F_{\xi_m}(u)=1-\sum_{k=1}^{m-1}\dfrac{(m-1)^k}{k!}u^ke^{-(m-1)u}$$

2. Ratio Formula: 

    a. $$\begin{aligned}F_{Y_m}(r)&=\mathbb{P}\left(\dfrac{Y}{\xi_m}\leq r\right)\\
&=\int\int_{\frac{y}{u}\leq r}f_Y(y)f_{\xi_m}(u)dydu\\
&=\int_0^\infty f_{\xi_m}(u)\int_{0}^{ru}f_Y(y)dydu\\
&=\int_0^\infty f_{\xi_m}(u)F_Y(ru)du\\
\end{aligned}$$
    b. Note that we have utilised the fact that both RVs are positive. Changing variables, $t=ru$, we get: $$F_{Y_m}(r)=\int_0^\infty F_Y(t)\dfrac{1}{y}f_{\xi_m}\left(\dfrac{t}{x}\right)dt$$
    c.Integrating by parts, for $U=F_Y(t)$ and $dV=\dfrac{1}{y}f_{\xi_m}\left(\dfrac{t}{x}\right)dt$, we get $$F_{Y_m}(y)=1-\int_0^\infty f_Y(t)F_{\xi_m}\left(\dfrac{t}{y}\right)dt$$

3. Substituting 1. in 2. we get: $$F_{Y_m}(y)=\sum_{k=0}^{m-1}\dfrac{(m-1)^k}{k!y^k}\mathbb{E}\left[Y^ke^{-(m-1)Y/y}\right]$$

4. MGF: Knowing that $\dfrac{d^k}{ds^k}\mathbb{E}[e^{sY}]=\mathbb{E}[Y^ke^{sY}]$, and subsituting at $s=-\dfrac{m-1}{y}$, we get: $$F_{Y_m}(y)=\sum_{k=0}^{m-1}\dfrac{(m-1)^k}{k!y^k}M_Y^{(k)}\left(-\dfrac{m-1}{y}\right)$$

5. Calculation of $k$-th derivative of the MGF: 
It is given by: $$\frac{d^k}{d s^k} M_Q(s)=M_Q(s) D_k(s)$$
where $$\begin{aligned}
D_k(s) & =\sum_{j=0}^{k-1}\left(\begin{array}{c}
k-1 \\
j
\end{array}\right) g_{k-1-j}(s) D_j(s), \\
g_i(s) & =2^i i ! \sum_{t=1}^n \frac{\lambda_t^{i+1}\left[(i+1) b_t^2+1-2 \lambda_t s\right]}{\left(1-2 \lambda_t s\right)^{i+2}}
\end{aligned}$$ 