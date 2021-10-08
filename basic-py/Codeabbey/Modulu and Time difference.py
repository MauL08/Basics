loop = int(input())
for i in range(loop):
    day1, hours1, minute1, second1, day2,hours2,minute2,second2 = [int(x) for x in input().split()]

    sum1 = ((day1 * 86400) + (hours1 * 3600) + (minute1 * 60) + second1)
    sum2 = ((day2 * 86400) + (hours2 * 3600) + (minute2 * 60) + second2)

    sum = sum2 - sum1

    day = sum/86400
    sum %= 86400
    day = int(day)

    hours = sum/3600
    sum %= 3600
    hours = int(hours)

    minute = sum/60
    sum %= 60
    minute = int(minute)

    second = sum
    second = int(second)

    print('(',day,' ',hours,' ',minute,' ',second,')',' ',sep='')
