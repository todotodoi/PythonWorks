'''
물건 가격과 할인율을 입력하면
할인된 가격을 알려주는 프로그램

'''

print("할인된 가격을 알려주는  프로그램입니다.\n")
price = input("물건 가격을 입력해주세요: ")
discount = input("\n할인율을 입력해주세요: ")

price = int(price)
discount = float(discount)
result = price*(100-discount)/100

if (discount >= 100):
    print("\n할인율을 확인해주세요.")
else:
    print("\n할인된 가격은",result,"원 입니다.")

input("\n\n창에서 나가려면 엔터키를 눌러주세요.")

