import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config
import py5

import math

def draw_kepala(x, y):
    # Kepala Utama
    py5.no_stroke()
    py5.fill(48, 196, 255)
    py5.ellipse(x, y - 25, 100, 50)  # Kepala utama
    py5.ellipse(x - 35, y, 50, 75)   # Telinga kiri
    py5.ellipse(x + 35, y, 50, 75)   # Telinga kanan
    py5.ellipse(x, y + 25, 100, 50)  # Bagian bawah kepala
    py5.ellipse(x + 28, y + 20, 105, 60)  # Bagian lebar di bawah

    # Telinga
    py5.fill(48, 196, 255)
    py5.triangle(x - 25, y - 45, x - 60, y - 10, x - 70, y - 50)  # Telinga kiri
    py5.triangle(x + 30, y - 45, x - 10, y - 40, x + 15, y - 65)  # Telinga kanan
    
    # Kumis Kiri
    py5.stroke(0, 0, 0)
    py5.stroke_weight(2)
    py5.line(x - 55, y + 25, x - 45, y + 20)
    py5.line(x - 45, y + 35, x - 37, y + 28)
    py5.line(x - 33, y + 43, x - 26, y + 35)
    
    # Kumis Kanan
    py5.line(x+78,y+28,x+69,y+24)
    py5.line(x+69,y+38,x+60,y+33)
    
    # Mata
    draw_mata(x + 5, y - 5)
    
    # Mulut
    py5.fill(255, 0, 0)
    py5.no_stroke() 
    py5.arc(x + 8, y + 17, 37, 60, 0, py5.PI)
    py5.fill(255, 105, 180)
    py5.ellipse(x + 8, y+37, 25, 20)
    
    # Hidung
    py5.fill(102, 105, 112)
    py5.arc(x+10, y+17, 40, 15, 0, py5.PI)
    py5.arc(x+10, y+17, 40, 7, py5.PI, 2 * py5.PI)
    py5.fill(255, 105, 180)
    py5.arc(x+10, y+13, 8, 10, 0, py5.PI)
    py5.stroke(0,0,0)
    py5.stroke_weight(1)
    py5.line(x+9, y+18, x+9, y+23)
    pass

def draw_mata(center_x, center_y):
    # Mengatur jarak antara dua mata
    eye_spacing = 25  # Jarak horizontal antara kedua mata

    py5.stroke_weight(0)
    py5.fill(255)  # Warna putih untuk mata
    py5.ellipse(center_x - eye_spacing, center_y, 45, 45)  # Lingkaran luar mata kiri
    py5.ellipse(center_x + eye_spacing, center_y, 45, 45)  # Lingkaran luar mata kanan

    # Menggambar Mata Kanan
    py5.stroke_weight(2)
    py5.fill(0)  # Warna hitam untuk pupil
    py5.ellipse(center_x - eye_spacing, center_y, 15, 15)  # Lingkaran pupil kiri
    py5.ellipse(center_x + eye_spacing, center_y, 15, 15)  # Lingkaran pupil kanan
    

def setup():
    py5.size(800, 800)
    #gumball = py5.load_image("referensi/gumball.webp")
    py5.grid = py5.load_image('referensi/grid.png')
    py5.image(py5.grid, 0, 0)
    #py5.image(gumball, 400, 400)
    py5.no_fill()
    py5.stroke_weight(3)
    py5.frame_rate(120)

def draw():
    py5.no_stroke()
    
    draw_kepala(350, 350)
    
py5.run_sketch()

