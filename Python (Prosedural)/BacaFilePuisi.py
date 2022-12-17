f = open("puisi.txt", 'r')
# baris = f.readline()
# while(baris):
#     print(baris.rstrip())
#     baris = f.readline()

# print("")
baris = f.readlines()
for i in range (len(baris)):
    baris[i] = baris[i].rstrip()
print(baris)
f.close()