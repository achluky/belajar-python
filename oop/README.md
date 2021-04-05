
# OOP

## Inheritence

## Polymorphism
### Konsep Dasar
Polymorphism = Poly + morphism = banyak + bentuk.

Jika berhubungan dengan konsep OOP maka Polymorphism adalah suatu konsep yang mendefinisikan bahwa objek yang memiliki kemampuan untuk mempunyai banyak bentuk, sebagai objek dari classnya sendiri atau dari parent/super classnya.

Keuntungan dengan menggunakan Polymorphism

1. Dapat menggunakan kelas-kelas yang kita buat (sebagai super kelas) dan membuat kelas kelas baru berdasar superkelas tersebut dengan karakteristik yang lebih khusus dari behaviour umum yang dimiliki superkelas.

2. Dapat membuat super kelas yang hanya mendefinisikan behaviuor namun tidak memberikan implementasi dari metode-metode yang ada.Hal ini berguna jika ingin membuat template kelas, kelas ini disebut kelas abstrak karena behaviournya masih abstrak dan belum diimplementasikan. Subkelas-subkelas dari kelas ini yang disebut kelas konkret, mengimplementasikan behaviuor abstrak tersebut sesuai dengan kebutuhan masing-masing.

3. Menghindari duplikasi object, yang dapat menciptakan class baru dari class yang sudah ada, sehingga tidak perlu menuliskan code dari nol ataupun mengulangnya, namun tetap bisa menambahkan attribute dan atau method unik dari class itu sendiri. Dalam konsep yang lebih umum sering kali polymorphism disebut dalam istilah satu interface banyak aksi.


### Jenis Polymorphism
1. Polymorphism pada fungsi dan objek

```python
class Yaris(): 
     def type(self): 
       print("Sedan") 
     def color(self):
       print("Merah") 

class Pajero(): 
     def type(self): 
       print("Sport") 
     def color(self): 
       print("Biru") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_yaris = Yaris() 
obj_pajero = Pajero() 
func(obj_yaris) 
func(obj_pajero)
```

2. Polymorphism pada class


```python
class Yaris(): 
     def type(self): 
       print("Sedan") 
     def color(self):
       print("Merah") 

class Pajero(): 
     def type(self): 
       print("Sport") 
     def color(self): 
       print("Biru") 
        
obj_yaris = Yaris() 
obj_pajero = Pajero() 
for mobil in (obj_yaris, obj_pajero):
    mobil.type()
    mobil.color()
```

3. Polymorphism pada inheritance

Terjadi ketika deklarasi fungsi subclass dengan nama dan parameter yang sama dengan fungsi dari superclassnya (Overiding).

```python
class Hewan:
    def name(self):
        pass
    def sleep(self):
        print('Tidur')
    def suara(self):
        pass

class Anjing(Hewan):
    def name(self):
        print('Saya Anjing')
    def suara(self):
        print('Gog Gog')

class Kucing(Hewan):
    def name(self):
        print('Saya Kucing')
    def suara(self):
        print('Meong')
    
class Singa(Hewan):
    def name(self):
        print('Saya Singa')
    def suara(self):
        print('Roar')

class TestHewan:
    def CetakNama(self, hewan):
        hewan.name()
    def goSleep(self, hewan):
        hewan.sleep()
    def BuatSuara(self, hewan):
        hewan.suara()

TestHewan = TestHewan()
anjing =  Anjing()
kucing =  Kucing()
singa =  Singa()

TestHewan.CetakNama(anjing)
TestHewan.goSleep(anjing)
TestHewan.BuatSuara(anjing)
TestHewan.CetakNama(kucing)
TestHewan.goSleep(kucing)
TestHewan.BuatSuara(kucing)
TestHewan.CetakNama(singa)
TestHewan.goSleep(singa)
TestHewan.BuatSuara(singa)
```

Penggunaan satu nama untuk beberapa fungsi yang berbeda (beda parameter) (Overloading)

```python
class Hewan:
    def name(self):
        pass
    def sleep(self):
        print('Tidur')
    def suara(self):
        pass

class Anjing(Hewan):
    def name(self):
        print('Saya Anjing')
    def sleep(self, status):
        print('Tidur ' + status )
    def suara(self):
        print('Gog Gog')

TestHewan = TestHewan()
anjing =  Anjing()

TestHewan.CetakNama(anjing)
TestHewan.goSleep(anjing, 'sendirian')
TestHewan.BuatSuara(anjing)
```

### Latihan
### Tugas