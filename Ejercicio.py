# Leer Archivo csv
import pandas as pd
import xml.etree.cElementTree as ET

#leer Archivo
df = pd.read_csv('Usuarios.csv', sep=";")
print(df)
df.to_json("Servicios.json")

root = ET.Element('root')
doc = ET.SubElement(root, 'doc')
for idx in df.index:
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Cuenta[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Nombres[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Apellidos[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Cargo[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Dependencia[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Oficina[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Telefono[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Email[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Compania[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Ciudad[idx])
    ET.SubElement(doc, 'nodo' + str(idx), name='Cuenta' + str(idx)).text=str(df.Estado[idx])

ar = ET.ElementTree(root)
ar.write('Programacion.xml')
