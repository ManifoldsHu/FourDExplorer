# -*- coding: utf-8 -*- 

import os
import sys

def tree(dir_path, prefix=''):
    contents = os.listdir(dir_path)
    contents.sort()
    for index, name in enumerate(contents):
        path = os.path.join(dir_path, name)
        is_last = (index == len(contents) - 1)
        if is_last:
            connector = '└── '
        else:
            connector = '├── '
        print(prefix + connector + name)
        if os.path.isdir(path):
            if is_last:
                extension = '    '
            else:
                extension = '│   '
            tree(path, prefix + extension)

if __name__ == '__main__':
    # 接收命令行参数，默认为当前目录
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = '.'
    base_name = os.path.basename(os.path.abspath(root_dir))
    print(base_name + '/')
    tree(root_dir)
