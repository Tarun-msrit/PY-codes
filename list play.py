li=['mark','steve','rohit','markram','parthiv','sharma','barghav','smith','bravo']
li2=['rob5','starc','arno6ld','ha5ish','alonso','nik2il']
print(li[::2])
newli=li[::3]
newli2=[x.upper() for x in newli]
print(newli2)
newli3=(li[::-1])
print(newli3)
newli4=[]
for i in range(0,len(li)):
    print(li[i][::-1])
    newli4.append(li[i][::-1])
print(newli4)

new_list = [int(m) for n in li2 for m in n if m in '0123456789']
print(new_list)




n=int(input('enter the number of elements in the dictionary'))
d={}
for i in range(1,n+1):
    key=int(input("Enter key"))
    ndet=int(input("enter the number of details"))
    v=[]
    for j in range(0,ndet):
        u=raw_input("Enter details")
        v.append(u)
    d[key]=v

    print(d)

newdi=(keyvalue for (keyvalue) in d.items() if key%2==0)
print(newdi)