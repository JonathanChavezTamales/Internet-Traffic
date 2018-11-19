import math
import matplotlib.pyplot as plt
import datetime as dt

#Abrir archivo lectura
file = open('data.csv', 'r')
rows = []

#[fecha, hora, bits]
for row in file:
    rows.append(row.rstrip().replace(' ', ',').replace('\"', '').split(','))

#Borro headers
del rows[0]

def promedio_hora(hora):
    """
    Recibe una hora y regresa el promedio de bits de cada día de esa hora
    el argumento debe ir en la forma '14:00' 24:00h
    """
    bits = []

    for i in rows:
        if i[1] == hora:
            bits.append(float(i[2]))
    return sum(bits)/len(bits)

def promedio_hora_plot(hora):
    """
    Recibe una hora y regresa el promedio de bits de cada día de esa hora
    el argumento debe ir en la forma '14:00' 24:00h
    """
    bits = []
    fechas = []

    for i in rows:
        if i[1] == hora:
            bits.append(float(i[2]))
            #Convierto fecha de string a datetime para no problemas con pyplot
            fechas.append(dt.datetime.strptime(i[0], '%Y-%m-%d'))

    return (fechas,bits)

def menor_dia(dia):
    """
    Recibe día y retorna hora con menor tráfico
    Formato día: '2007-12-30'
    """

    menor = 999999
    hora = None
    for i in rows:
        if i[0] == dia:
            if float(i[2]) < menor:
                menor = float(i[2])
                hora = i[1]
    return hora

def horas_menor_trafico():
    """
    Retorna la hora con menor tráfico de cada día, perfecto para histograma
    """
    horas = []
    fecha_actual = rows[0][0]
    horas.append(menor_dia(fecha_actual))
    for i in rows:
        if i[0] != fecha_actual:
            fecha_actual = i[0]
            horas.append(menor_dia(fecha_actual))
    return horas

def dia_menor_trafico_930():
    """
    Retorna día en el que menos tráfico hubo entre 9:30 y 23:30
    """
    menor = 99999
    dia_menor = None
    for i in rows:
        date = i[1].split(':')
        hora = int(date[0])
        if (hora > 9 and hora < 23):
            if float(i[2]) < menor:
                dia_menor = i[0]
    return dia_menor




def main():

    a = promedio_hora_plot('10:30:00')
    b = promedio_hora_plot('13:30:00')
    c = promedio_hora_plot('16:30:00')
    d = promedio_hora_plot('19:30:00')
    e = promedio_hora_plot('23:30:00')
    plt.plot(a[0],a[1])
    plt.plot(b[0],b[1])
    plt.plot(c[0],c[1])
    plt.plot(d[0],d[1])
    plt.plot(e[0],e[1])
    plt.legend(['10','13','16','19','23'], title='Hora del día')
    plt.xlabel('Días')
    plt.ylabel('Bits transmitidos promedio')
    plt.title('Promedio de bits transmitidos por hora cada día')
    plt.show()
    plt.clf

    print(menor_dia('2005-01-06'))

    plt.hist(horas_menor_trafico())
    plt.ylabel('Ocasiones')
    plt.xlabel('Horas')
    plt.title('Frecuencia de horas con menos tráfico')
    plt.show()
    print(max(horas_menor_trafico()))

    print(dia_menor_trafico_930())

main()
