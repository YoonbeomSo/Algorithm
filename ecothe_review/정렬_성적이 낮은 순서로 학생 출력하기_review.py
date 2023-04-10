n=int(input())

#n명 학생의 정보를 입력받은 리스트
array = []
for i in range(n):
    input_data = input().split()
    #(이름, 성적)
    array.append((input_data[0],int(input_data[1])))

#람다식 사용으로 value 점수를 기준으로 정렬
#lambda [arguments] : [return 되는 expression 부분]
array = sorted(array, key=lambda student: student[1])

#정답 출력
for student in array:
    print(student[0], end=" ")