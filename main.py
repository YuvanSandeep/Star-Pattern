"""
*
* *
* * *
* * * *
"""

print ("*")
print ("* *")
print ("* * *")
print ("* * * *")
print ("=================================")
for i in range(1,10):
    for j in range(i):
        print ("* ", end = "")
    print ()

print ("=====================================")

print ("* * * *")
print ("* * *")
print ("* *")
print ("*")

for i in range(4,0,-1):
    for j in range(i):
        print ("* ", end = "")
    print ()

print ("=============================================")

print ("     *")
print ("   * *")
print (" * * *")

print ("===============")

for i in range(3,0,-1):
    for j in range(i):
        print (" "*i, end = "")

    print (" *"* i)

"""
     *
   *  *
  *  *  *
 *  *  *  *
"""
print ("====================================")
for i in range (4,0,-1):
    for j in range (i):
        print 




'''
    *
  * *
* * *
'''
n = 4
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end = " ")
    print("* "*(n-i), end="") 
    if (n-i == 0):
        print("*", end="")
    for j in range(i, 0, -1):
        print("", end = "")
    print("* "*(n-i))
