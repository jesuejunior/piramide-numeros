#!/bin/env python
# enconding: utf-8
import fileinput
import re
import time


def get_bigger_neighbor(array, last_index=None):

    if last_index:
        value = max(array)
        index = last_index
        return value, index
    else:
        value = max(array)
        index = array.index(value)

    start = index-1
    end = index + 2
    if len(array) < 3:
        start = 0
        end = index + 1

    tmp_array = array[slice(start,end)]
    value = max(tmp_array)
    index = array.index(value)

    return value, index


class Queue(object): 

    def __init__(self):
        self.holder = []

    def enqueue(self,val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except:
            pass
        return val

    def is_empty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


def bfs(graph,start,end,q):

    temp_path = [start]
    q.enqueue(temp_path)

    while q.is_empty() == False:
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path)-1]
        print tmp_path
        if last_node == end:
            print "VALID_PATH : ",tmp_path
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)


def clear_and_convert_to_int(line):
    line = re.findall("\d+" , line)
    line = map(lambda x: int(x), line)
    return line

def execute():
    if not fileinput.input():
        print "Ta de pegadinha? Input vazio..."
    else:
        nodes = []
        for line in fileinput.input():
            nodes.append(clear_and_convert_to_int(line))

        print nodes
        total = 0
        index = 0
        value = 0
        for n in nodes:
            if not index:
                value, index = get_bigger_neighbor(n,last_index=0)
            else:
                value, index = get_bigger_neighbor(n,last_index=index)

            total += value

        print total
if __name__ == "__main__":

    start = time.time()
    execute()
    end = time.time()
    print "Tempo de execucao: ", end-start
