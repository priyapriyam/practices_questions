user_input=raw_input("Enter the student name")
students_record={"Priya":[34,56,78],"Neha":[56,78,90],"Ravina":[56,34,67],"pragti":[45,78,90]
,"Savita":[80,59,38]}
if user_input in students_record:
    print user_input
    a=user_input
    total=0
    i=0
    b=(students_record[a])
    while i<len(b):
        total=total+b[i]
        i=i+1
    avg=total/3
    avg= float(avg)
    print (avg)
    
    
    
    
    