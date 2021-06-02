def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 == 1:
            return x 


print (find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
