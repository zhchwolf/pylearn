
# 元字符
# . * ? ^ $ / {} [] ()


x = [3, -1, -10, 2, 7]
greater_than_zero = filter(lambda n: (n > 0), x)

print(list(greater_than_zero))