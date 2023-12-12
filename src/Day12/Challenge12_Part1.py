def sol(a,b):
  if a == "":
    return 1 if b == () else 0

  if b == ():
    return 0 if "#" in a else 1

  res = 0

  if b[0] in ".?":
    res += sol(a[1:], b)

  if a[0] in "#?":
    if b <= len(a) and "." not in a[:b[0]] and (b[0] == len(a) or a[b[0]] != "#"):
      res += sol(a[b[0] + 1:], b[1:])
    else:
      res += 0
      
  return res

ans = 0;

for line in open(0):
  a, b = line.split()
  b = tuple(map(int, b.split(",")))
  ans += sol(a, b)

print(ans)
  
  
