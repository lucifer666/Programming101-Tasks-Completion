def friday_years(start, end):
    leap_years = 0
    for year in range(start, end+1):
        if year % 4 == 0:
            # print(year)
            leap_years += 1
        # if year % 100 == 0:
        #     print(str(year)+"kur")
        #     leap_years -= 1
        # if year % 400 == 0:
        #     print(year)
        #     leap_years += 1
    return leap_years


print(friday_years(1000, 2000))
# print(friday_years(1753, 2000))
# print(friday_years(1990, 2015))ab