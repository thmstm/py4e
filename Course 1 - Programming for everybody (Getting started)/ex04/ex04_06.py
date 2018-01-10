# Defining the "computepay" function to return the gross pay according to schedule
def computepay(h, r):
    if h <= 40.0 :
        return h * r
    else :
        m = 1.5
        return (40 * r) + ((h - 40) * r * m)


# Asking input from user on hours and rate
hrs = input("Enter Hours: ")
rate = input("Rate per Hour: ")

# Converting the input into float numbers
h = float(hrs)
r = float(rate)

# Print gross pay using a multiplier for rates above 40 hours
print(computepay(h, r))