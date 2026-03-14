# compute statistics for numbers 1–10.\

# intitalize variables. 
# or store information. 
# or start new state. 

total = 0
count = 0

for i in range(1,11):
    print("Numbers: ", i)

    # Update the state 
    total += 1
    count += 1

# compute averages
average = total / count 

print("results: ", total)
print("Average: ", average)

print("Total:", total)
print("Average:", average)

