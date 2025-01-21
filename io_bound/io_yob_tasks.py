import csv
import mmap

def io_yob(read_yob, out_yob):
    reversed_rows = []
    with open(read_yob, 'r', newline='') as infile:
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            reversed_rows.append(row[::-1])

    with open(out_yob, 'wb') as outfile:
        csv_content = '\n'.join([','.join(row) for row in reversed_rows]) + '\n'
        encoded_content = csv_content.encode('utf-8')

        outfile.write(b' ' * len(encoded_content))

    with open(out_yob, 'r+b') as outfile:
        with mmap.mmap(outfile.fileno(), length=0, access=mmap.ACCESS_WRITE) as mm:
            mm.write(encoded_content)
