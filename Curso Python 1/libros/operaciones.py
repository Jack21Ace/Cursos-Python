# 1- se importan las librerias
import sqlite3

# 2- se creara la variable de conexión dentro una función
def conn():
    conexion = sqlite3.connect("Libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, año INTEGER, code INTEGER)")
    conexion.commit()
    conexion.close()

# 4- Función para insertar datos
def insert(titulo, autor, año, code):
    conexion = sqlite3.connect('Libros.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES (Null,?,?,?,?)", (titulo, autor, año, code))
    conexion.commit()
    conexion.close()

# 5- Visualización de contenido de la db
def read():
    conexion = sqlite3.connect("Libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    result = cursor.fetchall()
    conexion.close()
    return result

# 6- Buscar el ontendio mediante el metodo Seach
def search(titulo='', autor='', año=0, code=0):
    conexion = sqlite3.connect("Libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR año=? OR code=?",(titulo, autor, año, code))
    result = cursor.fetchall()
    conexion.close()
    return result

# 7- Eliminar un elemento mediante el metodo delete
def delete(id):
    conexion = sqlite3.connect("Libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?",(id, ))
    conexion.commit()
    conexion.close()

# 7- Actualizar un elemento mediante el metodo update
def update(titulo, autor, año, code, id):
    conexion = sqlite3.connect("Libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, año=?, code=? WHERE id=?", (titulo, autor, año, code, id))
    conexion.commit()
    conexion.close()

# 3- Pruebas invocando la función conn
conn()
# # prueba de insert
# insert("titulo4", "autor1", 2000, 6996)
# insert("titulo5", "autor2", 2001, 6431)
# insert("titulo6", "autor2", 2003, 862)
# insert("titulo7", "autor1", 2000, 6996)
# insert("titulo8", "autor2", 2001, 6431)
# insert("titulo9", "autor2", 2003, 862)
# insert("titulo10", "autor1", 2000, 6996)
# insert("titulo11", "autor2", 2001, 6431)
# insert("titulo12", "autor2", 2003, 862)

# # visualización de datos
# datos = read()
# for dato in datos:
#     print(dato)

# # ahora vamos a buscar datos por titulo o por el que se desee
# results = search(code=862)
# for result in results:
#     print(result)

# # Borrar
# insert("titulo4", "autor2", 2003, 862)
# datos = read()
# for dato in datos:
#     print(dato)
# # delete(4)
# # datos = read()
# # for dato in datos:
# #     print(dato)

# # Actualizar
# update(titulo="titulo3", autor="autor3", año=6646, code=976431, id=3)
# datos = read()
# for dato in datos:
#     print(dato)