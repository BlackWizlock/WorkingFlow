def count_bits(n):
    count = 0
    for bits in bin(n)[2:]:
        if bits == "1":
            count += 1
    return count

count_bits(9)
