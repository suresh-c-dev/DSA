def occurrence(items,target):
    count=0
    for item in items:
        if item==target:
            count=count+1
    return count 

print(occurrence([1, 2, 2, 3, 2], 2))    
print(occurrence(["a", "b", "a"], "a"))   
print(occurrence([5, 6, 7], 9))          
print(occurrence([], 1))          
print(occurrence([1, 2, 2, 3, 2], "2"))    
