#coding:utf-8
import sys
'''这是nester.py模块，提供了一个名为print_lol的函数，这个函数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表'''
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
    '''这个函数的位置参数为the_list，可以是任何python列表。所指定的列表中的每个数据项会递归地输出到屏幕上，各个数据占一行'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t',end='',file=fh)
            print(each_item,file=fh)
