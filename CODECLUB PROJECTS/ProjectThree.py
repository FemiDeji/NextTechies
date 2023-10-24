#code to count the number of words in a text file
file_name = input("Enter file name: ")
count = 0
with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        count += len(words)
print("Number of words in text file: ")
print(count)
