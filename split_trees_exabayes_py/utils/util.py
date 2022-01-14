import constant

def read_file():
    with open(constant.FILE) as f:
        content = f.read()

    return content