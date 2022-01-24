import utils.util as util
import constant
import models.extract_tree_info as eti

def main():
    content_file1 = util.read_file(constant.FILE1)
    content_file2 = util.read_file(constant.FILE2)
    content_file3 = util.read_file(constant.FILE3)
    content_file4 = util.read_file(constant.FILE4)

    tree1_list = eti.get_tree(content_file1)
    tree2_list = eti.get_tree(content_file2)
    tree3_list = eti.get_tree(content_file3)
    tree4_list = eti.get_tree(content_file4)

    all_trees_list = eti.interleave_tree(tree1_list, tree2_list, tree3_list, tree4_list)

    topologies = eti.get_topologies(all_trees_list)

    # most_freq_trees = eti.get_last_100_trees(topologies, all_trees_list)
    most_freq_trees = eti.get_100_random_trees(topologies, all_trees_list)

    header = eti.get_header(content_file1)
    footer = eti.get_footer()

    util.write_file(header, footer, most_freq_trees)

    print(f'Successfully recovered {len(most_freq_trees)} trees')

if __name__ == "__main__":
    main()