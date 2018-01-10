# Initialising variables
smallest = None
largest = None

# Starting loop
while True:
    # Ask for the user input
    sval = input('Enter a number: ')
    
    # If user types 'done' then exit
    if sval == 'done': break

    # Trying to convert user input to a value, but if it is not working, give an error message
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    # Adjusting counters
    if ((smallest is None) or (fval < smallest)):
        smallest = int(fval)
    if ((largest is None) or (fval > largest)):
        largest = int(fval)

# Printing the total, the number of inputs and the average
print('Maximum is', largest)
print('Minimum is', smallest)