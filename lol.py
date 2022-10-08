
1 задача
#n = str(input())
#print(len(n))

2 задача
#n = str(input())
#print(n[::-1])

3 задача
n = input()
m = n.find("'")
p = n.find("'", n.find("'") +1, -1)
h = n[m + 1:p]
#print(h)

4 задача
n = "23 456"
m = n.find(" ")
print(n[m+1:], n[:m])

5 задача
n = "ivan@lents.ru"
m = n.find(("@"))
print(n[:m])

6 задача
n = "7(918) 234-56-78"
n = n.replace("(", "", 1)
n = n.replace(")", "", 1)
n = n.replace("-", "", 2)
n = n.replace(" ", "", 1)
print(n)

7 задача 
n = "Hello world!"
m = n.find(" ")
a = n[:m]
g = "\n" + n[m+1:]
print(a, g)

8 задача
n = "zxcv737vcxz"
m = len(n)//2
a = n[:m]
q = n[m+1:]
d = q[::-1]
if a==d:
    print('yes')
else:
    print('no')
