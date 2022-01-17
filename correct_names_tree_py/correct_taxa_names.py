import pandas as pd
import glob

# Import dictionary as spreadsheets
dict = pd.read_excel('./dict_correct_names.xlsx')

# Format dictionary according to python
dict = dict.set_index('nome_original')['nome_final'].to_dict()

# Iter over files applying the rename function with the dictionary with original and final names
for index, file in enumerate(glob.iglob('../exabayes_phylo_trees/original/exabayes*')):
    with open(file, 'r') as f:
        content = f.read()
        for original, final in dict.items():
            content = content.replace(original, final)

    with open(f'../exabayes_phylo_trees/exabayes_trees_run_{index+1}','w+') as f:
        f.write(content)