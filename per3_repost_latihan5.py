# -*- coding: utf-8 -*-
"""per3_repost_latihan5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 5. Class Mahasiswa

class Mahasiswa:
  def __init__(self,nama,nim,prodi,thn_masuk):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin','10120371','sistem Informasi',2020)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)