# -*- coding: utf-8 -*-
"""per4_repost_tugas1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 1. Kelas Menu

class Menu:
  def __init__(self,nama,deskripsi,harga,rating,tipe):
    self.nama = nama
    self.deskripsi = deskripsi
    self.harga = harga
    self.rating = rating
    self.__tipe = tipe

mnm1 = Menu('jus jambu','jus jambu merah tanpa gula',8500,8,'panas/dingin')
mnm2 = Menu('jus alpukat ori','jus alpukat dengan tambahan air gula merah',15000,7,'panas/dingin')
mnm3 = Menu('jus alpukat extra susu','jus alpukat dengan campuran susu coklat dan taburan kepingan choco',15000,10,'panas/dingin')
mnm4 = Menu('red & smooth','smoothie pisang susu dengan strawberry',175000,6,'dingin')
mnm5 = Menu('kopicap','kopi murah rasa starbucks',7000,10,'panas')
mnm6 = Menu('pop ice','minuman kelas dunia',50000,9,'dingin')

pilihan_minuman = [mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print('daftar menu Healthy Fruits')
for mn in pilihan_minuman:
  t = '{} harga Rp{}, {}, tipe: {}, rating: {}' .format(mn.nama,mn.harga,mn.deskripsi,mn._Menu__tipe,mn.rating)
  print()
  print(t)