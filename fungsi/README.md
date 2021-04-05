# Fungsi pada Python

### Memulai dengan Teladan
fungsi sederhana

```python
def cetak_pesan():
    print("Selamat Siang")

# program utama
cetak_pesan()
```

keluaran:
```
Selamat Siang
```

Posisi fungsi selalu di atas dari program utama


```python
def cetak_lagi():
    cetak_pesan()

# program utama
cetak_lagi()

def cetak_pesan():
    print("Selamat Siang")

```


keluaran:
```
NameError: global name 'cetak_pesan' is not defined
```