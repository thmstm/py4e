text = "X-DSPAM-Confidence:    0.8475";

# Finding the colon ':' sign in the text
colon = text.find(':')
# Taking the part of the text after the colon
snumforslice = text[colon+1:]
# Stripping the text taken
snum = snumforslice.strip()
# Printing the converted text to float
print(float(snum))