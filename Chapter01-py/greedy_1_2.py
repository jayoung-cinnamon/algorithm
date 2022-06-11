n,m = map(int,input().split())
result = 0
for i in range(n):
  data = list(map(int,input().split()))
  min_value = min(data)
  max_value = max(min_value)
  result = max_value

print(result)