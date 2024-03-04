# Inputs:
1. $\alpha$: Half the degrees of freedom. 

2. $\mathbf{\Delta}$: Non-centrality parameter ($\times 2$)

3. $\mathbf{\Sigma}$: Covariance matrix of the indepenently sampled vectors ($\times 2$)

# Output:
The CDF of the Multivariate gamma distribution at point $(x_1, x_2, \ldots, x_p)$: $$F_{X_1, X_2, \ldots, X_p}(x_1, x_2, \ldots, x_p; \alpha, \mathbf{\Delta}, \mathbf{\Sigma})$$

# Steps:

1. Choose the arbitrary scale parameter $v$ such that $\|\mathbf{B}\|<1$, where $\mathbf{B}=(v\mathbf{\Sigma})^{-1}-\mathbf{I}_p$. A possible choice is $v=\frac12(\lambda_{\text{min}}^{-1}+\lambda_{\text{max}}^{-1})$.

2. Choose an arbitrary positive parameter $r$ so that $r>\|\mathbf{B}\|$.

3. Compute $\mathbf{D}=v^{-1}\mathbf{\Sigma}^{-1}\mathbf{\Delta}\mathbf{\Sigma}^{-1}$.

5. Set $F=0$.

5. Choose the number of steps $z$.

6. Numerical integration loop: For $(\phi_1,\phi_2,\ldots,\phi_{p}):=\left[-\pi+\dfrac{2\pi}{z}:\dfrac{2\pi}{z}:\pi\right]^{p}$:

    1. For $i=1:p$
        - Evaluate $y_i=r\mathrm{e}^{j\phi_i}$
        - Evaluate $G_i=\mathcal{G}_\alpha\left(vx_i, y_i\right)$ (using the frequently used functions). <span style="color : red"> Attention: Notations have flipped from the 2007 conv paper!!!</span>

    2. Calculate $G=\prod_{i=1}^{p}G_i$.

    2. Let $\mathbf{Y}=\operatorname{diag}(y_1,\ldots,y_P)$

    6. Calculate $G_{\text{outer}}=\dfrac{\operatorname{etr}\left(\mathbf{Y}^{-1}\left(\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right)^{-1} \mathbf{D}\right)}{\left|\mathbf{I}_p+\mathbf{B} \mathbf{Y}^{-1}\right|^\alpha}$.
 
 

    8. Add: $F+=G_{outer}G$.

7. Multiply: $F*=|v\mathbf{\Sigma}|^{-\alpha} \operatorname{etr}\left(-\mathbf{\Delta} \mathbf{\Sigma}^{-1}\right)(2 \pi)^{-p}$.

8. Finally: $F=F*\text{hypervolume of subdivision}$

## Frequently Used Functions

1. $\mathcal{G}_\alpha(x, y)=e^{-y} \sum_{n=0}^{\infty} G_{\alpha+n}(x) \dfrac{y^n}{n !}$

2. $G_\alpha(x)=\int_0^xg_\alpha(t)dt=\dfrac{\gamma(\alpha,x)}{\Gamma(\alpha)}=\begin{cases}
    1-e^{-x}\sum_{j=0}^{\alpha-1}\dfrac{x^j}{j!}&2\alpha \text{ is even}\\
    \operatorname{erf}(x^{1/2})-e^{-x}\sum_{j=1}^{\alpha-1/2}\dfrac{x^{j-1/2}}{\Gamma(j+\frac{1}{2})}&2\alpha \text{ is odd}
\end{cases}$

## Computational Test Cases
1 and 2 have theoretical hope!!!
1. The $K$ degrees of freedom non-central chi-square case:
    - Set $p = 1, K, \Delta = \delta = 0, \Sigma = \sigma^2 = 1$. The CDF is given trivially by: $$ F_X(x) = \gamma(K/2, x)/\Gamma(K/2)$$
    - Set $p = 1, K, \Delta = \delta = 1, \Sigma = \sigma^2 = 1$. CDF: $$ F_X(x) = 1 - Q_{K/2}(\sqrt{\delta}, \sqrt{x})$$
2. Independent Bivariate Chi-squares:
    - Set $p = 2, K, \Delta = 0, \Sigma = I$. The CDF is given by: $$F_{X_1,X_2}(x_1, x_2) = \frac{\gamma(K/2, x_1)\gamma(K/2, x_2)}{\Gamma(K/2)^2}$$
    - Set $p =2, K, \Delta = K\mathbf{J_p}, \Sigma = I$. Note $\mathbf{J_p}_{ij} = 1\;\forall i , j$. The CDF is given by: $$ F_{X_1,X_2}(x_1, x_2) = (1 - Q_{K/2}(\sqrt{K}, \sqrt{x_1}))(1 - Q_{K/2}(\sqrt{K}, \sqrt{x_2}))$$
3. The one factorial case:
    - Two dimensional case:
4. Hagedorn's Trivariate case such that his covariance matrix is real (for comparison)
<span style="color:red"> Hagedorn actually gives a PDF and hence direct numerical comparison against Royen 2007 paper is not straightforward!! </span>
5. Dharmawansa et al.: Take any specific case to compare against Royen

## Computational Thoughts

1. It may seem tempting to cut the domain in half, but the real part isn't even in each dimension. Counterexample: K = 3; Sigma = [1 0.8; 0.8 1]; delta = [1 2; 2 5]; z = 100; i_phiX2 = 20.


## Single CDF Case
We are interested in computing the CDF at a single value of $x_1, x_2, \ldots, x_P$.
```python
# Inputs
{x} # x_1, x_2, ... x_P
T = 100
v = 0.5
Delta
alpha = 
Sigma
P = size(Sigma, 1)

# Royens Predefinitions
B = v^-1 * (Sigma)^-1 - I
D = v * (Sigma)^-1 * Delta * (Sigma)^-1

# Precompute the values of for all indices.
Gcal_arr = zeros(P, T)
for j in range(P):
    for t in range(T):
        y_j_t = -pi + (2*pi/T)*t
        Gcal_arr[j, t] = Gcal(v * x[j], y_j_t)

G = 0
for s in range(T^P):
    {i} = LexicographicOrder(s) # i_1, i_2, ..., i_P
    {y} = {i} * (2*t/T)*pi
    f2_arg = I + (B .* transpose(y))
    f1 = exp(trace(((B + diag({y})) ^ -1)*D))
    f2 = det(f2_arg) ^ alpha
    f3 = G_util({i})
    G_s = f1 * f3 / f2
    G += G_s

# Volume and constants accounting

### Gcal Utility Function
# Inputs: {x}, {i} ==> {x_1, x_2, ... x_P}, {i_1, i_2, ..., i_P}
def G_util(i):
    G = 1
    for p in range(P):
        G *= Gcal_arr[p, i[p]]

def Lexicographic(s):
    # Use remainder and integer division as MATLAB does and suggested by Mahmoud. 
    # No need for pseudocode, just finished implementing it!!!!
```