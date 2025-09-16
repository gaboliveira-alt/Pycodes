
def recursive(start=0, end=4):
    print(start, end)
    
    if start >= end:
        return end
    
    
    start += 1
    return recursive(start, end)


print(recursive())