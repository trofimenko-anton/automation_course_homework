# # Если по заданию подразумевается, что входное число всегда будет от 1 до 12
def month_to_season(num_month):
    if 1 <= num_month <= 2:
        return "Зима"
    if 3 <= num_month <= 5:
        return "Весна"
    if 6 <= num_month <= 8:
        return "Лето"
    if 9 <= num_month <= 11:
        return "Осень"
    if 12 <= num_month:
        return "Зима"
# Если не гарантируется, что аргумент будет от 1 до 12
# def month_to_season(num_month):
#     if num_month == 12 or 1 <= num_month <= 2:
#         return "Зима"
#     elif 3 <= num_month <= 5:
#         return "Весна"
#     elif 6 <= num_month <= 8:
#         return "Лето"
#     elif 9 <= num_month <= 11:
#         return "Осень"
#     else:
#         return "Некорректный номер месяца"


num_month = int(input("Введите номер месяца: "))
print(month_to_season(num_month))
