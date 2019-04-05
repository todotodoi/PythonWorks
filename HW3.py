'''
단어를 입력하면
거꾸로 출력해주는 프로그램입니다

'''

print("단어를 입력하면 거꾸로 출력해주는 프로그램입니다.\n")
print("거꾸로 쓰고 싶은 말을 적어주세요: ", end='')

word = input()
back = ""

for n in word:
    back = n + back

print ("\n결과입니다:",back)

input("\n\n창에서 나가려면 엔터키를 눌러주세요.")
