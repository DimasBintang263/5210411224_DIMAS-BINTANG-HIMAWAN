# -*- coding: utf-8 -*-
"""per4_repost_latihan6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 6. class mobil(private)"""

#variabel bersifat private
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self.__jendela=jendela
    self.__pintu=pintu
    self.__mesin=mesin

audi=Mobil(4,5,"diesel")
audi._Mobil__mesin