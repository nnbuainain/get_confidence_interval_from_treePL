from collections import Counter
from random import sample
import glob

def get_header(content: str) -> str:
    header = content.split('tree gen.0.{0}')[0].split(';')[:-1]
    header[0] = header[0] + ';'
    header.append(';\n')
    header = ''.join(header)
    return header

def get_footer() -> str:
    footer = 'end;'
    return footer

def get_legend(content: str) -> dict:
    legend_str = content.split('translate')[1].split(';')[0]
    legend_str = legend_str.replace('\n', '').lstrip()
    legend_dict = dict(x.split("\t") for x in legend_str.split(",	"))
    return legend_dict

def get_tree(content: str) -> list:
    content = content.replace('\n', '').lstrip()
    tree_str = content[content.index('tree gen.0.{0}'):].split('end;')[0]
    tree_list = tree_str.split(';')[-2::-1]
    return tree_list

def interleave_tree(trees_list: list) -> list:
    interleaved_list = []
    len_list = len(trees_list[0])

    for index in range(len_list):
        for tree_list in trees_list:
            interleaved_list.append(tree_list[index])
    interleaved_list.reverse()

    return interleaved_list

def get_topologies(tree_list: list) -> list:
    topology_list = []

    for index, tree in enumerate(tree_list): # tree_list['tree1...', 'tree2', ... 'tree100']
        tree_split = tree.split(':')[:-1] # tree_split['tree gen.2000000.{0} = [&U] (47', '5.764047943831943e-04,(78', ...]
        topology = ''
        for partition in tree_split: # partition = 'tree gen.2000000.{0} = [&U] (47'
            if partition[-3:].isdigit():
                cod_legend = partition[-3:]
                topology += cod_legend

            if partition[-2:].isdigit():
                cod_legend = partition[-2:]
                topology += cod_legend

            elif partition[-1:].isdigit():
                cod_legend = partition[-1:]
                topology += cod_legend

        topology_list.append(topology)
    return topology_list

def get_last_100_trees(topology_list, tree_list: list) -> list:
    # Reverse topology list and tree list to place "best" tree on top
    topology_list.reverse()
    tree_list.reverse()

    # Get most frequent topology in the last 100 samples
    most_freq_topology = Counter(topology_list[:100]).most_common(1)[0][0]

    # Get trees with the most frequent topology
    most_freq_trees = [tree_list[i] for i, t in enumerate(topology_list) if t == most_freq_topology]

    # Select the last 100 samples with the most frequent topology
    if len(most_freq_trees) > 100:
        return most_freq_trees[:100]
    else:
        return most_freq_trees

def get_100_random_trees(topology_list, tree_list: list) -> list:
    # Reverse topology list and tree list to place "best" tree on top
    topology_list.reverse()
    tree_list.reverse()

    # Discard first 25% of tree which usually didn't reach stationarity of parameters
    topology_list = topology_list[:round(len(topology_list)*0.75)]

    # Get most frequent topology in the last 100 samples
    most_freq_topology = Counter(topology_list).most_common(1)[0][0]

    # Get trees with the most frequent topology
    most_freq_trees = [tree_list[i] for i, t in enumerate(topology_list) if t == most_freq_topology]

    # Select the last 100 samples with the most frequent topology
    if len(most_freq_trees) > 100:
        return sample(most_freq_trees, k=100)
    else:
        return most_freq_trees
