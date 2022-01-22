import utils.util as util
import models.extract_tree_info as eti

def main():
    content = util.read_file()
    most_freq_trees = eti.get_most_frequent_trees(content)
    with open('../prun_trees_R/original_trees/single_trees/most_freq_trees.tre', 'w') as output_tree:
        output_tree.write(eti.get_header(content))
        for tree in most_freq_trees:
            output_tree.write(tree + '\n')
        output_tree.write('end;')

if __name__ == "__main__":
    main()