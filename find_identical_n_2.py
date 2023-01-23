def find_identical(lst):
    value = None
    
    for j in range(len(lst)):
        value = lst[j]
        for i in range(len(lst)):
            if i != j and lst[i] == value:
                return value
            
    return None
