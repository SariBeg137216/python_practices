st1 = "America"
st2 = "Japan"


def first_mid_end(s1, s2):
    mid_s1 = len(s1)//2
    mid_s2 = len(s2)//2
    s3 = s1[0] + s2[0] + s1[mid_s1] + s2[mid_s2] + s1[-1] + s2[-1]
    print(s3)


first_mid_end(st1, st2)
