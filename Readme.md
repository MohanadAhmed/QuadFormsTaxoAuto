# Quadratic Forms Taxonomy Automater
## Objectives:
We have collected many references related to **Quadratic Forms in Gaussian Random Variables** . Many of these contain formulae to evaluate statistical properties of interest such as : Cumulative Distribution Functions, Probability Distribution Functions, Moments and so on. We wish to present a taxonomic view of these references. We have so far enumerated 8 items we wish to present. As we add or remove references managing the synchronization between these many faces is cumbersome and error prone. We wish to have a single of manual entry source from which the items below can be generated. In this branch and repo we develop the sources responsible for this process.

1. List of References Category A
    - We define `Category A` as: the set of references after 1990 or not cited by Mathai and Provost in their Book of Quadratic Forms in Gaussian Random Variables.

2. List of References Category B
    - We define `Category B` as: the set of references before 1990 or not cited by Mathai and Provost.

3. Classification Diagram
	- Category A
	- Category A  `Union` Category B
	
4. Raw input classification table:
    - Multivariate
    - Ratios
    - Single
	
5. Formula Type {Six Categories Diagram/Table}
    - Finite Expression
    - Infinite Series
    - Numeric Integration
    - Approximate Random Variable
    - Moment Matching
    - Saddle Point Approximation

6. Approach/Common Themes Table
    - M-factorial Representation of Covariance Matrix
    - Parital Fraction Decomposition
    - Integral Transform / Inversion
    - Marginalization over Auxiliary Variables

7. Formula Supplement
	- Formulas
	- Steps/PsuedoCode
	
8. Quadratic Form Subsumption Graph 
	- Multivariate 
    - Ratios 
    - Single

9. M vs. N graph

    This graph shows which papers have **"actually"** computed quadratic froms for what values of $M$ (the number of quadratic forms) and $N$ (the number of gaussian variables).

## The Lists

1. List of References Category A
    - We define `Category A` as: the set of references after 1990 or not cited by Mathai and Provost in their Book of Quadratic Forms in Gaussian Random Variables.

2. List of References Category B
    - We define `Category B` as: the set of references before 1990 or not cited by Mathai and Provost.

How do we generate the items above?
These should be very straight forward. We need a text based file (preferrably json) containing citation keys and the category for each item. What format do we use? Two big objects category A and B with citation key arrays. Or citation key objects with category tags?

Lets assume the earlier. We run through each list and output a latex file line that says: \fullcite{item}.

We also want post notes to differentiate repeat items. We need to include post note in source file.

I guess one way now is a CSV File

Bibkey | Equation No | Category (A or B) | 
-------|-------------|-------------------|
mohanad2023 |Eq 5 | A |

 
The classification diagram we have has 3 main categories: Single, Ratios, Multivariate.
In the Single Forms we have (Centra, Definite, Definite Central) subcategories. In the Ratios we have: Moments

### Mahmoud was here
