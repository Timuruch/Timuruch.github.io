import math

t = 118
F = 4997904.0 #Суммарная тяга двигателей первой ступени в ваккууме (4 + 1), Н
Fmin = 4147360.0 #Суммарная тяга двигателей на старте (4 + 1), Н
M = 313000.0
angle = 61.0
k = 1688.0

ang = angle * ((math.pi/2)/90)/t
fuel_spent = (F - Fmin)/t


data = []
for x in range(1, t+1):
    fuel_coeff = (fuel_spent*x+Fmin)
    angle_coeff = (ang*x*angle)
    m_coeff = M-k*x
    wx = (fuel_coeff*math.sin(math.radians(angle_coeff)))
    wx = wx/m_coeff
    wy = (fuel_coeff*math.cos(math.radians(angle_coeff)))
    wy = wy/m_coeff
    wy -= 9.81
    data.append((wx, wy))


for i in range(1, len(data)):
    dat = data[i-1]
    print(i, "Секунда Полёта")
    print("X: ", dat[0], "M")
    print("Y: ", dat[1], "M")
