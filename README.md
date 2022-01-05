# get_confidence_interval_from_treePL
A project to get confidence interval from phylogenetic trees with treePL

Phylogenetic trees estimate the evolutionary relationships among individuals. treePL is a software developed to estimate divergence times in a phylogenetic tree, and is especially useful with large datasets such as genomic data or large trees. However, divergence times is given as a point value and does not accomodate uncertainty.

## GOAL

The goal of this project is to develop a pipeline to get confidence intervals for divergence times from multiple phylogenetic trees in treePL. We will do that from a subset of phylogenetic trees sampled from the posterior generated in a Bayesian Framework in the software ExaBayes.

## STEPS

1) Subsample and separate n trees from the posterior in different files
2) Run treePL with each tree
3) Summaryze results for each node

