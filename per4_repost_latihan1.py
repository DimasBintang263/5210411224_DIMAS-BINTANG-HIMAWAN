# -*- coding: utf-8 -*-
"""per4_repost_latihan1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 1. class segitiga


class segitiga:
  def __init__(self,alas,tinggi):
    self.alas = alas
    self.tinggi = tinggi
    self.luas = 0.5 * alas * tinggi

segitiga_besar = segitiga(100,80)
print("alas: ",segitiga_besar.alas)
print("tinggi:",segitiga_besar.tinggi)
print("luas: ",segitiga_besar.luas)