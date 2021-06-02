def DNA_strand(dna):
    ans = ""
    for x in dna:
        if x == "A":
            ans += "T"
        if x == "T":
            ans += "A"
        if x == "C":
            ans += "G"
        if x == "G":
            ans += "C" 
    return ans

print (DNA_strand("GTAT"))