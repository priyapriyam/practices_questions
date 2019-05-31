def swapPositions(list, a, b): 
      
    list[a], list[b] = list[b], list[a] 
    return list
   
list = [2,4,6,10,15,8] 
a, b  = 1,5
  
print(swapPositions(list, a-1, b-1)) 
