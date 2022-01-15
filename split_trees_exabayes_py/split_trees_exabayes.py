import utils.util as util

def get_legend(content: str) -> dict:
    legend_str = content.split('translate')[1].split(';')[0]
    legend_str = legend_str.replace('\n', '').lstrip()
    legend_dict = dict(x.split("	") for x in legend_str.split(",	"))
    return legend_dict

def get_tree(content: str) -> list:
    content = content.replace('\n', '').lstrip()
    tree_str = content[content.index('tree gen.0.{0}'):].split('end;')[0]
    tree_list = tree_str.split(';')[-101:-1]
    return tree_list

def main():
    content = util.read_file()

    # Extracting legend from file into a dictionary
    legend_dict = get_legend(content)
    print('\n--------------------- LEGEND ---------------------')
    for key, value in legend_dict.items():
        print(key, ' : ', value)

    # Extracting last 100 trees from file into a list
    tree_list = get_tree(content)
    print('\n--------------------- TREES ---------------------')
    for index, tree in enumerate(tree_list, start=1):
        print(f'{index}{tree}')

    # Get keys and values for each tree
    tree_split_list = []
    trees_are_equal = True
    all_cod_legend_previous = ''
    for index, tree in enumerate(tree_list, start=1): # tree_list['tree1...', 'tree2', ... 'tree100']
        tree_split = tree.split(':')[:-1] # tree_split['tree gen.2000000.{0} = [&U] (47', '5.764047943831943e-04,(78', ...]
        all_cod_legend_current = ''
        for partition in tree_split: # partition = 'tree gen.2000000.{0} = [&U] (47'
            if partition[-2:].isdigit():
                cod_legend = partition[-2:]
                all_cod_legend_current += cod_legend
                # print(f'{cod_legend} - {legend_dict[cod_legend]}')
            elif partition[-1:].isdigit():
                cod_legend = partition[-1:]
                all_cod_legend_current += cod_legend
                # print(f'{cod_legend} - {legend_dict[cod_legend]}')
        print(f'{tree_split[0]} - {all_cod_legend_current}')

        if index > 1:
            if all_cod_legend_previous != all_cod_legend_current:
                trees_are_equal = False
                break

        all_cod_legend_previous = all_cod_legend_current

    if not trees_are_equal:
        print(f' TREE # {index} is different')
    else:
        print('all trees are equal')

if __name__ == "__main__":
    main()