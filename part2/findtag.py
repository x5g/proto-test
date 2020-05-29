import os
import warnings
warnings.filterwarnings('ignore')
from collections import Counter
import numpy as np

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

def read(file):
    try:
        with open(file, 'r', encoding='utf-8') as f1:
            list1 = f1.read()
    except UnicodeError:
        with open(file, 'r', encoding='gbk') as f1:
            list1 = f1.read()
    return list1

if __name__ == '__main__':
    base_dir = './'
    if os.path.exists(base_dir + '/.DS_Store'):
        os.remove(base_dir + '/.DS_Store')

    protolist = file_name(base_dir)
    protolist = [proto for proto in protolist if str(proto).find('.proto') != -1]
    # print(protolist)
    for num, file in enumerate(protolist):
        content= read(base_dir + '/' + file)
        if 'oneof' in content:
            print(file)
