def pair_Avg(input):
    half = int(len(input)/2)
    output = []
    for i in range(half) :
        output.insert(i, (input[2*i] + input[2*i +1]) / 2)
    return output

