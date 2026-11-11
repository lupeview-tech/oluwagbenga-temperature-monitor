# Analyses a list of temperatures
def analyse(temps):
    highest = max(temps)
    lowest = min(temps)
    average = sum(temps) / len(temps)
    return highest, lowest, average

temperatures = []

# Collect 5 readings from the user
for i in range(5):
    while True:
# Keep asking until the user types a valid number.
        try:
            temp = float(input("Enter temperature: "))
            temperatures.append(temp)
            break
        except ValueError:
            print("Please type a number, not letters.")

# Call the function and print results
highest, lowest, average = analyse(temperatures)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Average temperature:", average)

# Count readings over the safe limit
count =0

# Check each reading against the safe limit
for temp in temperatures:
    if temp > 80:
        print("WARNING! Temperature is too high:", temp)
        count = count + 1
    else:
        print("ok:", temp)

print("Number of readings too high:",count)
