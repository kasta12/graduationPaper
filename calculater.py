import sys
import os

operand1 = []
operand2 = []
operator = []
result = []
operation = 0

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

while 1:
    print("+-------------------+")
    print("l 1. 계산하기       l")
    print("l 2. 계산기록       l")
    print("l 3. 프로그램 종료  l")
    print("+-------------------+")

    while 1:
        n = input("원하시는 번호를 입력하세요: ")
        if n == '1' or n == '2' or n == '3':
            break
        else :
            print("올바른 번호를 입력하세요!")
            
    if n == '1':
        while 1:
            opd1 = input("첫번째 피연산자를 입력하세요: ")
            if isNumber(opd1):
                opd1 = float(opd1)
                break
            else:
                print("올바른 피연산자를 입력하세요!")
        while 1:
            opr = input("연산자를 입력하세요(+,-,*,/): ")
            if opr == '+' or opr == '-' or opr == '*' or opr == '/':
                break
            else:
                print("올바른 연산자를 입력하세요!")
        while 1:
            opd2 = input("두번째 피연산자를 입력하세요: ")
            if isNumber(opd2):
                opd2 = float(opd2)
                break
            else:
                print("올바른 피연산자를 입력하세요!")
                
        if opr == '+':
            res = opd1 + opd2
        elif opr == '-':
            res = opd1 - opd2
        elif opr == '*':
            res = opd1 * opd2
        elif opr == '/':
            res = opd1 / opd2
        print("계산결과: " + str(opd1) + " " + opr + " " + str(opd2) + " = " + str(res))

        operand1.append(opd1)
        operand2.append(opd2)
        operator.append(opr)
        result.append(res)
        operation += 1

    elif n == '2':
        i = 0
        if operation == 0:
            print("계산기록이 없습니다..")
        else:
            print("-------계산기록------")
            while i < operation :
                print(str(i+1) + ": " + str(operand1[i]) + " " + operator[i] + " " + str(operand2[i]) + " = " + str(result[i]))
                i += 1

    else:
        print("프로그램을 종료합니다!")
        sys.exit()
        
