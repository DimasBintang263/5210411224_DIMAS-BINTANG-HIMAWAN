"""
PER5_TUGAS_LAPORAN
Nama: Dimas Bintang Himawan
Nim : 5210411224
"""

# Multilevel Inheritance
class ComputerPart:
    def __init__(self, pabrikan, nama, harga,jenis):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.jenis = jenis


class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(
            f"{self.nama} produk dari {self.pabrikan} dijual dengan harga Rp.{self.harga}")


class RandomAccessMemory(Processor):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self):
        print(
            f"{self.nama} produk dari {self.pabrikan} memiliki kapasitas sebesar {self.kapasitas} dijual dengan harga Rp.{self.harga}")


class HardDiskSATA(RandomAccessMemory):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(
            f"{self.nama} produk dari perusahaan {self.pabrikan} dijual dengan harga Rp.{self.harga}")


pro = Processor('AMD', 'Ryzen™ 7 5800X', 6500000)
ram = RandomAccessMemory('Corsair', 'Corsair Vengeance DDR4 Dimm PC4-28800/3600MHz',1500000,"2x8GB")
hdd = HardDiskSATA('WD Black', 'WD Black Caviar Dekstop HDD 3.5 inch', 2950000)

parts = [pro, ram, hdd]
print("\n\t\t\tMULTILEVEL COMPUTER PART")
print("=================================================================================")
for part in parts:
    part.Tampil()
print("=================================================================================\n")

#Hierarchical Inheritance ComputerPart

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

#Multiple Inheritance ProgramPart

def ruppiah(harga) :
    x = str(harga)
    if len(x) <= 3 :
        return "Rp." + x
    else :
        a = x[:-3]
        b = x[-3:]      
        return ruppiah(a) + '.' + b
    
class ComputerPart1():
    def __init__(self, pabrikan, nama) :
        self.pabrikan = pabrikan
        self.nama = nama
class ComputerPart2() : 
    def __init__(self, harga) :
        self.harga = harga

class Processor(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga, core,) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.core = core
    def Tampil(self) :  
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Jumlah Core = {self.core}")
        print(f"Harga : {ruppiah(self.harga)}")
class RandomAccessMemory(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self) :  
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"Harga : {ruppiah(self.harga)}")

class HardDiskSATA(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm
    
    def Tampil(self) :
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {ruppiah(self.harga)}")
     
class GraphicsCard(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga, kapasitas, MHz) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas
        self.MHz = MHz
    
    def Tampil(self) :
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"MHz : {self.MHz}")
        print(f"Harga : {ruppiah(self.harga)}")
def ruppiah(harga) :
    x = str(harga)
    if len(x) <= 3 :
        return "Rp." + x
    else :
        a = x[:-3]
        b = x[-3:]      
        return ruppiah(a) + '.' + b

pro = Processor('Intel', 'Core i7 7740X', 4500000, 5,)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MH', 2330000, '2x8GB')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 4200000, '1TB', 7200)
vga = GraphicsCard('NVIDIA', 'NVIDIA RTX 3080 TI', 6300000, 10, 1560)

parts = [pro, ram, hdd, vga]   
print("\n\t\t\t\tMULTIPLE COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
    print("")   
print("---------------------------------------------------------------------------------")
