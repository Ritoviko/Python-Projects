month = int(input("Enter your birth month (in number): "))
day = int(input("Enter your birth day: "))

if month <=12 and month >=1:
    if month != 2:
        if day <=31 and day >=1:
            n = day%10
            m = day//10
            day_num = n+m

            x = month%10
            y = month // 10
            month_num = x+y
            sum1 = day_num+month_num
            while sum1>9:
                s_a = sum1%10
                s_b = sum1//10
                sum1 = s_a+s_b
            print ("Your numerology number is : ", sum1)
        else:
            print("invalid day input")
    elif month==2:
        if day <=28 and day >=1:
            n = day%10
            m = day//10
            day_num = n+m

            x = month%10
            y = month // 10
            month_num = x+y
            print("Your numerology number is: ", day_num+month_num)
        else:
            print("invalid day input")
else:
    print("invalid month input")
