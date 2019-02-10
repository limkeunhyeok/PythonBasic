# -*- coding: utf-8 -*-

class Star:
    def Type1(num):
        for i in range(1, num + 1):
            print('*' * i)
    def Type2(num):
        for i in range(num, 0, -1):
            print('*' * i)
    def Type3(num):
        for i in range(1, num + 1):
            print(' ' * (num - i) + '*' * i)
    def Type4(num):
        for i in range(num, 0, -1):
            print(' ' * (num - i) + '*' * i)
    def Type5(num):
        for i in range(1, num + 1):
            print(' ' * (num - i) +'*' * (i * 2 - 1))
    def Type6(num):
        for i in range(1, num + 1):
            print(' ' * (num - i) +'*' * (i * 2 - 1))
        for i in range(num - 1, 0, -1):
            print(' ' * (num - i) + '*' * (i * 2 - 1))

class Search:
    def Linear(arr, target):
        for i in range(0, len(arr)):
            if arr[i] == target:
                return i
        return -1
    def Binary(arr, target):
        arr.sort()
        start = 0;
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

class Sorted:
    def Selection(arr):
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                value1 = arr[i]
                value2 = arr[j]
                if value1 > value2:
                    arr[j] = value1
                    arr[i] = value2
    def Bubble(arr):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(0,i):
                value = arr[j]
                if value > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    def Insertion(arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
            print(arr)