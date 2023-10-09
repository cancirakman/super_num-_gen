#program 9 basamaklı bir sayı üretecek ve kendisine kadar olan sayı kendine bölünebilecek.
#ilk bir basamak bire ilk iki basamak ikiye ilk üç basamak üçe bölünecek ve böyle 9 a kadar gidecek ayrıca rakamlar farklı olmak zorunda.

import random


def num_gen(num):
    if int(num)%len(num-1):
        return True
    else:
        return False


nums = ["1","2","3","4","5","6","7","8","9"]
num = ""

while len(num)!=9:
    random_ = random.choice(nums)
    if num_gen(num + random_):
        num += random_
        nums = nums - random_
        


print(num)