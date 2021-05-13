s1 = "Ault"
s2 = "Kelly"

mid_str1 = len(s1) // 2


s3 = s1[:mid_str1:] + s2 + s1[mid_str1:]
print(s3)