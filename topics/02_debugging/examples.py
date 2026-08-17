"""
Debugging Practice

Practice finding logical errors using:
- Breakpoints
- Step-by-step execution
- Variable inspection
"""


# --------------------------------------------------
# 1. Variable Initialization Error
# --------------------------------------------------

def initialization_error():
    """
    문제:
    각 테스트 케이스의 합을 독립적으로 계산해야 한다.

    예상 결과:
    10
    10
    10

    실제 결과가 왜 다르게 나오는지
    디버거를 이용해 answer 값을 확인해보자.
    """

    answer = 0

    for test_case in range(3):

        for i in range(5):
            answer += i

        print(f"Test {test_case + 1}: {answer}")


# --------------------------------------------------
# 2. Range Error
# --------------------------------------------------

def range_error():
    """
    문제:
    numbers의 모든 값을 출력하려고 한다.

    실제로 모든 값이 출력되는지 확인한다.
    """

    numbers = [10, 20, 30, 40, 50]

    for i in range(4):
        print(numbers[i])


# --------------------------------------------------
# 3. Wrong Variable Error
# --------------------------------------------------

def wrong_variable_error():
    """
    문제:
    현재 테스트 케이스 번호를 출력하려고 한다.

    예상:
    Test 1
    Test 2
    Test 3
    """

    test_count = 3

    for t in range(1, test_count + 1):
        print("Test", test_count)


# --------------------------------------------------
# 4. Type / Division Error
# --------------------------------------------------

def division_error():
    """
    문제:
    두 수를 나눈 몫을 정수 형태로 출력하려고 한다.

    예상:
    5

    실제 출력값과 자료형을 확인한다.
    """

    answer = 10 / 2

    print("value:", answer)
    print("type :", type(answer))


# --------------------------------------------------
# 5. Division Operators
# --------------------------------------------------

def division_operators():

    a = 5
    b = 2

    print("a / b  =", a / b)
    print("a // b =", a // b)
    print("a % b  =", a % b)


# --------------------------------------------------
# Run
# --------------------------------------------------

if __name__ == "__main__":

    print("1. Initialization Error")
    initialization_error()

    print("\n2. Range Error")
    range_error()

    print("\n3. Wrong Variable Error")
    wrong_variable_error()

    print("\n4. Division Error")
    division_error()

    print("\n5. Division Operators")
    division_operators()