#praktik pbo.py
str='aku cinta indonesia'
print(str)
str=str[:10]+'tanah air ku'+str[9:]
print(str)
str=''
print(str)
str1='aku cinta tanah air ku indonesia'
str1=str1[:9]+''+str1[22:]
print(str1)
kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)
s='     Python    '
s.strip()
s.lstrip()
s.rstrip()
len(kelas)
jumlah=len(kelas)
print('panjang string adalah:',jumlah)
s1='python'
s2='programming'
print(s1+s2)
print(kelas)
print(kelas.index('a'))
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)
a='satu'
b='dua'
c='tiga'
print('saya mempunyai %s mangga'%(c))
print(kelas2)
kelas2.split()
input('hari ini adalah: ')
data1=input('angka 1: ')
data2=input('angka 2: ')
hasil=int(data1)*int(data2)
print(data1,'*',data2,' = ',hasil)

#list
list=[0,1,2,3,4,5,6,7,8,9]
print(list)
print(list[0])
print(list[5])
print(list[:3])
print(len(list))
print(list[10-3:])
print(list[2:9])
print(list[-10])
list.append(10)
print(list)
list.insert(1,11)
print(list)
list2=['halo']
list.extend(list2)
print(list)
list.extend('hai')
print(list)
del list[1]
print(list)
list.remove(10)
print(list)
print(list.pop())
print(list)
print(list.pop(2))
print(list)
a=[50,10,20,30,40]
b=sorted(a)
print(b)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))

#dictionary
d={1:100, 2:200, 3:300, 4:400, 5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[1]
print(d)
b=d.copy()
print(b)
d.clear()
print(d)
len(d)

#tuple
t=(100,200,300,400)
print(t)
print(t[0])
print(t[3])
print(t.index(200))
t2=(10,20,10,30,10,40,20)
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))

# set
abjad = {'a', 'b', 'c'}
print(abjad)
# menambah add()
abjad.add('d')
abjad.add('e')
print(abjad)
# menambah update()
abjad.update({ 'f', 'g' })
print(abjad)
# bisa juga pakai list
abjad.update(['h', 'i'])
print(abjad)
himpunan = {'maya', 'budi', 100, ('a', 'b'), False, True}
print(himpunan)
# remove()
himpunan.remove(100)
print(himpunan)
# discard()
himpunan.discard(('a', 'b'))
print(himpunan)
# pop()
nilaidihapus = himpunan.pop()
print('nilai dihapus =', nilaidihapus)
print(himpunan)
# clear()
himpunan.clear()
print(himpunan)
grup_kelas1 = {
  'andi', 'budi', 'ratna', 'sari'
}
grup_kelas2 = {
  'putri', 'ratna', 'andi', 'agus'
}
#union()
# cara 1
print(grup_kelas1 | grup_kelas2)
# cara 2
print(grup_kelas1.union(grup_kelas2))
#intersection()
# cara 1
print(grup_kelas1 & grup_kelas2)
# cara 2
print(grup_kelas1.intersection(grup_kelas2))
#intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#difference()
print('\nanggota kelas1 yang bukan anggota kelas2:')
print(grup_kelas1 - grup_kelas2)
print(grup_kelas1.difference(grup_kelas2))
print('\nanggota kelas2 yang bukan anggota kelas1:')
print(grup_kelas2 - grup_kelas1)
print(grup_kelas2.difference(grup_kelas1))
#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
#symmetric_difference()
print('\nanggota yang hanya ikut satu kelas saja:')
print(grup_kelas2.symmetric_difference(grup_kelas1))
#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
#issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
