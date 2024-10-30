import sys
import csv

files = sys.argv[1:]
fields    = []
img_names = []
headers   = []
openfiles = []

if len(files) >= 1:
    for file in files:
        with open(file) as data_csv:
            data      = csv.DictReader(data_csv)
            fields    = data.fieldnames
            headers   = data.fieldnames[1:-1]
            cols      = []

            next(data)
            img_names = [row[data.fieldnames[0]] for row in data]
            data_csv.seek(0)

            next(data)
            for header in headers:
                cols.append([int(row[header]) for row in data])
                data_csv.seek(0)
                next(data)

            openfiles.append(cols)


for i in range(len(files)):
    print(files[i])
    file = openfiles[i]
    for j in range(len(headers)):
        print(f"\t %-22s := %1.4f" % (headers[j], sum(file[j]) / len(file[j])))            

avgs = [[0] * len(openfiles[0][0]) for i in range(len(openfiles[0]))]
for row in range(len(openfiles[0][0])):
    for col in range(len(openfiles[0])):
        entry_avg = 0
        for file in openfiles:
            entry_avg += file[col][row]

        entry_avg /= len(openfiles)
        avgs[col][row] = entry_avg

output = "output.csv"

with open(output, 'w') as out:
    writer = csv.DictWriter(out, lineterminator="\n", fieldnames=fields)
    writer.writerow({fields[0] : fields[0], fields[1] : fields[1],
                     fields[2] : fields[2], fields[3] : fields[3],
                     fields[4] : fields[4], fields[5] : fields[5], 
                     fields[6] : fields[6]})
    for i in range(len(img_names)):
        writer.writerow({fields[0] : img_names[i], fields[1] : avgs[0][i],
                         fields[2] : avgs[1][i],   fields[3] : avgs[2][i],
                         fields[4] : avgs[3][i],   fields[5] : avgs[4][i], 
                         fields[6] : ""})

        

            


    