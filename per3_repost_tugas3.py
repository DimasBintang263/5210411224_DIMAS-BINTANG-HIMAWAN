# -*- coding: utf-8 -*-
"""per3_repost_tugas3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 3. Kelas Buku

class Buku: 
  def __init__(self,judul,pengarang,tahun_terbit,harga,rating):
    self.judul = judul 
    self.pengarang = pengarang
    self.tahun_terbit = tahun_terbit
    self.harga = harga
    self.rating = rating

buku1 = Buku('Tenggelamnya Kapal Van Wijck','HAMKA',1938,50000,7)
buku2 = Buku('Berani tidak disukai','Ichiro kishimi',2019,25000,8)
buku3 = Buku('Catatan harian sang pembunuh','Kim young-ha',2013,75000,9)

daftarbuku = [buku1,buku2,buku3]
print('''Daftar Buku''')
for buku in daftarbuku:
  t = '- buku {} karangan {} diterbitkan tahun {} memiliki harga {} dengan rating {}' .format(
      buku.judul,buku.pengarang,buku.tahun_terbit,buku.harga,buku.rating)
  print()
  print(t)