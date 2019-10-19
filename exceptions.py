try:
    f=open('simple.txt','w')
    f.write("Test write to simple text!")
except:
    print("ERROR:cant read data")
else:
    print("SUCCESS!")
    f.close()

finally:
    print("HELLO WORLD")