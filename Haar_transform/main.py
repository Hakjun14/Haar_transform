import math
import haar_transform

lst = input("리스트를 입력하세요 : ")
lst = lst.split()
lst = list(map(int, lst))

n = math.log2(len(lst))

if n % 1 != 0 : exit("not a type INT!")

result = haar_transform.Haar_transform(lst, n)
print(result)

