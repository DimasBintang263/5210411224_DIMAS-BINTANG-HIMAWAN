#program menghitung luas jajar genjang
alas = int(input("masukkan alas= " ))
tinggi = int(input("masukkan tinggi= " ))
def luasjajargenjang(alas,tinggi):
  luas = alas * tinggi
  return luas
hasil = luasjajargenjang(alas,tinggi)
print("Luas dari jajar genjang tersebut adalah= " + str(hasil)+ "cm")
