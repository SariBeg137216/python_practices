"""
 create a third-string made of the first char
 of s1 then the last char of s2 Next,
 the second char of s1 and second last char of s2, and so on.
 Any leftover chars go at the end of the result.
"""


s1 = "Abc"
s2 = "Xyz"


res_s1 = s1.lstrip(s1[0] + s1[1])
rest_s2 = s2.rstrip(s2[-1] + s2[-2])
res_all = res_s1 + rest_s2

s3 = s1[0] + s2[-1] + s1[1] + s2[-2] + res_all
print(s3)