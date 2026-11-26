from pathlib import Path


FASTA_FILE = "gene.fna"
organismo = Path(FASTA_FILE).stem
complementos = str.maketrans("ATGC", "TACG")
gc_total = 0
bases_totales = 0


def formato_fraccion(gc, total):
    """Trunca a dos decimales para coincidir con los valores del ejemplo."""
    if total == 0:
        return "0"

    centesimas = gc * 100 // total
    entero, decimales = divmod(centesimas, 100)
    if decimales == 0:
        return str(entero)

    parte_decimal = f"{decimales:02d}".rstrip("0")
    return f"{entero}.{parte_decimal}" if entero else f".{parte_decimal}"


with open(FASTA_FILE, "r", encoding="utf-8") as fasta:
    primera_secuencia_del_contig = False

    for numero_linea, linea in enumerate(fasta, start=1):
        linea = linea.strip()

        if not linea:
            continue

        if linea.startswith(">"):
            encabezado = linea[1:].strip()
            print(f"Organismo {organismo}, contig {encabezado}")
            primera_secuencia_del_contig = True
            continue

        secuencia = linea.upper()
        bases_validas = [base for base in secuencia if base in "ATGC"]
        gc_linea = secuencia.count("G") + secuencia.count("C")
        gc_total += gc_linea
        bases_totales += len(bases_validas)

        print(f"GC línea {numero_linea}: {formato_fraccion(gc_linea, len(bases_validas))}")

        if primera_secuencia_del_contig:
            complementaria = secuencia.translate(complementos)
            print(complementaria)
            primera_secuencia_del_contig = False

        if "ATG" in secuencia:
            print(f"ATG en línea {numero_linea}")

print(f"GC total del archivo: {formato_fraccion(gc_total, bases_totales)}")

 #BIOM significa Biological Observation Matrix (matriz de observaciones biológicas). Es un formato estándar para guardar tablas de datos biológicos, especialmente conteos de microorganismos en muestras, como tablas de OTU o ASV de estudios de microbioma.

#¿Para qué sirve?
#Permite compartir y analizar datos de secuenciación con herramientas como QIIME 2 y otros programas de bioinformática. Además de los conteos, puede incluir información adicional sobre las muestras y los organismos.

#Estructura básica:

#Filas: organismos, OTU, ASV u otras características biológicas.
#Columnas: muestras.
#Valores: conteos o abundancias observadas.
#Metadatos: descripciones de las muestras y de las características.
#Formato de almacenamiento: puede ser JSON o HDF5. En una matriz dispersa, solo se guardan las celdas con valores distintos de cero para ahorrar espacio.
#link de video: https://youtu.be/DQWGcvDBb-o 
