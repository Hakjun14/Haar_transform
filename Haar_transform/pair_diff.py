def pair_Diff(input):
    half = int(len(input) / 2)
    output = []
    i = 0
    while i < half :
        output.insert(i, (input[2 * i] - input[2 * i + 1]) / 2)
        i += 1
    return output