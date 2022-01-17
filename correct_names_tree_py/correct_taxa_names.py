import pandas as pd
import glob

# Import dictionary as spreadsheets
taxa_dict = pd.read_excel('./dict_correct_names.xlsx')

# Format dictionary according to python
taxa_dict = taxa_dict.set_index('nome_original')['nome_final'].to_dict()

# Iter over files applying the rename function with the dictionary with original and final names
for index, file in enumerate(glob.iglob('../exabayes_phylo_trees/original/exabayes*')):
    with open(file, 'r') as f1:
        content_1 = f1.read()
        for original, final in taxa_dict.items():
            content_1 = content_1.replace(original, final)

        with open(f'../exabayes_phylo_trees/exabayes_trees_run_{index+1}', 'w') as f2:
            f2.write(content_1)
            f2.close()
    f1.close()
