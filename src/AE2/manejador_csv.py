
import csv
from pathlib import Path


class ManejadorCSV:
    def __init__(self):
        self.encabezados = []
        self.datos = []
        self.registros_procesados = 0
        self.modificacion = ""

    def importar(self, ruta):
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)

        if not filas:
            raise ValueError("El archivo CSV está vacío.")

        self.encabezados = filas[0]
        self.datos = filas[1:]
        self.registros_procesados = len(self.datos)

        return self.encabezados, self.datos

    def modificar(self):
        columna = "procesado_ae2"

        if columna not in self.encabezados:
            self.encabezados.append(columna)
            for fila in self.datos:
                fila.append("Sí")
            self.modificacion = (
                "Se agregó la columna procesado_ae2 "
                "con el valor Sí a cada registro."
            )
        else:
            self.modificacion = (
                "La columna procesado_ae2 ya existía; "
                "no se agregó nuevamente."
            )

        return self.encabezados, self.datos

    def guardar(self, ruta):
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)

        return str(ruta)
