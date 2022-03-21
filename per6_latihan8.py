# -*- coding: utf-8 -*-
"""per6_latihan8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zG9eArEEQhDZIRSidmrs-NnKMlqwqMaH

# 8. Implementasi Overriding Class Mahasiswa
"""

"""
Nama : Dimas Bintang Himawan
Nim :5210411224
"""
#Implementasi Overriding Class Mahasiswa
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
    def override(self) :
        print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}\n")
class Hitung(Mahasiswa) :
    def __init__(self, nama, nim, jmlhsks, sks) :
        super().__init__(nama, nim)
        self.jmlhsks = jmlhsks
        self.sks = sks

    #Override Method
    def override(self):
        totalsks = self.jmlhsks + self.sks

        if totalsks>=100 :
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Diperbolehkan mengambil skripsi\n")
        else :
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Tidak diperbolehkan mengambil skripsi\n")
mahasiswa1 = Mahasiswa("Eren", 123180015)
mahasiswa2 = Hitung("Mikasa", 123190007, 84, 22)
mahasiswa1.override()
mahasiswa2.override()