# Nadimi

# Sought Ratio 

We're considered only in the distribution of the modulus of $$Z=\dfrac{X}{Y}\sim \dfrac{\mathcal{CN}(\nu_xe^{j\phi_x},\sigma_x^2)}{\mathcal{CN}(\nu_ye^{j\phi_y},\sigma_y^2)}$$ where the numerator and the denominator are independent.

# Rice Distribution

Note that if $X\sim \mathcal{CN}(\nu e^{j\phi},\sigma^2)$, then its PDF is given by $$f_{R_X}(r)=\dfrac{2r}{\sigma^2}\exp\left(-\left(\dfrac{r^2}{\sigma^2}+k^2\right)\right)I_0(\lambda)$$ where $k=\dfrac{\nu}{\sigma}$ and $\lambda=\dfrac{2r\nu}{\sigma^2}$. Now the joint distribution of the moduli is given by: $$f_{R_X,R_Y}(r_x,r_y)=\dfrac{4r_xr_y}{\sigma_x^2\sigma_y^2}\exp\left(-\left(\dfrac{r_x^2}{\sigma_x^2}+\dfrac{r_y^2}{\sigma_y^2}+k_x^2+k_y^2\right)\right)I_0(\lambda_x)I_0(\lambda_y)$$ where the quantities are defined similarly.

# Change of Variables

Transform $(X,Y)$ into $(Z=\dfrac{X}{Y},Y)$. Hence the joint PDF of the moduli is given by $$f_{R_Z,R_Y}(r_z,t)=tf_{R_X,R_Y}(tr_z,t)$$

# Expansion in Series

Recall that the modified Bessel function can be written as $$I_0(z)=\sum_{k=0}^\infty \dfrac{(\frac14z^2)^k}{(k!)^2}$$ Then the joint distribution contains the product $$\sum_{n=0}^\infty \dfrac{\left(\dfrac{r_z\nu_x}{\sigma_x}\right)^{2n}}{(n!)^2}t^{2n}\sum_{k=0}^\infty \dfrac{\left(\dfrac{\nu_x}{\sigma_x}\right)^{2k}}{(k!)^2}t^{2k}$$
Applying Cauchy product formula, i.e., collecting the coefficients of $t^{2m}$, we get $$\begin{aligned}c_m&=\sum_{\ell=0}^mc_x(\ell)c_y(m-\ell)\\
&= \sum_{\ell=0}^m \dfrac{1}{(\ell!)^2((m-\ell)!)^2}\left(\dfrac{r_z\nu_x}{\sigma_x}\right)^{2\ell}\left(\dfrac{\nu_y}{\sigma_y}\right)^{2(m-\ell)}
\end{aligned}$$
Hence the joint distribution can now be written as: $$f_{R_Z,R_Y}(r_z,t)=\dfrac{4t^3r_z}{\sigma_x^2\sigma_y^2}\mathrm{e}^{-\left(k_x^2+k_y^2\right)} \mathrm{e}^{-\left(\frac{r_z^2}{\sigma_x^2}+\frac{1}{\sigma_y^2}\right) t^2} \sum_{m=0}^{\infty} c_m t^{2 m}$$

# Marginalization 

Marinalizing over $t$, and using Equation 3.326.2 of Gradshteyn et al. $$\int_0^{\infty} x^m \exp \left(-\beta x^n\right) d x=\frac{\Gamma(\gamma)}{n \beta^\gamma}, \quad \gamma=\frac{m+1}{n}$$ we get the desired result: $$
f_{R_z}\left(r_z\right)= \frac{2 r_z \sigma_x^2 \sigma_y^2}{\left(r_z^2 \sigma_y^2+\sigma_x^2\right)^2} \mathrm{e}^{-\left(k_x^2+k_y^2\right)} \sum_{m=0}^{\infty} c_m(m+1) !\left(\frac{\sigma_x^2 \sigma_y^2}{r_z^2 \sigma_y^2+\sigma_x^2}\right)^m$$

# Notes

Nadimi didn't justify the interchange of the integral and the series. I think we can use LMCT. 
