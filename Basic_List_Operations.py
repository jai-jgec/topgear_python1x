def List():
  L = [1,2,3,4,5,6,7,8,9,0] # List with 10 elements
  for e in L:
    print e
  for e in L[1:len(L)-1]: #Slicing operation
    print e
  print L*100 # repeat 100 time 
  L2  =  ['a','b','c']
  print  L+L2  # List concatination



List()