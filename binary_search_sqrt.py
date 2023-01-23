# explanation: https://www.youtube.com/watch?v=plbSgfLCt74

def sqrt(x, eps=10 ** -6):
    low = 0
    high = max(1, x)
    
    while high - low > eps:
        mid = (low + high) / 2
        
        if mid**2 < x:
            low = mid
        else:
            high = mid
        
    return (high + low) // 2
    
    
print(sqrt(12))