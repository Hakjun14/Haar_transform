import pair_avg
import pair_diff

def Haar_transform(input, n) :
    A = pair_avg.pair_Avg(input)
    D = pair_diff.pair_Diff(input)
    if n == 1 :
        return A + D
    else :
        n -= 1
        return Haar_transform(A, n) + D
