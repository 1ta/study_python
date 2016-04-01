#infile = open("input.txt","r")
#outfile = open("output.txt","w")

#oneline = infile.readline()
#print(oneline)

#for line in infile:
#    outfile.write(line)

#print(line)

fd = open("Harry Potter 1.txt")
fd.tell()
for line in fd:
    pass
fd.seek(0)
fd.seek(-30,2)
fd.readline()
print (fd.readline())
