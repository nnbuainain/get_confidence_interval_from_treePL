def read_file(file) -> str:
    with open(file) as f:
        content = f.read()

    return content

def write_file(header, footer: str, content: list):
    with open('../prun_trees_R/original_trees/most_freq_trees.nexus', 'w') as output_tree:
        output_tree.write(header)
        for line in content:
            output_tree.write(line + '\n')
        output_tree.write('end;')