students = [
    {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3},
    {'no': 2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 1},
    {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 55, 'total': 255, 'avg': 85.0, 'rank': 4},
    {'no': 4, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': 5},
    {'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2}
]


# max : 최댓값을 찾아주는 함수
print(max(students,key = lambda x : x['no']))     # 'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2

# count (students 내에 count 최댓값 + 1 : 다음학생번호)
print(max(students,key = lambda x : x['no'])['no']+1) 
