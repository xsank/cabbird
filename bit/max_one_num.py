def count_max_one(num=0):
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count
