Deskripsi:
Proyek ini adalah sebuah program Python yang menggunakan modul turtle untuk menggambar gambar hati berwarna merah. Program ini membuat hati menggunakan kombinasi perintah menggambar dan warna pengisian.

Cara Menggunakan:

1.Instal Python: Pastikan Anda sudah menginstal Python di komputer Anda.

2.Salin Kode: Salin kode Python berikut ke dalam file .py, misalnya draw_heart.py:

import turtle

t = turtle.Turtle()
t.speed(10)  
def draw_heart():
    t.begin_fill()
    t.color("red")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

draw_heart()

t.hideturtle()
turtle.done()

3.Jalankan Program: Jalankan file Python dengan perintah:

python draw_heart.py
Hasil: Program akan membuka jendela turtle dan menggambar hati merah.

Kontribusi:
Jika Anda ingin berkontribusi pada proyek ini, silakan ajukan pull request atau buka issue dengan ide atau perbaikan.

Lisensi:
Proyek ini dilisensikan di bawah MIT License.

Kontak:
Untuk pertanyaan atau dukungan, hubungi erlangga.nde@gmail.com.
