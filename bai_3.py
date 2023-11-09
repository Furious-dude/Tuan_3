a = 0
x= int(input())
for i in range(10):
    a=a + pow(10,i)
    if x - a == 0:
        print("tieu duoc")
    else:
        print("khong duoc")