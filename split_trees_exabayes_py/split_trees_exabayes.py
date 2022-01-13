import utils.util as util

def get_legend(content: str) -> dict:
    legend_str = content.split('translate')[1].split(';')[0]
    legend_str = legend_str.replace('\n', '').lstrip()
    legend_dict = dict(x.split("	") for x in legend_str.split(",	"))
    return legend_dict

def get_tree(content: str):
    tree_str = content[content.index('tree gen.0.{0}'):].split('end')[0]
    return tree_str

def main():
    content = util.read_file()

    print('Extracting legend...')
    legend_dict = get_legend(content)
    print(f'Size of the legend: {len(legend_dict)}')

    print('Extracting trees...')
    tree_str = get_tree(content)
    print(f'First two trees...{tree_str[:13522]}')
    print(f'Last two trees... {tree_str[18036750:]}')

if __name__ == "__main__":
    main()