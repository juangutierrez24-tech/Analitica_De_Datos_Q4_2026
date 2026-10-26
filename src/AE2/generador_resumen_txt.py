from pathlib import Path


class GeneradorResumenTXT:
    def __init__(self):
        self.contenido = ""

    def generar(
        self,
        url_csv,
        url_json,
        archivo_csv_original,
        archivo_json_original,
        archivo_csv_modificado,
        archivo_json_modificado,
        registros_csv,
        registros_json,
        modificacion_csv,
        modificacion_json,
    ):
        self.contenido = f"""
RESUMEN DE LA ACTIVIDAD AE2
Manejo de archivos CSV, JSON y TXT
===================================

1. FUENTES DE DATOS

URL del CSV:
{url_csv}

URL del JSON:
{url_json}

2. ARCHIVOS PROCESADOS

CSV original: {archivo_csv_original}
CSV modificado: {archivo_csv_modificado}
Registros CSV procesados: {registros_csv}

JSON original: {archivo_json_original}
JSON modificado: {archivo_json_modificado}
Registros JSON procesados: {registros_json}

3. MODIFICACIONES REALIZADAS

CSV:
{modificacion_csv}

JSON:
{modificacion_json}

4. CLASES Y MÉTODOS UTILIZADOS

Clase ManejadorCSV:
- importar()
- modificar()
- guardar()

Clase ManejadorJSON:
- importar()
- modificar()
- guardar()

Clase GeneradorResumenTXT:
- generar()
- guardar()

5. RESULTADO

El resumen se generó mediante código a partir de los resultados
de la ejecución de las clases.
""".strip()

        return self.contenido

    def guardar(self, ruta):
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(self.contenido)

        return str(ruta)