# mini_project_asd

Program ini berfungsi untuk membantu admin untuk mengelola data siswa berprestasi di SMAN 1 BeHemat Wakanda. Program ini mengimplementasikan konsep linked list dalam paradigma pemrograman berorientasi objek (OOP) di Python. Program juga menggunakan library PrettyTable untuk menampilkan data dengan lebih rapi.

Program terdiri dari beberapa bagian yaitu:

Bagian definisi variabel, class dan fungsi yang akan digunakan di program.

User: berisi informasi username dan password untuk login user.
Siswa: class ini berfungsi untuk menyimpan data siswa, seperti nama, kelas, prestasi, dan tingkat.
RiwayatSiswa: class ini berfungsi untuk mengelola data siswa dalam bentuk linked list. Ada beberapa metode yang didefinisikan di dalam kelas ini, seperti untuk menambahkan siswa, menghapus siswa, dan menampilkan riwayat siswa.
tabel_siswa: variabel ini berisi field yang akan ditampilkan menggunakan library PrettyTable.
login_user(): fungsi ini akan menampilkan tampilan login user, dimana user harus memasukkan username dan password yang telah didefinisikan di variabel user.
menu(): fungsi ini menampilkan tampilan pilihan menu yang tersedia di program.
pilihan(): fungsi ini berisi logika program utama, dimana user dapat memilih pilihan menu yang tersedia.
Bagian utama program:

pertama-tama program akan meminta user untuk melakukan login dengan memanggil fungsi login_user().
setelah login berhasil, program akan menampilkan menu pilihan dengan memanggil fungsi menu().
jika user memilih pilihan 1, program akan meminta user untuk memasukkan data siswa dan akan menyimpan data siswa tersebut ke dalam linked list dengan memanggil metode tambah_siswa() dari kelas RiwayatSiswa.
jika user memilih pilihan 2, program akan meminta user untuk memasukkan nama siswa yang ingin dihapus dan akan menghapus data siswa tersebut dari linked list dengan memanggil metode hapus_siswa() dari kelas RiwayatSiswa.
jika user memilih pilihan 3, program akan menampilkan riwayat siswa yang telah disimpan di dalam linked list dengan memanggil metode lihat_riwayat() dari kelas RiwayatSiswa.
jika user memilih pilihan 4, program akan keluar.
