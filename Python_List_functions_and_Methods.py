EmpId = [1,2,3,4,5,6,7,8,9,0]
EmpName = ['aas','bde','dec','dd','eds','fdd','grf','hrg','igt','jgt']
for e in EmpName:
  print e
i = input("Enter number less than 10: ")  
if i<10:
  print EmpId[i],EmpName[i]
for e in EmpName[3:9]:
  print e
for e in EmpName[2:]:
  print e
print EmpId+EmpName

Empname = ['aas','bde','dec','dd','eds']
i = raw_input("Enter a name :")
if i in Empname: #using in operator
  print "present"
else:
 print "not present"   
for e in Empname:  #not using in operator
  if (i == e):
    print "present"
    break
else:
  print "not present"    

for i in range(0,len(Empname)):
  print Empname[len(Empname)-1-i]


