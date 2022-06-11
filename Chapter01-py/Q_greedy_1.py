n = int(input()) # 총 인원 수
data = list(int,input().split()) # 공포도를 받는다.(인원수별로)

data.sort() # 공포도별로 사람을 그룹에 포함시키기 위해서 최소값부터 정렬 , 최대한 많은 그룹이 구성되어야함

group_count = 0 #그룹의 숫자를 0으로 초기화
people_count = 0 #그룹원의 숫자를 0으로 초기화

# 1,1,2,2,3
for i in data : #공포도를 낮은 것부터 하나씩 확인
  people_count += 1 #현재 그룹에 해당 모험가를 포함시키기
  if people_count >= i : #현재 그룹에 포함된 사람의 수가 현재 공포도 이상이라면 그룹
    group_count += 1
    people_count = 0 # 현재 그룹에 포함된 사람의 수 초기화

print(group_count)
