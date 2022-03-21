# -*- coding: utf-8 -*-
"""per5_repost_tugas2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pOOcuFjc5KXP3cim5koCfFL4D5PRyCs
"""

"""
Nama : Dimas Bintang Himawan
Nim : 5210411224
"""
# 2. Hierarchical Inheritance ComputerPart

class ComputerPart:
  def __init__(self, pabrikan, nama, harga) :
    self.pabrikan = pabrikan
    self.nama = nama    
    self.harga = harga

class Processor(ComputerPart) :
  def __init__(self, pabrikan, nama, harga) :
    self.pabrikan = pabrikan
    self.nama = nama 
    self.harga = harga
        
  def Tampil(self) : 
    print(f'{self.pabrikan} mengembangkan seri {self.nama} yang memiliki harga Rp.{self.harga}')

class RandomAccessMemory(ComputerPart) :
  def __init__(self, pabrikan, nama, harga, kapasitas) :
    self.pabrikan = pabrikan
    self.nama = nama
    self.harga = harga
    self.kapasitas = kapasitas

  def Tampil(self) : 
    print(f'Diproduksi oleh    :{self.pabrikan}')
    print('Spesifikasi: ')
    print(f'Seri      : {self.nama}')
    print(f'Kapasitas : {self.kapasitas}')
    print(f'Memiliki harga Rp.{self.harga}')

class HardDiskSATA(ComputerPart) :
  def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
    self.pabrikan = pabrikan
    self.nama = nama 
    self.harga = harga
    self.kapasitas = kapasitas
    self.rpm = rpm

  def Tampil(self) :
    print(f'Diproduksi oleh  :{self.pabrikan}')
    print(f'Nama produk      : {self.nama} ')
    print(f'Spesifikasi:')
    print(f"Kapasitas: {self.kapasitas}")
    print(f"RPM      : {self.rpm}")
    print(f"Memiliki harga Rp.{self.harga}")

pro = Processor('AMD', 'Ryzen™ 7 5800X', 6500000)
ram = RandomAccessMemory('Corsair', 'Corsair Vengeance DDR4 Dimm PC4-28800/3600MHz',1500000,"2x8GB")
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 520000, '500GB', 7200)
  
parts = [pro, ram, hdd]
print("\n\t\t\tHIERARCHICAL COMPUTER PART")
print("=================================================================================")

for part in parts :
  print()
  part.Tampil()
  print('-----------------------------------------------------------------------')