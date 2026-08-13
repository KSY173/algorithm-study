"""
Time Complexity Examples

01. O(1)
02. O(N)
03. O(3N) -> O(N)
04. O(N^2)
05. Best / Worst case of linear search
06. Estimate operation counts
"""

import math


# --------------------------------------------------
# 1. O(1) - Constant Time
# --------------------------------------------------

def constant_time(arr):
    """데이터 크기와 관계없이 한 번만 접근한다."""
    return arr[0]


# --------------------------------------------------
# 2. O(N) - Linear Time
# --------------------------------------------------

def linear_time(n):
    """반복문이 N번 실행된다."""
    count = 0

    for _ in range(n):
        count += 1

    return count


# --------------------------------------------------
# 3. O(3N) -> O(N)
# --------------------------------------------------

def three_linear_loops(n):
    """
    각각 N번씩 실행되는 반복문이 3개 있다.

    실제 연산 횟수: 약 3N
    Big O: O(N)
    """
    count = 0

    for _ in range(n):
        count += 1

    for _ in range(n):
        count += 1

    for _ in range(n):
        count += 1

    return count


# --------------------------------------------------
# 4. O(N^2) - Quadratic Time
# --------------------------------------------------

def quadratic_time(n):
    """
    N번 반복하는 반복문 안에서
    다시 N번 반복한다.

    N * N = N^2
    """
    count = 0

    for _ in range(n):
        for _ in range(n):
            count += 1

    return count


# --------------------------------------------------
# 5. Linear Search
# --------------------------------------------------

def linear_search(arr, target):
    """
    앞에서부터 target을 탐색한다.

    Best Case  : 첫 번째에서 발견 -> Ω(1)
    Worst Case : 마지막에서 발견 -> O(N)
    """
    count = 0

    for value in arr:
        count += 1

        if value == target:
            return count

    return count


# --------------------------------------------------
# 6. 입력 크기에 따른 예상 연산량 비교
# --------------------------------------------------

def estimate_operations(n):
    """
    강의에서 비교한 O(N^2)와 O(N log N)의
    예상 연산량을 계산한다.
    """

    n_squared = n ** 2
    n_log_n = n * math.log2(n)

    print(f"N              : {n:,}")
    print(f"O(N^2)         : {n_squared:,.0f}")
    print(f"O(N log N)     : {n_log_n:,.0f}")


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    n = 10

    print("O(N)")
    print("operation count:", linear_time(n))

    print("\nO(3N) -> O(N)")
    print("operation count:", three_linear_loops(n))

    print("\nO(N^2)")
    print("operation count:", quadratic_time(n))

    data = list(range(1, 101))

    print("\nLinear Search - Best Case")
    print("operation count:", linear_search(data, 1))

    print("\nLinear Search - Worst Case")
    print("operation count:", linear_search(data, 100))

    print("\nN = 1,000,000")
    estimate_operations(1_000_000)