'''
하나의 숫자를 입력받아서
홀수면 True 출력,
짝수면 False 출력하는 프로그램

'''

print("홀수 -> True\n 짝수 -> False\n")
print("숫자를 입력해주세요: ", end = '')

num = input()
num = int(num)


if (num%2 == 1):
    print("\n"True)
else:
    print("\n"False)

input("\n\n창에서 나가려면 엔터키를 눌러주세요.")

