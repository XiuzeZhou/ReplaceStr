#!usr/bin/python
# -*- coding:UTF-8 -*-
 
'''
Introduction: TODO(ICY)
Created on: 13/12/2018
@author: Xiuze Zhou
email: zhouxiuze@foxmail.com
'''
 
#-------------------------FUNCTION---------------------------#
from collections import defaultdict

#递归替换字符串中的字符
def n_replace( liststring, old, listnew):
    list1=[]
    for s in liststring: 
        if old not in s:
            return liststring
        else:                  
            for new in listnew:
                list1.append(s.replace(old, new, 1))
    if list1:
        return n_replace(list1, old, listnew)             

def generate(string, dic):
    # string: input string
    # dic: input dic
    
    lists=[[string]]
    for key in dic:
        if key in string:
            list=[string]
            lists.append(n_replace(lists[-1], key, dic[key]))
            #print(lists)                      

    return lists

       
#----------------------------SELF TEST----------------------------#
 
def main():
    str1="adcbf"
    input_dic1={'a': ['B', 'C'], 'b': ['X']}
    str2="adcbfaa"#有重复字符出现
    input_dic2={'a': ['B', 'C'], 'b': ['X','Y']}
    output=generate(str1, input_dic1)
    print(output[-1])
    output=generate(str2, input_dic2)
    print(output[-1])
 
if __name__ == '__main__': 
    main()