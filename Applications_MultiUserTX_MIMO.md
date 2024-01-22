# Jan 18<sup>th</sup> 2024: Multi-User TX-MIMO with Single RX Antenna

Consider a communication system with a single base station in Downlink scenario with $K$ users. The base stations is equiped with $M$ antennas. In the downlink, we want to deliver to each user a symbol $s_i\;\forall i \in [1, K]$.

1. The base station and users agree upon beam forming vectors $w_i \in \mathbb{C}^{M \times 1}, \forall i \in [1, K]$. 

2. The K incoming symbols are multiplied by the beam-forming vectors and summed up. To produce the transmitted symbols at the $M$-antennas. Thus the transimtted symbols $x$ are given by: $$x = \sum_{i=1}^{K} w_i s_i $$
Thus an individual symbol $x_j$ (appearing at the $j^{th}$ transmitter) is given by: $$ x_j = \sum_{i=1}^{K} (w_i)_j s_i \quad \forall j \in [1,M]$$

3. The symbol rate is assumed much less than the coherence bandwidth of the channel. Thus all multipaths can be accounted for in one symbol duration. The channel is represend by matrix $H \in \mathbb{C}^{K \times M}$. Each entry $h_{ij}$ indicates the gain and phase of the $j^{th}$ antenna beam at the $i^{th}$ user antenna. The channel entries are assumed gaussian: $$H \sim \mathcal{CN}(0, R)$$

<span style="color:red;font-weight:bold;font-size:14pt;"> When is it reasonable to assume the channel gains are correlated and when are the independent (uncorrelated)?</span>

4. The received signals at each of the receiver antennas are $y_1, y_2, \ldots, y_K$. $$y  = Hx + v, \quad v \sim \mathcal{CN}(0, \sigma_v^2I)$$

5. For an individual user the received signal is given by: $$ y_i = (H)_i x + v_i = \sum_{m = 1}^{M}H_{im} x_m + v_i = \sum_{m = 1}^{M}\sum_{k = 1}^{K}H_{im}(w_k)_ms_k + v_i$$

6. The $i^{th}$ user is interested only in the $i^{th}$ symbol $s_i$. Thus we extract the terms with $s_i$ alone. The rest are considered interference. $$y_i = \left(\sum_{m=1}H_{im}(w_i)_ms_i\right) + \left\{\sum_{m = 1}^{M}\sum_{\substack{k = 1 \\ k \neq i}}^{K}H_{im}(w_k)_ms_k\right\} + v_i$$

7. The SINR is now given by the signal term (round brackets) divided by the noise term ($v_i$) and the interference terms (curly brackets) after conversion to energy quantities (taking the norms). 
    - Towards that end the signal symbols $s_i$ are assumed drawn form zero mean distribution and with a unit variance, $\mathbb{E}[s_i] = 0, \mathbb{V}[s_i] = 1$ and that user symbols are independent such that $\mathbb{E}[s_is_j] = 0 = \mathbb{E}[s_is_j^*], \forall\; i \neq j$.
    
    - The signal energy is given by: $$S = \mathbb{E}_s\left[\left|\sum_{m=1}^MH_{im}(w_i)_ms_i\right|^2\right] = \mathbb{E}_s[|s_i|^2] (H_i w_i)(H_i^* w_i^*) = H_i^*w_iw_i^HH_i = |H_iw_i |^2$$

    - The interference power is given by: $$I = \mathbb{E}_s\left[\left| \sum_{m = 1}^{M}\sum_{\substack{k = 1 \\ k \neq i}}^{K}H_{im}(w_k)_ms_k \right|^2\right] = \sum_{m = 1}^M\sum_{n = 1}^M \sum_{\substack{k = 1 \\ k \neq i}}^{K} \sum_{\substack{q = 1 \\ q \neq i}}^{K}$$