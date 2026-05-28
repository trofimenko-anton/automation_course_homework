def is_year_leap(year):
    return "Високосный год" if year % 4 == 0 else "Невисокосный год"


test_year = int(input("Введите год: "))
result = is_year_leap(test_year)

print(f"Год {test_year}: {result}")
