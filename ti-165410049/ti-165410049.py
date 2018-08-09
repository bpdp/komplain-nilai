
from __future__ import print_function
import os
import capnp

capnp.remove_import_hook()
capnp=capnp.load('ti-165410049.capnp')
mahasiswa=ti-nim.mahasiswa.new_message()
mahasiswa.nama='Ganesha Bintang Sri Dahono'
mahasiswa.nim='165410049'
mahasiswa.mata_kuliah='Konsep Cloud Computing'
mahasiswa.nilai_pantas='B'
mahasiswa.alasan='format penilaian 50:50 untuk UTS dan UAS disertai dengan kisi-kisi yang sesuai dengan soal yang diujikan. Saya seharusnya bisa mendapat nilai setidaknya B'

print ('NAMA :'.mahasiswa.nama)
print ('NIM :'.mahasiswa.nim)
print ('MATA KULIAH :'.mahasiswa.mata_kuliah)
print ('NILAI YANG PANTAS SAYA DAPATKAN :'.mahasiswa.nilai_pantas)
print ('ALASAN :'.mahasiswa.alasan)