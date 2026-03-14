day1 = 2
day2 = 3
day3 = 4
day4 = 1
day5 = 5
day6 = 3
day7 = 2

total = 0
highest = 0

for i in range(1,8):
    if i <  1 or i > 7:
        break
    day = globals()[f"day{i}"]
    if day > highest:
        highest = day
        highest_day = f"day{i}"
    total += day
else:
    average_hours = total/i
print("studied for:",total, "hours")
print("Studied", average_hours,"hours on average")
print(f"{highest_day} is the day where you studied maximum")
