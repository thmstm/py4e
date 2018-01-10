# Asking input from user on hours and rate
hrs = input("Enter Hours:")
rate = input("Rate per Hour:")

# Converting the input into float numbers
h = float(hrs)
r = float(rate)

# Print gross pay using a multiplier for rates above 40 hours
if h <= 40.0 :
    print(h * r)
else :
    multiplier = 1.5
    print((40 * r) + ((h - 40) * r * multiplier))