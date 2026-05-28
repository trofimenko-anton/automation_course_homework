from address import Address
from mailing import Mailing

from_address = Address(
    "188800",
    "Выборг",
    "Ленинградское шоссе",
    "10",
    "66"
)

to_address = Address(
    "195009",
    "Санкт-Петербург",
    "Арсенальная наб.",
    "3",
    "25"
)

mailing = Mailing(
    to_address,
    from_address,
    1520,
    "TRACK-092564"
)

print(f"Отправление {mailing.track} "
      f"из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - "
      f"{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
