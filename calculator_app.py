print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))
print('=' * 25)

if operasi == '1':
    print('User memilih penjumlahan')
elif operasi == '2':
    print('User memilih pengurangan')
elif operasi == '3':
    print('User memilih perkalian')
elif operasi == '4':
    print('User memilih pembagian')
else:
    print('Tidak valid')
