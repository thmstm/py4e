score = input("Enter Score: ")
try :
    sc = float(score)
except :
    print("Error, please enter a number.")
    quit()
    
if sc >= 1.0 :
    print("Please enter a number smaller than or equal to 1.0.")
elif sc >= 0.9 :
    print("A")
elif sc >= 0.8 :
    print("B")
elif sc >= 0.7 :
    print("C")
elif sc >= 0.6 :
    print("D")
elif sc >= 0.0 :
    print("F")
else :
    print("Please enter a number greater than or equal to 0.0.")