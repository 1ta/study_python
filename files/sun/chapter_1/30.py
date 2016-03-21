import time

ISOTIMEFORMAT="%Y-%m-%d %X"   # %X represent clocktime can be deleted 
D = time.strftime( ISOTIMEFORMAT,time.localtime(time.time()))

print ("Today's date is:",D)
