import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original

duplicates = []

names_set = set(names_1)

for name in names_2:
    if name in names_set:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# stretch

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

stretch_duplicates = []

for name in names_2:
    if name in names_1:
        stretch_duplicates.append(name)

end_time = time.time()
print (f"{len(stretch_duplicates)} duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
print (f"Stretch runtime: {end_time - start_time} seconds")