"""In this Kata, your function receives an array of positive integers as input. Your task is to determine whether the numbers are in ascending order.

For the purposes of this Kata, you may assume that all inputs are valid (i.e. arrays containing only positive integers with a length of at least 2)."""

def in_asc_order(arr):
  print(True if arr == sorted(arr) else False)
    

arr = [2, 1]
in_asc_order(arr)#, False)
arr = [1, 2, 3]
in_asc_order(arr)#, True)
arr = [1, 3, 2]
in_asc_order(arr)#, False)
arr = [1,4,13,97,508,1047,20058]
in_asc_order(arr)#, True)
arr = [56,98,123,67,742,1024,32,90969]
in_asc_order(arr)#, False)