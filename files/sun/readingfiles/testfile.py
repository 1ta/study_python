#testfiles = open("temp.txt","r") # "r" means "reading"
#aLine = testfiles.readline()
#for line in testfiles:
#    print (line)

datafile = open("temp2.txt","w")
#if file do not exit, it will creat
#"w" means writing and delete old content
#"a" means writing at the end of old content
s = "first line \nsecond line"
datafile.write(s) #write string to the file
datafile.close()
