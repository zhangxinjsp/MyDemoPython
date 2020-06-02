#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

count_dict = {}
counted_file = {}
count_files = ['.swift', '.kt', '.dart', '.xml']

path = os.path.join(os.path.expanduser('~'), 'Desktop/CheryProject')

for folder, subFolders, files in os.walk(path):
    if '/Pods/' in folder:
        continue
    for file_name in files:
        for ends in count_files:
            if file_name.endswith(ends):
                num = count_dict.get(ends)
                file_list = counted_file.get(ends)
                if file_list is None:
                    file_list = []
                if num is None:
                    num = 0

                print(os.path.join(folder, file_name))
                if file_name not in file_list:
                    file_list.append(file_name)
                    counted_file[ends] = file_list
                else:
                    print(os.path.join(folder, file_name))

                file = open(os.path.join(folder, file_name))
                num += len(file.readlines())
                count_dict[ends] = num
                break

print(count_dict)
