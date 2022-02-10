

#튜플 선언 (소괄호)

fruits = ('사과','스타푸룻트','오렌지','블루베리','샤인머스켓','귤')

#튜플은 데이터를 수정할수없다

#튜플 조회

print(fruits[3])

#튜플 문제1)

for x in range(0,6):
    if x % 2 == 1:
        print(fruits[x])



score = ('A','A+','F','B','B','A+','F','A')

print(score.count('F'))

#아이템 정렬

ab = sorted(score)

print(type(ab))

ab = tuple(ab)

print(type(ab))


ab = list(fruits)

print(type(ab))

#튜플 슬라이싱 [n:m] n 인덱스부터 m-1 인덱스까지

Animals = ('호랑이','사자','곰','여우','늑대')

print (Animals[0: 3])
print (Animals[1: 4])
print (Animals[2: ])







