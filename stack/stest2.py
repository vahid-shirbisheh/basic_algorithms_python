from stack import Stack


"""
To test the height property of the stack class 
"""

s = Stack()
l = [5,7,3,6,2,8]
for x in l:
    s.push(x)

while s.height >0:
    print(s.height)
    print(s)
    print(s.pop())
    print("--------------------------")

print(s)

ss = Stack()
print(ss)
