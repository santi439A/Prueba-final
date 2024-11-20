import csv

def guardar_articulos_csv(articulos, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for articulo in articulos:
            writer.writerow(articulo)

def guardar_articulo_csv(nombre_archivo, articulo):
  with open(nombre_archivo, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(articulo)

def leer_articulos_csv(nombre_archivo):
    articulos = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for articulo in reader:
            articulos.append(articulo)

    return articulos