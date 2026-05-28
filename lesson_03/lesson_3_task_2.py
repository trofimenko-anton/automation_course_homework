from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25", "+799567165"),
    Smartphone("Asus", "E-240", "794369554"),
    Smartphone("iPhone", "17Pro", "791055300"),
    Smartphone("Honor", "Ultra-A", "791868077"),
    Smartphone("Xiaomi", "Redmi Note 8T", "793474038")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
