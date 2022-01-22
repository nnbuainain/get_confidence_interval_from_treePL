#!/bin/bash

files=(../prun_trees_R/pruned/*.tre)
folder=runs/run_
count=0

for i in "${files[@]}"
do
   mkdir "$folder$count"/
   cp "$i" "$folder$count"/arremon.tre
   cp configuration "$folder$count"/configuration
   let count=$count+1

done