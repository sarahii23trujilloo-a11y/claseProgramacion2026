#Tarea 5.

#Dado el archivo fasta, hacer un programa con las siguientes funciones

#(1 punto)
#1. Para todos los encabezados, lo imprima en el formato
"Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""
with open("phytophtora.fasta","r") as f:
	# Your code to process the file goes here
 for line in f:
  line= line.strip() #elimina espacios y saltos de linea
  if line.startswith(">"): #verifica si la linea es un encabezado
   encabezado= line[1:] #elimina el ">"
   print("Organismo phytophtora, contig", encabezado)
   

#(2 punto)
#2. Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"
def GCcontent(sequence):
    gc_count = sum(1 for base in sequence if base.upper() in ['G', 'C'])
    if len(sequence) == 0:
        return 0
    porcentaje = gc_count / len(sequence)
    return porcentaje

with open("phytophtora.fasta", "r") as fa:
    line_number = 0
    for line in fa:
        line = line.strip()
        if not line.startswith(">") and line != "":
            line_number += 1
            gc = GCcontent(line)
            print(f"GC línea {line_number}: {gc:.2f}")
#(2 puntos)
#3. Para la primera secuencia de cada segmento, imprima su secuencia complementaria
def complement(seq):
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C',
            'a':'t', 't':'a', 'c':'g', 'g':'c'}
    return ''.join(comp.get(base, base) for base in seq)

### al correr tu código, imprime el complemento de todas las líneas, no sólo la primera
with open("phytophtora.fasta", "r") as f:
    print_next_seq = False
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            print_next_seq = True
            continue
        if print_next_seq and line:
            print(complement(line))
            print_next_seq = True

#(2 punto)
#4. Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"
with open("phytophtora.fasta", "r") as f:
    line_number = 0
    for line in f:
        line = line.strip()
        if line and not line.startswith(">"):
            line_number += 1
            if "ATG" in line.upper():
                print(f"ATG en línea {line_number}")
#(1 punto)
#5. Calcule el contenido GC total del archivo y lo imprima al final en formato "GC total del archivo: <GC>"
def gc_total(fasta_path):
    gc_count = 0
    total_count = 0
    with open(fasta_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue  # Skip headers and empty lines
            gc_count += sum(1 for base in line if base.upper() in ['G', 'C'])
            total_count += len(line)
    gc_content = gc_count / total_count if total_count > 0 else 0
    print(f"GC total del archivo: {round(gc_content, 2)}")
gc_total("phytophtora.fasta")

