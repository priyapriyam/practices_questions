user_input=input("Number of students")
user_input1=input("Ek student ka kharcha")
expense=0
student=0
while student <= user_input:
    expense=student*user_input1
    student=student+1
    if 50000 >= expense:
        print "hum budget ke andar hai"
    else:
        print "hum budget ke bahar hai"
    
