# Notes on TSP White Paper 11th Feb 2024

1. In the abstract we compare our selves to Mathai. We should point out we are broadening the "actual scope" by discussing multivariate chi squares and general multivariate quadratic forms.

2. The statement *"...Through this comprehensive overview, valuable insights will be
offered to elucidate the significance and implications of these
results in practical applications..."* is very generic. We need to have more specifics. Mahmoud suggests we comment on the following questions?
    1. Is there any available code (I think this is important as it removes the burden of producing an "optimzed" implementation.
    2. Computational efficiency: as obtaining theoretical bounds is a highly demanding open problem, we can resort to empirical measures (CPU time,...)
    3. The applicability of the model plays an impoirtant part: from a practical (domain-specific) point of view, is the model widely applicable?
<span style="color:red"> This needs more work from us </span>

3. Mahmoud noted that through the papers we studied (till 11th Feb 2024) the particular case of definite complex (non-central forms) did not have special "effects/results". Athley reports an ugly formula in his 2005 paper Eq 18 which might be worthy of reporting. See his thesis Eq 9.34 which cites Proakis 1995 (probably appendix B)

<span style="color:red"> We want to do this for the references moazz cites and see if they have new formulas or are using the ones we covered (or excluded)! </span>

4. Mahmoud comments that *the thread joining the two entities is very thin*. They are both instances of $x^TA_ix^T + b_i^Tx + c_i$. Using applications can strengthen this thin thread! (make it not look as contrived!!)

5. We can use the $^\dagger$ operator to generalize. We can also call it the "adjoint operators". Does the word adjoint apply to vectors??? 

6. Consider this sentence: "... These metrics are considered from both an analytical standpoint and in terms of computational aspects ... ". Does Maaz mean the literature has these considerations or does he mean that we considered them. Assuming the 2nd, Mahmoud thinks we need more work to make this claim. For example can we answer the following questions:
    1. When considering +ve definite QFs which is better: power series or Laguerre Series? (Laguerre series is better, but why?)
    2. Chi Square expansion or Moment matching methods. From accuracy under infinite resources,  expansions are better but under double precision floating point and finite time, which is better?
    3. Saddle point (Kuonen 1999, Al-Naffouri 2016) vs. Ha and Provost for indefinite?
    4. Can we compare methods that appear equivalent in our Subsupmtion Graphs?
        - Wiegand (2019) and Khammassi (2022)?
        - Royen 1991 and Royen 2007?
    5. <span style="color:red">There probably should be many more questions here?</span>
    6. Can we resort to simplified aggregate measures like wall-time/flop count?

7. Maaz used the label "inverting the characteristic function" seemingly in place of Numerical integration. If that is the case Mahmoud notes that: "Numerical integration does not only arise from inversion, it can also be the result of marginalization, deconditioning ... "

8. Mohanad says: "We should mention the names of the various problems to entice the reader" next to the "[1] - [14]" and probably brake down this bulk into individual ones.

9. The sentence: *"... Given the scattered nature of the theoretical framework surrounding quadratic forms in the existing literature, we recognized the importance of consolidating this knowledge for the benefit of the community ... "* is unclear and worded wierdly for me. What does this mean? Does it mean the scattered results to compute quadratic forms? What is the `theoretical framework`?

10. On **Establishing Connections**: Mahmoud comments that we showed connections, we did not establish them. He suggests: 
    "Maybe we should try to rederive new results from older ones, examples: 
    1. derive Khammassis's from Royen's (this doesn't belittle her formula, since her method of approximation by an \epsilon-rank factorial is easier to grasp
    2. derive Al-Naffouri's exact central complex from already available finite expressions
    3. In the multivariate subsumption graph, go through the edges and check quickly if the formula (i) collapses to (j)'s; if that's true, we consider two cases:
        1. if (i) is older than (j), and (j) doesn't mention the relation explicitly, that's a new connection
        2. if (j) is older than (i), we can say (i) is a gneralization
11. On **Numerical and Computational Considerations**: Mahmoud suggests that we will need a lot more work to fullfill the promise of this paragraph!

12. Mahmoud asks **Question: if we submit to this journal, should we limit our apps to signal processing?**. Mohanad says no. In fact I think it is important to point other fields to the signal processing people.

13. On **M vs. N** graph: Mahmoud asks whether we should give it a more descriptive name, that can be used to refer to it.

14. It fact the naming of all the summary graphs and tables should be considered as a whole. Preferably close to the deadline!!!

15. Should we follow Hadi's style, where he mentions the sections of the paper and what each section considers? Recall Hadi's was rejected!!

16. There is a suddent transition into the last two paragraphs? Do we need more paragraphs for the white paper?

17. A very important question: if we do submit to TSP what would the structure of the document be? What does the table of contents look like?

## Side Questions:
1. Does Al-Naffouri's Saddle point for real central form apply to non-central forms? By doing some other derivations? Mohanad thinks yes it should apply!