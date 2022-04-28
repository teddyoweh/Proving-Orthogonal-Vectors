
def IsOrthogonal(u,v):
  vu = u.split(',')
  vu =list(map(int,vu))
  vv = v.split(',')
  vv = list(map(int,vv))

 
  print(out)
  ians = (vu[0]*vv[0])+(vu[1]*vv[1])
  return ians == 0
IsOrthogonal('3,4','-8,6')