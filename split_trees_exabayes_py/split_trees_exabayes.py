import utils.util as util

def get_legend(content: str) -> dict:
    legend_str = content.split('translate')[1].split(';')[0]
    legend_str = legend_str.replace('\n', '').lstrip()
    legend_dict = dict(x.split("	") for x in legend_str.split(",	"))

    return legend_dict

def main():
    content = util.read_file()
    legend_dict = get_legend(content)

    for k, v in legend_dict.items():
        print(k, v)

if __name__ == "__main__":
    main()