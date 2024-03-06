import csv
import solar
import math



def readdata(filename):
    #open and read csv file for solar zenith angles
    #write to csv file programmic data
    datout = []
    with open(filename, newline='') as sonomafile:
        sonread = csv.reader(sonomafile, delimiter=' ', quotechar='|')
        for row in sonread:
            row = row[0].split(',')
            if row[0] == '2019':
                datout.append(row[17])
    return(datout)



print(readdata('Sonoma_Irradiance_data.csv'))

test = solar.Solar(37.76, 8)
print(test.getAzimuth(-4, 280))