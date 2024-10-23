def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * (b // gcd(a, b))


def count_multiples(x, m):
    if x < 1:
        return 0
    return x // m


def count_not_divisible(L, R, N):
    from itertools import combinations

    numbers = list(range(2, N + 1))
    total_count = R - L + 1

    excluded_count = 0
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            lcm_value = combo[0]
            for num in combo[1:]:
                lcm_value = lcm(lcm_value, num)
            multiples_in_R = count_multiples(R, lcm_value)
            multiples_in_L_minus_1 = count_multiples(L - 1, lcm_value)
            excluded_count += (multiples_in_R - multiples_in_L_minus_1) * (-1 if r % 2 == 0 else 1)

    return total_count - excluded_count


def main():
    while True:
        input_line = input().strip()
        if input_line == "-1":
            break
        L, R = map(int, input_line.split())
        N = int(input().strip())

        result = count_not_divisible(L, R, N)
        print(result)


if __name__ == "__main__":
    main()

