# explanation: https://www.youtube.com/watch?v=kFeXwkgnQ9U
# another implementation on page 29 in lecture slides of week 7

from typing import List, Any

def quick_sort(sequence: List[Any]):
    length = len(sequence)
    if length <= 1:
        return sequence # the sequence is sorted as is
    
    pivot = sequence.pop()
    
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
            
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)   

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))



# time complexity:
#    ___     __           __                          __   
#  .'   `. .' _|         [  |                        |_ `. 
# /  .-.  \| |   _ .--.   | |  .--.   .--./) _ .--.    | | 
# | |   | || |  [ `.-. |  | |/ .'`\ \/ /'`\;[ `.-. |   | | 
# \  `-'  /| |_  | | | |  | || \__. |\ \._// | | | |  _| | 
#  `.___.' `.__|[___||__][___]'.__.' .',__` [___||__]|__,' 
#                                   ( ( __))               