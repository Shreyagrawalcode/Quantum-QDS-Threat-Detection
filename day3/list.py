measurements = [0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
length = len(measurements)
def count_one(measurements):
    count = 0
    for i in measurements:
        if i==1:
            count +=1
    return count
def count_zero(measurements):
    count = 0
    for i in measurements:
        if i==0:
            count +=1
    return count
probability_one_percent = count_one(measurements)/length*100
probability_zero_percent = count_zero(measurements)/length*100
print("No of one's :",count_one(measurements))
print("No of zero's :" ,count_zero(measurements))
print("probability of one:" , probability_one_percent)
print("probability of zero :",probability_zero_percent)