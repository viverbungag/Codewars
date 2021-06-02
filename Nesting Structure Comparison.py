def dim(a):
    if type(a) == list:
        for x in range(len(a)):
            if type (a[x]) == list:
                return [len(a)] + dim(a[x]) + [x]
        return [len(a)]

def same_structure_as(original,other):
    if dim(original) == dim(other):
        return True
    return False



print (same_structure_as([1,[1,1]],[2,[2,2]]))



