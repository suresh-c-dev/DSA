def count_occurrences(items,target):
    count=0
    for item in items:
        if item==target:
            count=count+1
    return count 

print(count_occurrences([1, 2, 2, 3, 2], 2))    
print(count_occurrences(["a", "b", "a"], "a"))   
print(count_occurrences([5, 6, 7], 9))          
print(count_occurrences([], 1))          
print(count_occurrences([1, 2, 2, 3, 2], "2"))    
