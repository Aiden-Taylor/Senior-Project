import csv





def readdata(filename):
    #open and read csv file for solar zenith angles
    # #-----Later functionality to select multiple locations for testing
    datout = []
    with open(filename, newline='') as sonomafile:
        sonread = csv.reader(sonomafile, delimiter=' ', quotechar='|')
        for row in sonread:
            row = row[0].split(',')
            if row[0] == '2019':
                datout.append(row[17])
    return(datout)



print(readdata('Sonoma_Irradiance_data.csv'))