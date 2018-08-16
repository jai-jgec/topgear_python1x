import sys
lst=['MK14',56,23,'1','stg44',7.62,7.92]

search_element=sys.argv[1]

def is_present_in_list(s,l):
  for i in l:
    if i==s:
      return True
      break

result=is_present_in_list(search_element,lst)
if result==True:
  print(search_element,' is present in the list')
else:
  print(search_element,' is not present in the list!!!')
