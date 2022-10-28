#You are given some information about N people. Each person has a first name, last name, age and sex. 
#Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first.
#For two people of the same age, print them in the order of their input.

N = int(input())
l = []
for i in range(N):
    L = raw_input().split()
    L[2] = int(L[2])
    l.append(L)
l.sort(key=lambda x: x[2])
for i in l:
    if i[3]=='M':
        print "Mr.", i[0], i[1]
    else:
        print "Ms.", i[0], i[1]
        
#Sample Input
#3
#Mike Thomson 20 M
#Robert Bustle 32 M
#Andria Bustle 30 F

#Sample Output
#Mr. Mike Thomson
#Ms. Andria Bustle
#Mr. Robert Bustle
