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

    for tree in tree_list:
        tree_splited = tree.split(':')[:-1]

    for tree in tree_splited:
        if tree[-2:].isdigit():
            cod_legend = tree[-2:]
            print(f'{cod_legend} - {legend_dict[cod_legend]}')
        elif tree[-1:].isdigit():
            cod_legend = tree[-1:]
            print(f'{cod_legend} - {legend_dict[cod_legend]}')


if __name__ == "__main__":
    main()