'''
0이상 100이하의 숫자가
90점 이상이면 A 출력,
80점 이상이면 B 출력,
70점 이상이면 C 출력,
그 외에는 전부 F 출력하는 프로그램

'''

print("등급을 알려주는 프로그램입니다.\n")
print("0이상 100 이하의 실수를 입력해주세요: ", end = '')

grade = input()
grade = float(grade)

if(grade > 100):
    print("\n0이상 100이하의 실수가 아닙니다.")
elif(grade >= 90):
    print("\n",grade,"점은 A등급 입니다.")
elif (grade >= 80):
    print("\n",grade,"점은 B등급 입니다.")
elif (grade >= 70):
    print("\n",grade,"점은 C등급 입니다.")
else:
    print("\n",grade,"점은 F등급 입니다.")

input("\n\n창에서 나가려면 엔터키를 눌러주세요.")
