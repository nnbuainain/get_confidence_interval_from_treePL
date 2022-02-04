# get_confidence_interval_from_treePL
> Developed by *Nelson Buainain & Maura Regina*

A project to get confidence interval from phylogenetic trees with treePL. 

Phylogenetic trees estimate the evolutionary relationships among individuals. treePL is a software developed to estimate divergence times in a phylogenetic tree, and is especially useful with large datasets such as genomic data or large trees. 

However, divergence times is given as a point value and does not accomodate uncertainty.

## GOAL

The goal of this project is to develop a pipeline to get confidence intervals for divergence times from multiple phylogenetic trees in treePL. 

We will do that with a subset of phylogenetic trees sampled from the posterior generated in a Bayesian Framework in the software ExaBayes.

## STEPS

1) Interleave the files of n independent runs of Exabayes
2) Subsample n trees from the posterior of Exabayes. Selection can be done by picking the last 100 trees with the most frequent topology, 100 random trees with the most frequent topology or just 100 random trees.
3) Prun trees using Phytools to include only one sample per taxa
4) Run treePL for each tree
5) Summarize results for each node using TreeAnnotator

## Current situation

The pipeline to extract the last 100 trees is running, the functions to sample at random with the most frequent topology or just at total random are ready, but need to be implemented to the automated pipeline.


