def binary_search(dictionary, word):
    low = 0
    high = len(dictionary) - 1
    while low <= high:
        mid = (low + high) // 2
        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            low = mid + 1
        else:
            high = mid - 1
    return "Definisi tidak ditemukan."

dictionary = [
    ["Banana", "Buah pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

word_to_find = input("Masukan item yang ingin diterjemahkan : ")
definition = binary_search(dictionary, word_to_find)

if definition != "Definisi tidak ditemukan.":
    print("Definisi kata", word_to_find, "adalah:", definition)
else:
    print("Tidak ditemukan definisi kata", word_to_find)
