# Komplain Nilai

Repository ini digunakan untuk menampung berbagai komplain nilai. Berikut ini langkah-langkah yang diperlukan untuk melakukan komplain. 
1. Pelajari format serialisasi [Cap'n Proto](https://capnproto.org/)
2. Buat serialisasi *Cap'n Proto* dengan _schema_:
  * Nama
  * NIM
  * Mata Kuliah
  * Nilai yang menurut anda pantas didapatkan
  * Alasan mengapa anda pantas mendapatkan nilai itu
3. Dengan menggunakan Python, buat script untuk inisialisasi _schema_ tersebut dan isikan data anda. Silahkan lihat di pustaka [pycapnp](http://capnproto.github.io/pycapnp/)
4. Nama-nama file yang anda buat:
  * prodi-nim.capnp (berisi _schema_)
  * prodi-nim.py (berisi script untuk mengisi data berdasarkan _schema_
5. Simpan 2 file tersebut dalam satu direktori dengan nama *prodi-nim*, kemudian kirim PR ke repo ini. 
6. Komplain anda akan saya jawab di komentar dari PR yang anda kirim.

Contoh struktur direktori dan file-file yang harus anda buat untuk dikirim sebagai PR:

~~~~
- 123456
  |______ ti-1233456.capnp
  |______ ti-123456.py
~~~~

Prosedur untuk komplain nilai ini mutlak, jika tidak diikuti, maka komplain nilai tidak dilayani.

