def is_unique_string(string):
    num=0
    for i in string:
        bit=1<<(ord(i)-97)
        if num&bit:
            return False
        num|=bit
    return True


print is_unique_string("hello")
print is_unique_string("world")

