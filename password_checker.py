user_input=raw_input("Enter your password")
if user_input <= 6:
    print"Strong password"
elif user_input <=16:
    print "Strong password"
elif "$" in user_input:
    print "Strong password"
elif "2" in user_input:
    print "Strong password"
elif "8" in user_input:
    print "strong password"
elif "A" in user_input:
    print "Strong password"
elif "Z" in user_input:
    print "Strong password"
else:
    print "weak password"
