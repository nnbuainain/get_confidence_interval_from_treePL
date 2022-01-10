import constant

def read_file():
    print('\nReading file...')

    lines = []
    with open(constant.FILE) as f:
        lines = f.readlines()

    return lines