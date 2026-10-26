import json
from pathlib import Path


class ManejadorJSON:
    def __init__(self):
        self.datos = []
        self.registros_procesados = 0
        self.modificacion = ""

    def importar(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        if not isinstance(self.datos, list):
            raise ValueError("Se esperaba una lista de registros JSON.")

        self.registros_procesados = len(self.datos)
        return self.datos

    def modificar(self):
        if not self.datos:
            raise ValueError("Primero debes importar los datos JSON.")

        # Agregar un campo que identifique el procesamiento de AE2.
        if "procesado_ae2" not in self.datos[0]:
            for registro in self.datos:
                registro["procesado_ae2"] = True

            self.modificacion = (
                "Se agregó el campo procesado_ae2 "
                "con valor true a todos los registros."
            )
        else:
            self.modificacion = (
                "El campo procesado_ae2 ya existía; "
                "no se agregó nuevamente."
            )

        return self.datos

    def guardar(self, ruta):
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=2)

        return str(ruta)