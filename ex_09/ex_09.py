fname = input("Enter File name: ")
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retrieve/create/update counter
        di[word] = di.get(word, 0) + 1

# print(di)

# now we want to find the most common words

theword = None
largest = -1
for k, v in di.items():
        if v > largest:
            largest = v
            # capture/ remember the key that was largest
            theword = k

print(theword, largest)
