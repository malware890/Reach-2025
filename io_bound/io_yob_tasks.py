from csv import writer

def io_yob(write_yob):
    wf = open(write_yob, 'w')
    w = writer(wf, lineterminator='\n')
    lines = wf.readlines()
    
    for line in lines:
        w.writerow([line.alpha.capitalize(), line.sex, str(line.count)])
    wf.close()
