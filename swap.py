def swap(list, a, b):   
    list[a], list[b] = list[b], list[a] 
    return list   
list = ["priya","savita","priyanka","ravina"]
a, b  = 0, 3  
print(swap(list,a,b)) 
float_list=[8.9,9.1,5.9,9.0,1.9]
print (swap(float_list,a,b))
number_list=[4,6,7,8,6,5,5,4,8]
print(swap(number_list,a,b))