# -*- coding: utf-8 -*-
"""per6_latihan4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
from abc import ABC, abstractmethod
class Bentuk(ABC):
  @abstractmethod
  def luas(self):
    return self.__sisi * self.__sisi

  @abstractmethod
  def keliling(self):
    return 4 * self.__sisi
class Persegi(Bentuk):
  def __init__(self,sisi):
    self.__sisi = sisi
  def luas(self):
    return self.__sisi * self.__sisi
  def keliling(self):
    return 4 * self.__sisi
persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())