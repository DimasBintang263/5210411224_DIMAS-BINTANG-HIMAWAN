# -*- coding: utf-8 -*-
"""per6_latihan6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
class Segiempat():
  def __init__(self, panjang, lebar):
    self.panjang=panjang
    self.lebar=lebar
  def hitungLuas(self): # Method Overriding
    print("Luas Segiempat =", self.panjang* self.lebar, "m^2")
class Bujursangkar(Segiempat):
  def __init__(self,sisi):
    self.side=sisi
    Segiempat.__init__(self,sisi,sisi)
  def hitungLuas(self): # Method Overriding
    print("Luas Bujur sangkar =", self.side*self.side, "m^2")
b=Bujursangkar(4)
s=Segiempat(2,4)
b.hitungLuas()
s.hitungLuas()