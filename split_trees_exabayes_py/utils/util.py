import constant
from collections import Counter
import glob

def read_file():
    with open(constant.FILE) as f:
        content = f.read()

    return content