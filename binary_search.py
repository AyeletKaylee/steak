def search(val, seq):
    return binary_search(val, seq, 0, len(seq))

def binary_search(val, seq, low, high):
    if low >= high:
        return -1
    
    mid = (low + high) // 2
    
    if seq[mid] == val:
        return mid
    elif seq[mid] > val:
        return binary_search(val, seq, mid + 1, high)
    return binary_search(val, seq, low, mid)

# runtime:
#  ██████╗  ██╗██╗      ██████╗  ██████╗     ███╗   ██╗██╗ 
# ██╔═══██╗██╔╝██║     ██╔═══██╗██╔════╝     ████╗  ██║╚██╗
# ██║   ██║██║ ██║     ██║   ██║██║  ███╗    ██╔██╗ ██║ ██║
# ██║   ██║██║ ██║     ██║   ██║██║   ██║    ██║╚██╗██║ ██║
# ╚██████╔╝╚██╗███████╗╚██████╔╝╚██████╔╝    ██║ ╚████║██╔╝
#  ╚═════╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═══╝╚═╝ 
                                                         