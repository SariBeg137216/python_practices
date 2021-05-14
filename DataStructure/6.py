""" Given the following two sets find the intersection and remove those elements from the first set"""
First_Set = {65, 42, 78, 83, 23, 57, 29}
Second_Set = {67, 73, 43, 48, 83, 57, 29}

inter_section = First_Set.intersection(Second_Set)
print(First_Set.difference(inter_section))

