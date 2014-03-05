#!/bin/env python
# enconding: utf-8
import fileinput
import re
import time


def get_bigger_neighbor(array, last_index=0):
    if len(array) == 1:
        value = max(array)
        index = array.index(value)
        return value, index
    else:
        # value = max(array)
        index = last_index

        end = index + 2
        if len(array) <= 2:
            # start = 0
            end = index + 1
            tmp_array = array
        else:
            start = 0
            tmp_array = array[slice(start,end)]

        value = max(tmp_array)
        index = array.index(value)

        return value, index

def clear_and_convert_to_int(line):
    line = re.findall("\d+" , line)
    line = map(lambda x: int(x), line)
    return line


def _get_bigger_path(nodes):
    total = 0
    index = 0
    for n in nodes:
        value, index = get_bigger_neighbor(n, last_index=index)
        total += value
    return total


def execute():
    if not fileinput.input():
        print "Ta de pegadinha? Input vazio..."
    else:
        nodes = []
        for line in fileinput.input():
            nodes.append(clear_and_convert_to_int(line))
        print _get_bigger_path(nodes)

if __name__ == "__main__":

    start = time.time()
    execute()
    end = time.time()
    print "Tempo de execucao: ", end-start
