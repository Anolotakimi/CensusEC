import csv


outfile = open('kids-quito.csv', 'w')

with open('poblacion.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)

    for row in reader:
        Provincia = int(row[0])
        Canton = int(row[1])
    #    Parroquia = row[2]
    #    Sexo = row[9]
    #    Edad = row[10]
    #    Etnia = row[35]
    #    Discapacidad = row[78]

        if Provincia == 17 and Canton == 1:
            line = '{},{},{},{},{}\n'.format(row[2], row[9], row[10], row[35], row[78])
            outfile.write(line)

outfile.close()