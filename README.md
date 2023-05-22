Percobaan 10
Fungsi binary_search_rotation menerima satu argumen data, yang merupakan daftar yang dirotasi secara siklik.
Inisialisasi low dengan 0, yang merupakan indeks terendah dalam daftar.
Inisialisasi high dengan len(data) - 1, yang merupakan indeks tertinggi dalam daftar.
Masuk ke dalam loop while low < high untuk melakukan pencarian biner.
Hitung mid sebagai indeks tengah antara low dan high dengan menggunakan operator pembagian bulat (//).
Periksa apakah data[mid] lebih besar dari data[high]. Jika ya, berarti rotasi terjadi setelah indeks mid. Oleh karena itu, setel low menjadi mid + 1.
Jika data[mid] tidak lebih besar dari data[high], berarti rotasi terjadi sebelum atau pada indeks mid. Oleh karena itu, setel high menjadi mid.
Setelah loop selesai, low akan menjadi indeks rotasi terkecil.
Di luar fungsi, daftar my_list diinisialisasi dengan (6, 7, 8, 9, 1, 2, 3, 4, 5).
Panggil fungsi binary_search_rotation dengan argumen my_list untuk mendapatkan indeks rotasi terkecil.
Cetak hasil menggunakan f-string dengan teks "Indeks rotasi terkecil adalah " diikuti oleh nilai rotation_index.
Hasil eksekusi program ini akan mencetak "Indeks rotasi terkecil adalah 4", karena elemen terkecil dalam daftar berada pada indeks 4 setelah rotasi

Percobaan 11
Fungsi find_most_frequent_element menerima satu argumen data, yang merupakan daftar elemen.
Inisialisasi kamus counts untuk menyimpan jumlah kemunculan setiap elemen dalam daftar.
Inisialisasi most_frequent dengan None untuk menyimpan elemen yang paling sering muncul.
Inisialisasi max_count dengan 0 untuk menyimpan jumlah kemunculan maksimum yang telah ditemukan.
Loop melalui setiap elemen num dalam data.
Periksa apakah num sudah ada dalam kamus counts. Jika ya, tambahkan 1 ke jumlah kemunculan counts[num].
Jika num belum ada dalam kamus counts, setel jumlah kemunculan counts[num] menjadi 1.
Periksa apakah jumlah kemunculan counts[num] lebih besar dari max_count. Jika ya, setel max_count menjadi counts[num] dan most_frequent menjadi num.
Setelah loop selesai, most_frequent akan berisi elemen yang paling sering muncul dalam daftar.
Di luar fungsi, daftar my_list diinisialisasi dengan [2, 2, 2, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8].
Panggil fungsi find_most_frequent_element dengan argumen my_list untuk mendapatkan elemen yang paling sering muncul.
Cetak hasil menggunakan f-string dengan teks "Elemen yang paling sering muncul adalah " diikuti oleh nilai most_frequent_element.
Hasil eksekusi program ini akan mencetak "Elemen yang paling sering muncul adalah 8", karena elemen 8 muncul paling sering dalam daftar.

Percobaan 12
Fungsi binary_search menerima dua argumen: data yang merupakan daftar terurut secara menaik, dan target yang merupakan elemen yang ingin dicari dalam daftar.
Inisialisasi low dengan 0, yang merupakan indeks terendah dalam daftar.
Inisialisasi high dengan len(data) - 1, yang merupakan indeks tertinggi dalam daftar.
Masuk ke dalam loop while low <= high untuk melakukan pencarian biner.
Hitung mid sebagai indeks tengah antara low dan high dengan menggunakan operator pembagian bulat (//).
Periksa apakah data[mid] sama dengan target. Jika ya, berarti elemen target ditemukan, dan kembalikan mid sebagai indeks elemen tersebut.
Jika data[mid] lebih kecil dari target, berarti elemen target berada di sebelah kanan mid. Oleh karena itu, setel low menjadi mid + 1.
Jika data[mid] lebih besar dari target, berarti elemen target berada di sebelah kiri mid. Oleh karena itu, setel high menjadi mid - 1.
Jika loop selesai tanpa menemukan target, kembalikan -1 untuk menandakan bahwa target tidak ditemukan dalam daftar.
Di luar fungsi, daftar names diinisialisasi dengan ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'George'].
Meminta pengguna untuk memasukkan nama yang ingin dicari melalui input.
Panggil fungsi binary_search dengan argumen names dan target_name untuk mencari indeks dari nama yang diinginkan.
Periksa apakah index tidak sama dengan -1. Jika ya, cetak "Nama ditemukan pada indeks" diikuti oleh nilai index.
Jika index sama dengan -1, cetak "Nama tidak ditemukan".
Pada saat eksekusi program, pengguna diminta untuk memasukkan nama yang ingin dicari. Jika nama tersebut ada dalam daftar names, program akan mencetak "Nama ditemukan pada indeks X", di mana X adalah indeks nama tersebut dalam daftar. Jika nama tidak ditemukan, program akan mencetak "Nama tidak ditemukan".
