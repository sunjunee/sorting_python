# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:45:09 2018

@author: 孙俊
"""
import time
import random

def sortName(nums):
    '''
    排序算法
    :param nums: Inputs list of nums
    :return: sorted list
    '''

    return nums

def selectSort(nums):
    '''
    选择排序
    :param nums: Inputs list of nums
    :return: sorted list
    '''
    lens = len(nums)
    for i in range(lens):
        minI = i
        for j in range(i+1, lens):
            if(nums[j] < nums[minI]):
                minI = j
        nums[i], nums[minI] = nums[minI], nums[i]

def InsertSort(nums):
    '''
    插入排序
    :param nums: Inputs list of nums
    :return: sorted list
    '''
    lens = len(nums)

    for i in range(1, lens):
        for j in range(i, 0, -1):
            if(nums[j] >= nums[j-1]):
                break
            else:
                nums[j], nums[j-1] = nums[j-1], nums[j]

def shellSort(nums):
    '''
    希尔排序
    :param nums: Inputs list of nums
    :return: sorted list
    '''
    #先构造递增系列

    lens = len(nums)

    s = 1
    while(s < lens / 3):
        s = s * 3 + 1   #递增序列

    while(s >= 1):
        for i in range(s, lens):
            for j in range(i, s-1, -s):
                if(nums[i] > nums[j - s]):
                    break
                else:
                    tem = nums[j - s]
                    nums[j - s] = nums[j]
                    nums[j] = tem

        s = int(s / 3)

def bubbleSort(nums):
    '''
    冒泡排序
    :param nums: Inputs list of nums
    :return: sorted list
    '''
    lens = len(nums)
    for i in range(lens):
        for j in range(lens - 1 - i):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]

def fastSort(nums, start = 0, end = None):
    '''
    快速排序
    :param nums: Inputs list of nums
    :return: sorted list
    '''

    lens = len(nums)

    if(end == None):
        end = lens - 1

    if(end <= start):
        return

    #最后一个值作为比较的值
    keyV = nums[end]

    # 然后把大于该数的放在右边，小于的放在左边
    i = start;  j = end
    while(i < j):
        #从前往后
        while((nums[i] <= keyV) and (i < j)):
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

        #从后往前
        while((nums[j] >= keyV) and (i < j)):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    #此时i = j，且为keyV， 则递归
    fastSort(nums, start, i-1)
    fastSort(nums, i+1, end)

def main():
    nums = [random.randint(1, 500) for i in range(200)]
    print(nums)

    sortAlgoritms = [bubbleSort, selectSort, InsertSort, fastSort]

    for func in sortAlgoritms:
        start = time.time()
        func(*(nums,))
        end = time.time()
        print(nums)
        print(func.__name__, " ", end - start)


if __name__ == "__main__":
    main()