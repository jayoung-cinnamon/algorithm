#-*- coding: utf-8 -*-

n, k = map(int,input().split())
result = 0

while n >= k :
  while n % k !=0 :
    n -= 1
    result += 1
  #몫
  n //= k
  result += 1

#마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
  n -= 1
  result += 1
print(result)

