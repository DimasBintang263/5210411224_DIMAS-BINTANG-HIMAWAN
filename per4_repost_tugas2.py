# -*- coding: utf-8 -*-
"""per4_repost_tugas2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 2. Kelas Mahasiswa

class Mahasiswa:
  def __init__(self,nama,nim,prodi,thn_masuk,alamat,umur):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.thn_masuk = thn_masuk
    self.alamat = alamat
    self.__umur = umur 

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,'bengkulu',19)
m2 = Mahasiswa('Dimas',2639236,'Informatika',2021,'tais',20)
m3 = Mahasiswa('Aldi',2485252,'Informatika',2021,'magelang',19)
m4 = Mahasiswa('Taher',17538175,'Hukum',2021,'madura',20)
m5 = Mahasiswa('Fahmi',23764672,'Hukum',2020,'Tais',19)
list_mahasiswa = [m1,m2,m3,m4,m5]
print(' DAFTAR MAHASISWA ')
for m in list_mahasiswa:
  teks = '{} adalah mahasiswa {} angkatan {} dengan nim {} dengan umur {} alamat {}'.format(
      m.nama,m.prodi,m.thn_masuk,m.nim,m._Mahasiswa__umur,m.alamat)
  print()
  print(teks)