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

tmp = list()
for k, v in di.items():
    newt = (v,k)
    tmp.append(newt)

# print("Flipped", tmp)
tmp = sorted(tmp, reverse=True)
# print("Sorted", tmp[:5])

for v, k in tmp[:5]:
    print(k,v)
