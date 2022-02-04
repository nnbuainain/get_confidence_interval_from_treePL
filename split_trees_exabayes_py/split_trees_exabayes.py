import utils.util as util
import constant
import models.extract_tree_info as eti

def main():
    util.cleanup()

    print('############# GETTING CONFIDENCE INTERVAL FROM TREE PL ################\n')
    print('The program will read all files starting with <exabayes_trees_run...> from folder <exabayes_phylo_trees_input>.\n')

    text = input("Type in ENTER to continue... \n")

    if text != "":
        return

    files_content_list = util.read_files_from_folder(file_location=constant.FOLDER, file_starts_with="exabayes_trees_run")

    if not files_content_list:
        print('It is not possible to continue. There is no file in the folder!')
        return

    # content_file1 = util.read_file(constant.FILE1)
    # content_file2 = util.read_file(constant.FILE2)
    # content_file3 = util.read_file(constant.FILE3)
    # content_file4 = util.read_file(constant.FILE4)

    trees_list = []
    for file_content in files_content_list:
        trees_list.append(eti.get_tree(file_content))

    # tree1_list = eti.get_tree(content_file1)
    # tree2_list = eti.get_tree(content_file2)
    # tree3_list = eti.get_tree(content_file3)
    # tree4_list = eti.get_tree(content_file4)

    all_trees_list = eti.interleave_tree(trees_list)

    # all_trees_list = eti.interleave_tree(tree1_list, tree2_list, tree3_list, tree4_list)

    topologies = eti.get_topologies(all_trees_list)

    # most_freq_trees = eti.get_last_100_trees(topologies, all_trees_list)
    most_freq_trees = eti.get_100_random_trees(topologies, all_trees_list)

    header = eti.get_header(files_content_list[0])
    footer = eti.get_footer()

    util.write_file(header, footer, most_freq_trees)

    print(f'Successfully recovered {len(most_freq_trees)} trees')

if __name__ == "__main__":
    main()