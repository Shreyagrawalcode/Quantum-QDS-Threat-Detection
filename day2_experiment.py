measurements = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
zero =0
one =0
total = len(measurements)
print ("===== MEASUREMENT ANALYSIS =====")
print ("Total measurements: " , total)

for i in measurements:
    if i==0:
        zero +=1
    elif i==1:
        one +=1
print("zero: " ,zero)
print ("one: ", one)

zero_prob = (zero/total)*100
one_prob = (one/total)*100
print("Zero_prob: ",zero_prob)
print("One_prob: ",one_prob)

if zero_prob>70:
    print ("Status: Unusual")
else:
    print ("Status: Normal")