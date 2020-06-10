playlist = []
#playlist.append(input("Paste your playlist below:\n"))
#a = len(playlist)
#print(a)
#print(playlist)
count = 0
with open("file.txt", 'r') as f:
    for line in f:
        count += 1
i = 0
f = open("file.txt", "r")
while i < count:
    playlist.append(f.readline(i))
    i += 1
print("You have {} songs in your playist".format(len(playlist)))
