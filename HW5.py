'''
숫자를 입력받으면
역피라미드를 출력하는 프로그램

'''

print("역피라미드를 출력하는 프로그램입니다.\n")
row = input("행의 개수를 입력해주세요: ")

row = int(row)

for n in range(row,0,-1):
    print(" "*(row-n),"*"*(2*n-1)," "*(row-n))

input("\n\n창에서 나가려면 엔터키를 눌러주세요.")
