import os

def cleanup() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def read_file(file) -> str:
    with open(file) as f:
        content = f.read()

    return content

def read_files_from_folder(file_location, file_starts_with: str) -> list:
    files_content_list = []
    directory = os.path.normpath(file_location)

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith(file_starts_with):
                f = open(os.path.join(subdir, file), 'r')
                files_content_list.append(f.read())
                f.close()

    return files_content_list

def write_file(header, footer: str, most_freq_trees: list):
    with open('../prun_trees_R/original_trees/most_freq_trees.nexus', 'w') as output_tree:
        output_tree.write(header)
        for line in most_freq_trees:
            output_tree.write(line + '\n')
        output_tree.write('end;')