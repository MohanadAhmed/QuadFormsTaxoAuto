# Gardini's Derivation
The quadratic form is given by: $$Q(x) = \sum_{i = 1}^r \lambda_i (x_i + \tilde{\eta}_i)^2 \sim \sum_{i = 1}^r \lambda_i \chi_1^2(\eta_i), \quad \eta_i = \tilde{\eta_i}^2$$
We start from a chi-squared expansion of the PDF/CDF. $$f_Q(q)  = \sum_{k = 0}^{\infty} a_k f_G(q; \alpha + k, 2\beta), \quad \alpha = r/2,\quad \beta = \min_{i \in [1, r]} \lambda_i = \lambda_r$$

1. We compute the Mellin Transform $\hat{f}_Q(z)$ (def) of $f_Q(q)$. $$\hat{f}_Q(z) = \int_{0}^{\infty} x^{z - 1} f_Q(x) dx = \int_{0}^{\infty} x^{z - 1}  \sum_{k = 0}^{\infty} a_k f_G(q; \alpha + k, 2\beta) dx $$

    1. Use Lebesgue Monotone Convergence Theorem (for.) to interchange integral (from Mellin) and summation. (Requires: measurability and non-negativity of $x^{z - 1}f_G(q; \ldots)$ $$\hat{f}_Q(z) =  \sum_{k = 0}^{\infty} a_k \int_{0}^{\infty} x^{z - 1}f_G(q; \alpha + k, 2\beta) dx $$

    2. The mellin transform of gamma density function is given by (for.). That is substituted and manipulations to get the $\hat{f_Q}$. $$\hat{f}_Q(z) =  \sum_{k = 0}^{\infty} a_k \hat{f}_G(z; \alpha + k, 2\beta)  = (2\beta)^{z-1}\sum_{k = 0}^{\infty} a_k \frac{\Gamma(z + \alpha + k - 1)}{\Gamma(\alpha + k)}, \quad \Re{(z)} > 1 - \alpha$$


<!-- 2. Gardini normalizes the eigenvalues by the minimal positive eigenvalue. <span style="color:red"> Needs a bit more careful manipulation!!</span> -->

2. We wish to numerically invert the Mellin Transform. The Inverse of the Mellin Transform is given by (for.). $$ f_Q(q) = \int_{h - i\infty}^{h + i\infty} q^{-z}\hat{f}_Q(z) dz  = \int_{h - i\infty}^{h + i\infty} q^{-z}  \sum_{k = 0}^{\infty} a_k \hat{f}_G(z; \alpha + k, 2\beta)dz$$

    1. The path of integral (a vertical line on the complex plane at h) used must be in region of analyticity (Mellin def./Inv Mellin for.). This equivalent to choose $$h \in (1 - \alpha, +\infty)$$

    2. We make a change of variables to convert the complex path integral into an integral (of a complex function) over the real line. $z = h + iy$ <span style="color:red"> Can we make it real before discretization?</span> $$ f_Q(q) = \int_{-\infty}^{+\infty} q^{-(h + iy)}  \sum_{k = 0}^{\infty} a_k \hat{f}_G(h + iy; \alpha + k, 2\beta) idy$$

    4. We truncate the series of $\hat{f_Q}$ up to $K$ and add an error term accounting for the terms from $K+1$ up to $+\infty$ (inside the integral sign). Call the error term $e_M$. The truncation error is calculated by: $$e_M =  \int_{-\infty}^{+\infty} q^{-(h + iy)}  \sum_{k = K + 1}^{\infty} a_k \hat{f}_G(h + iy; \alpha + k, 2\beta) idy $$

        1.  The function above is the Mellin transform a function similar to $f_Q(q)$ but starting at $K+1$. We assume the uniqueness of the Mellin transform pair. Thus: $$ e_M =  \sum_{k = K + 1}^{\infty} a_k {f}_G(q; \alpha + k, 2\beta) $$
        
        2. We first bound the absolute the value of the error. $$\begin{aligned} |e_M| &= \left| \sum_{k = K + 1}^{\infty} a_k {f}_G(q; \alpha + k, 2\beta) \right| = \sum_{k = K + 1}^{\infty} a_k {f}_G(q; \alpha + k, 2\beta) 
        \end{aligned} $$

        3. We replace the density function $f_G(q;\alpha + k, 2\beta)$ by its maximum at  the mode $q = 2(\alpha + k - 1)$. That is we claim that: $$ \begin{aligned} f_G(q; \alpha + k, 2) &\leq  f_G(2(\alpha + k - 1); \alpha + k, 2) \\ &= 
        \frac{ (\alpha + k - 1)^{\alpha + k - 1} e^{-(\alpha +k - 1)}}{ 2 \Gamma{(\alpha + k)} } \end{aligned} $$

        4. The last function is a decreasing function of $k$. See note 10 below. Thus we can replace $k$ by the even by $K$. $$ |e_M| \leq f_G(2(\alpha + K - 1); \alpha + K, 2) \sum_{k = K + 1}^{\infty} a_k  = f_G(2(\alpha + K - 1); \alpha + K, 2) \Bigg(1 -  \sum_{k = 0}^{K} a_k\Bigg)  $$

        3. For the case of the CDF bounding was given by Ruben.

    3. We trunctate the integral over $[-\infty, \infty]$ to $[-T\Delta, T\Delta]$ and add an error term accounting for the integral over $[-\infty, -T\Delta] \cup [T\Delta, \infty]$. Call the error $e_T$. It is given by: $$ e_T = \frac{1}{\pi} \int_{T\Delta}^{\infty}  + \int_{-\infty}^{-T\Delta} $$

        1. The absolute value of the error is bound by the sum of the absolutes.

        2. The functions are conjugates (for. 5). Thus the moduli are equal. They can be summed and the factor of half cancelled (after keeping the positive interval only).

        3. Gardini assumes quadratic decay of $\hat{f}_Q$ with a particular coefficient $M$. The value of $M$ is given by another conjecture.

        4. Replacing the function by its quadratic bound and integrating we obtain an $\arctan$ represenation as an error. $$|e_T| \leq \frac{|\hat{f}_Q(h + iT\Delta)| \times (h^2 + (T\Delta)^2)}{\pi h q^h} \times\left(\frac{\pi}{2} - \arctan{\frac{T\Delta}{h}}\right)$$

    5. We discretize the integral and (underhandedly) let the reader figure out the truncation error!!! It seems this is not going to be nice to obtain.

    


# References Definitons and Formulae

1. Mellin Transform

2. Lebesgue Monotone Convergence Theorem 

3. Mellin Transform of Gamma Density Function

4. Inverse Mellin Transfrom.

5. Symmetry of improper integral tail bounds: 
Denote by $C(z)$ the conjugate of \(z\). Clearly $C(q^{iy})=C(e^{iy\ln(q)})=q^{-iy}$. Now consider the bound on each side:
$$\begin{aligned}\left|\int_{T\Delta}^\infty q^{-(h+iy)}\hat{f}_Q(h+iy)dy\right| & \leq\int_{T\Delta}^\infty \left|q^{-(h+iy)}\hat{f}_Q(h+iy)\right|dy\\
&=\int_{T\Delta}^\infty q^{-h}\left|\hat{f}_Q(h+iy)\right|dy\\
\end{aligned}$$

Similarly $$\begin{aligned}\left|\int_{-\infty}^{-T\Delta} q^{-(h+iy)}\hat{f}_Q(h+iy)dy\right|&=\left|\int_{T\Delta}^\infty q^{-(h-iy)}\hat{f}_Q(h-iy)dy\right|\\
&\leq\int_{T\Delta}^\infty q^{-h}\left|\hat{f}_Q(h-iy)\right|dy\end{aligned}$$
Now $$\begin{aligned}C(\hat{f}_Q(h+iy))&=C\left(\int_0^\infty x^{q+iy-1}f_Q(x)dx\right)\\
&=\int_0^\infty C\left(x^{q+iy-1}\right)f_Q(x)dx\\
&=\int_0^\infty x^{q-iy-1}f_Q(x)dx=\hat{f}_Q(h-iy)\end{aligned}$$
Hence their moduli are equal and the bounds of both tail are equal.
 
6. **Conjecture**: the Mellin transform of the Quadratic form density is monotonically decaying with quadratic rate and a constant $M$.

7. **Conjecture**: The decay constant $M$ is conjectured to be given by: $$M = |\hat{f}_Q(h + iT\Delta) \times (h + iT\Delta)^2|$$

8. $f_G$ the gamma density function. (Also related to the chi square density).

9. The chi-square expansion is a mixture of densities such that $$1 = \sum_{k = 0}^{\infty} a_k \implies \sum_{k = K + 1}^{\infty} a_k = 1 - \sum_{k = 0}^{K} a_k$$

10. Shifted Digamma Natural Logarithm Inequality. $$ \ln(x + \nu)  - \psi (x + \nu + 1) \leq 0$$ To see this consider the following helping:
    1. From (https://en.wikipedia.org/wiki/Digamma_function#Inequalities) $$ \ln z - 1/z \leq \psi (z) \quad \forall z \geq 0 $$
    2. The digamma function satisfies: $$\psi (x+1)  = \psi (x) + 1 /x$$
    3. Use 2 in 1 to get the desired result.
    
    <!-- $$\begin{aligned} \end{aligned}$$ -->