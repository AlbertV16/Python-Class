# Program to count bob
# Define variables
bobs = 0
count = 0
count2 = 2
s='bobobob'

# For loop to count bobs
while count2 < len(s):
    if s[count:count2+1] == 'bob':
        bobs +=1
    count += 1
    count2 +=1

# Print number of bobs
print('Number of times bob occurs is: ' + str(bobs))