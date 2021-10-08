loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = float(b)

    BMI = a/(b**2)

    if BMI < 18.5:
        status = "under"
    if BMI >= 18.5 and BMI < 25.0:
        status = "normal"
    if BMI >= 25.0 and BMI < 30.0:
        status = "over"
    if BMI >= 30.0:
        status = "obese"

    print(status,' ',sep='')