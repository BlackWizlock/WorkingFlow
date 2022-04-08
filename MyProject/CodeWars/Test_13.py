def solution(digits):
    max_digit = digits[0:5]
    for five_digit in range(0, len(digits)-4):
        max_digit = max(int(max_digit), int(digits[five_digit:five_digit+5]))
    return max_digit


number_test = "1234567898765"
print(solution(number_test))
