import utils.util as util

def filter_legend(lines):
    count = 0
    for line in lines[5:100]:
        count += 1
        print(f'line {count}: {line}')

def main():
    lines = util.read_file()
    legend_dict = filter_legend(lines)

if __name__ == "__main__":
    main()