import csv


outfile = open('girls-quito.csv', 'w')

with open('kids-quito.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:

        Sexo = int(row[1])
        Edad = int(row[2])
    #    Parroquia = row[0]
    #    Sexo = row[1]
    #    Edad = row[2]
    #    Etnia = row[3]
    #    Discapacidad = row[4]

        if Sexo == 2 and Edad <= 5:
            line = '{},{},{},{},{}\n'.format(row[0], row[1], row[2], row[3], row[4])
            outfile.write(line)

outfile.close()