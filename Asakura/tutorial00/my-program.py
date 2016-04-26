#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict

def add_and_abs(x, y):
    z = x+y
    if z >= 0:
        return z
    else:
        return z * -1


def main():
    my_int = 4
    my_float = 2.5
    my_string = 'hello'
    print('string:{}\tfloat:{}\tint:{}'.format(my_string,my_float,my_int))

    my_variable = 5
    if my_variable == 4:
        print('my_variable is 4')
    else:
        print('my_variable is not 4')
    for i in range(1,my_variable):
        print('i == {}'.format(i))
    
    my_list = [1,2,4,8,16]
    my_list.append(32)
    print(len(my_list))
    print(my_list[3])
    print('')

    for value in my_list:
        print(value)

    my_dict = {"alan":20,"bill":45,"chris":17,"dan":27}
    my_dict["eric"] = 33

    print(len(my_dict))
    print(my_dict["chris"])
    if "dan" in my_dict:
        print("dan exists in my_dict")

    for foo, bar in sorted(my_dict.items()):
        print("{}-->{}".format(foo, bar))

    my_dict = defaultdict(lambda:0)
    my_dict["eric"] = 33
    print(my_dict['eric'])
    print(my_dict['fred'])

    for foo, bar in sorted(my_dict.items()):
        print("{}-->{}".format(foo, bar))

    sentence = "this is a pen"
    words = sentence.split(" ")
    for word in words:
        print(word)

    print(" ||| ".join(words))

    print(add_and_abs(-4, 1))

    my_file = open(sys.argv[1],'r')

    for line in my_file:
        line = line.strip()
        if len(line) != 0:
            print(line)



if __name__ == '__main__':
    main()
