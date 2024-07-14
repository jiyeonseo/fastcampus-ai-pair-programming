import random

def create_math_problem(N):
    for _ in range(N):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])

        if operator == '+':
            print(f"{num1} + {num2} = ?")
        elif operator == '-':
            # 뺄셈의 경우, 결과가 음수가 되지 않도록 큰 수에서 작은 수를 뺍니다.
            if num1 < num2:
                num1, num2 = num2, num1
            print(f"{num1} - {num2} = ?")
        elif operator == '*':
            print(f"{num1} * {num2} = ?")
        else:  # operator == '/'
            # 나눗셈의 경우, 0으로 나누는 것을 방지합니다.
            if num2 == 0:
                num2 = 1
            print(f"{num1} / {num2} = ?")

# 문제 생성
N = int(input("Enter the number of problems to generate: "))
create_math_problem(N)
