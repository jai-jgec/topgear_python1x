def String(Str):
  L = []
  L = Str
  for e in L:
    print e
  Str_sub = ''
  for e in L[1:len(Str)-1]:
    Str_sub = Str_sub + e
  print Str_sub  # Sub string
  print Str_sub*100 # repeat 100 time 
  Str2 = str(raw_input("Enter String: "))
  Str2 =  Str_sub + Str2 # String concatination
  print   Str2



String("asdzxc")