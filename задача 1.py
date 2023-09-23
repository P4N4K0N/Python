import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
 
result = 0
for a in s:
    if a in j:
        result += 1
 
print(result)
