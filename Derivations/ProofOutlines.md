## 1. Gardini's Method
1. Assume we have the chi-square expansion coefficients
    - This is a non-trivial computational step.
    - Choose Beta so that the expansion is assured to be a mixture (see Ruben 1962).
2. Compute the Mellin transform.
3. Write the inverse mellin transform as a numerical integration (rectangular sum method), and estimate the two errors
    - Series Truncation error
    - Integral Truncation Error: (under the assumption of existence of quadratically decaying upper bound of the Mellin transform)

## 2. Khammasi's method
1. The basic idea in this method is to reduce the number of correlated variables to the most significant ones. This is achieved by expanding the covariance matrix in an eigenvalue (singular value) decomposition, then truncating the eigenvectors/eigenavalues with values smaller than some $\epsilon$.
2. We compensate the variance of each of the approximate variables to match the variance of the original. This is achieved by adding independent normals with the missing variance.
3. The approximate variables have the same variance as the originals, but only the most dominant $\epsilon-\text{rank}$ correlations are included (as indicated by common variables / m-factorial). $\epsilon-\text{rank}$.
4.  We closed form integrate for the (non-shared variables) and brute force numerically integrate for the shared variables.

## 3. Laverny's method
1.  

## 4. Gu's method
1. 

## 5. Tekinay and Beard method
1.

## 6. Zhang Shen Wu method
1. It is moment matching method that matches to a linearly scaled gamma variate with four moments. 
2. Computing the moments for large numbers of variables such as genetic applications requires heavy computational load. They provide a method to reduce this. The method does not reduce the $O(N^3)$ complexity but rather the scalar coefficient of the third power in the complexity formula. This comes at the cost of an increase of the quadratic coefficient.

### Side Comment (Mahmoud)
Genetics applications compared to old/statistics and telecomm/sig. proc. the focus more is on manipulating the moments/eigenvalues to take less time, whilst the later focus on the convolution of the  chi-squareds.
 
 ## 7. Bithas
 1.

 ## 8. Chen and Lumley method

# Question to Complete Paper
1. New "SECTION" **Literature Statistics and Classifications**.
    - Classification diagrams: "*what are the broad categories of works in this area, as we see them?*"
        - Show one diagram and differentiate category B.
    - Citation count:
        - Bar graph, ordinal/date sorted x-axis, y-axis is citations
        - Scatterplot with actual date scale.
        - Scopus/Semantic Scholar/*Cooked Google Scholar!!*.
    - Subsumption graph: *"which formula can be used in place of the other?*"
        - This graph is highlighs the fact that although they are all quadratic forms, they are not equal. Some are more general or cover more cases.
        - An edge in this graph indicates subsumption.
        - Needs checking the adjacency matrix.
        - Needs a drawing mechanism. (Maybe in python) hopefully with vector graphic export or something in tikz.
2. Applications section writeup:
    - System Reliability and Structural  Engineering :
        - We need many citations (at least 15)
        - Kinematic Reliability
        - Transmissivity of structures
    - Telecommunications section:
        - SNR modelling for MIMO systems
        - Angle of Arrival estimation
        - Time of Arrival estimation
        - GNSS false alarm
    - Genetics:
        - Variance Components Score metric derivation.
            - Can we derive this $Q = (Y - X\hat{\alpha})^T G W G^T (Y - X \hat{\alpha})$?
            - are there other tests/applications related to genetics where a quadratic form pops up?
    - Financials / Econometrics
