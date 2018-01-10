# Initialising variables
count = 0
total = 0

# Starting loop
while True:
    # Ask for the user input
    sval = input('Enter a number: ')
    
    # If user types 'done' then exit
    if sval == 'done':
        break

    # Trying to convert user input to a value, but if it is not working, give an error message
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    # Adjusting counters
    count = count + 1
    total = total + fval

# Printing the total, the number of inputs and the average
print(total, count, total/count)