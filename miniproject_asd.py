# NAMA  : BAYU PURNAMA AJI
# NIM   : 2209116050
# KELAS : SISTEM INFORMASI A

# TUGAS MINI PROJECT ASD 3


import os
import time
from prettytable import PrettyTable

user ={"username":["admin"],
       "password":["111"] 
       }

# untuk mengakses pretttable untuk merapikan data
tabel_siswa =PrettyTable()
tabel_siswa =field_names=["Nama","Kelas","Prestasi","Tingkat"]


class Siswa:
    def __init__(self, nama, kelas, prestasi, tingkat):
        self.nama = nama
        self.kelas = kelas
        self.prestasi = prestasi
        self.tingkat=tingkat
        self.next = None
        
    def __str__(self):
        return f"Nama{self.nama}, Kelas{self.kelas}, Prestasi{self.prestasi}, Tingkat {self.tingkat}"

class RiwayatSiswa:
    def __init__(self):
        self.head = None

    def tambah_siswa(self, nama, kelas, prestasi, tingkat):
        siswa_baru = Siswa(nama, kelas, prestasi, tingkat)

        if self.head is None:
            self.head = siswa_baru
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = siswa_baru
            
    def hapus_siswa(self, nama, kelas):
        current = self.head
        previous =None
        while current:
            if current.nama:
                if previous:
                    previous.next = current.next
                else:
                    self.head =current.next
                    return True
                previous=current
                current=current.next
            return False
        
    
# def ini menjelaskan untuk menampilkan berbagai data yang telah dimasukan ke program linkedlist oop
    def lihat_riwayat(self):
            if self.head is None:
                print("Riwayat data siswa kosong")
            else:
                current = self.head
                data_list=[]
                while current is not None:
                    os.system("cls")
                    data_list.append([current.nama, current.kelas, current.prestasi, current.tingkat])
                    current = current.next
                    table = PrettyTable()
                    table.field_names= field_names
                    table.add_rows(data_list)
                    print(table)
                
                

namasiswa = RiwayatSiswa()

# fungsi dibawah ini ada sebuah sintax untuk melakukan login user sebelum memasuki program
def login_user():
    os.system("cls")
    while True:
        username         = input("silakan memasukan username Anda : ")
        password         = input("Silakan memasukan password Anda : ")
        try:
            login        = user.get("username").index(username)
            if username  == user.get("username")[login] and password == user.get("password")[login]:
                os.system('cls')
                break
            else:
                print("Password yang Anda Masukan Salah")
        except ValueError:
            print("Username yang Anda Masukan Salah")


# fungsi menampilkan sebuah tampilan pilihan untuk memilih opsi sintax
def menu():
    print('''
    ==============================================
    |  SISWA BERPRESTASI SMAN 1 BEHEMAT WAKANDA  |   
    |                MENU ADMIN                  |
    |=============================================
    |   SELAMAT DATANG PENYEDIA LAYANAN DIGITAL  |
    |                                            |          
    | 1. Menambahkan Daftar Riwayat Siswa        |
    | 2. Menghapus Daftar Riwayat SisWa          |
    | 3. Menampikan Daftar Riwayat Siswa         |
    | 4. Keluar                                  |
    ==============================================    
        ''')

# sebuah ruler untuk memasuki jalannya program dengan sebagai pilihan dalam memasukan opsi untuk user untuk menampilkan tampilan pilihan
def pilihan():
    login_user()
    menu()
    while True:
        choice = input("Masukan pilihan yang tersedia:")
        os.system("cls")
        if choice == "1":
            os.system("cls")
            print("===================================")
            print("MENAMBAHKAN DATA SISWA BERPRESTASI")
            print("===================================")
            print()
            nama    = input("Masukan nama siswa ditambahkan                 : ")
            kelas   = input("Masukan Kelas Siswa ditambahkan                : ")
            prestasi =input("Masukan Prestasi siswa ditambahkan             : ")
            tingkat = input("masukan tingkat prestasi siswa                 : ")
            namasiswa.tambah_siswa(nama, kelas, prestasi, tingkat)
            os.system("cls")
            print("Data siswa telah ditambahkan.")
            time.sleep(3)
            os.system("cls")
            menu()
            

        elif choice =="2":
            os.system("cls")
            print("===================================")
            print("MENGHAPUS DATA SISWA BERPRESTASI")
            print("===================================")
            print()
            
            nama1      = input("Masukan nama siswa yang dihapus                 :")
            namasiswa.hapus_siswa(nama1)
            os.system("cls")
            print("Data siswa telah dihapus.")
            time.sleep(3)
            os.system("cls")
            menu()
            
        elif choice =="3":
            namasiswa.lihat_riwayat()
            time.sleep(5)
            os.system("cls")
            menu()
        
        elif choice =="4":
            print("Anda keluar dari admin")
            time.sleep(3)
            os.system("cls")
            pilihan()


pilihan()