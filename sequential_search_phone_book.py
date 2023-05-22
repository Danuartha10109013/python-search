def find_phone_number(name, names, phone_numbers):
    for i in range(len(names)):
        if names[i] == name:
            return phone_numbers[i]
    return "Nomor telepon tidak ditemukan."

names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"]
phone_numbers = ["081234567890", "089876543210", "087811223344", "082122232425"]

name_to_find = "Jane Smith"
phone_number = find_phone_number(name_to_find, names, phone_numbers)

if phone_number != "Nomor telepon tidak ditemukan.":
    print("Nomor telepon", name_to_find, "adalah:", phone_number)
else:
    print("Tidak ditemukan nomor telepon untuk", name_to_find)
