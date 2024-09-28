import primitif.line
import py5
import numpy as np
import math

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin,margin,width-margin,margin))
    py5.points(primitif.line.line_dda(margin,height-margin,width-margin,height-margin))
    py5.points(primitif.line.line_bresenham(margin,margin,margin,height-margin))
    py5.points(primitif.line.line_bresenham(width-margin,margin,width-margin,height-margin))

def draw_grid(width, height, margin, c=[0,0,0,255]):
    # Sumbu Y
    xa = margin;
    ya = 2*margin;
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa,ya,xb,ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa,ya,xa,yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2,margin,width/2,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/2,width-margin,height/2))
    
def persegi(xa, ya, panjang, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya,xa,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa+panjang,ya, xa+panjang,ya+panjang))

def persegi_panjang(xa, ya, panjang, lebar, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass

def segitiga_siku(xa, ya, alas, tinggi, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass


def trapesium_siku(xa, ya, aa, ab, tinggi, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    pass

def kali(xa, ya, panjang, c=[255,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(xa,ya,xa+panjang,ya+panjang))
    py5.points(primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya))

def circlePlotPoints(xc, yc, x, y):
    return [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
    ]

def lingkaran(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius

   
    circle_points = []
    circle_points.extend(circlePlotPoints(xc, yc, x, y))

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        
        circle_points.extend(circlePlotPoints(xc, yc, x, y))

    return circle_points            

def ellipsePlotPoints(xc, yc, x, y):
    return [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y]
    ]

def ellipse(xc, yc, Rx, Ry):
    Rx2 = Rx * Rx
    Ry2 = Ry * Ry
    twoRx2 = 2 * Rx2
    twoRy2 = 2 * Ry2
    x = 0
    y = Ry
    px = 0
    py = twoRx2 * y

    ellipse_points = []

    
    p = Ry2 - (Rx2 * Ry) + (0.25 * Rx2)
    while px < py:
        ellipse_points.extend(ellipsePlotPoints(xc, yc, x, y))
        x += 1
        px += twoRy2
        if p < 0:
            p += Ry2 + px
        else:
            y -= 1
            py -= twoRx2
            p += Ry2 + px - py

   
    p = Ry2 * (x + 0.5) ** 2 + Rx2 * (y - 1) ** 2 - Rx2 * Ry2
    while y > 0:
        ellipse_points.extend(ellipsePlotPoints(xc, yc, x, y))
        y -= 1
        py -= twoRx2
        if p > 0:
            p += Rx2 - py
        else:
            x += 1
            px += twoRy2
            p += Rx2 - py + px

    return ellipse_points


def apply_pattern(points, pattern):
    pattern_points = []
    
    if pattern == 'dot':
        for i, (px, py) in enumerate(points):
            if i % 5 == 0:
                pattern_points.append((px, py))

    elif pattern == 'dot-strip':
        dash_length = 10
        dot_length = 1
        gap_length = 7
        counter = 0

        for i, (px, py) in enumerate(points):
            if counter < dash_length:  
                pattern_points.append((px, py))
            elif counter == dash_length + gap_length:  
                pattern_points.append((px, py))
            counter += 1
            if counter >= dash_length + gap_length + dot_length:  
                counter = 0

    elif pattern == 'strip':
        dash_length = 20
        gap_length = 10
        counter = 0

        for i, (px, py) in enumerate(points):
            if counter < dash_length:  
                pattern_points.append((px, py))
            elif counter < dash_length + gap_length:
                pass
            counter += 1
            if counter >= dash_length + gap_length:
                counter = 0

    elif pattern == 'solid':
        pattern_points = points

    return pattern_points

def translate2D(tx, ty, pts):
    return [(x + tx, y + ty) for x, y in pts]

def scale2D(sx, sy, refx, refy, pts):
    return [
        (refx + (x - refx) * sx, refy + (y - refy) * sy)
        for x, y in pts
    ]

def rotate2D(x, y, angle_deg, refx, refy):
    angle_rad = np.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)

    dx = x - refx
    dy = y - refy

    xr = dx * cos_a - dy * sin_a + refx
    yr = dx * sin_a + dy * cos_a + refy

    return xr, yr

def transformation(points, refx, refy, angle_deg=0, tx=0, ty=0, sx=1, sy=1):
   
    transformed_points = scale2D(sx, sy, refx, refy, points)

    
    if angle_deg != 0:
        transformed_points = [
            rotate2D(x, y, angle_deg, refx, refy)
            for x, y in transformed_points
        ]

    
    transformed_points = translate2D(tx, ty, transformed_points)

    return transformed_points


def draw_points(points, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    for (x, y) in points:
        py5.point(x, y)