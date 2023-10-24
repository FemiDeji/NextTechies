file_name = open("ProjectOne.py", "r")
count = 0
for line in file_name:
        words = line.split(" ")
        count += len(words)
print("Number of words is: ",)
print(count)