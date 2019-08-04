import csv

dates=[]
with open('10-18.csv','r') as f:
    c_reader=csv.reader(f)
    #print(c_reader)

    for line in c_reader:
        if (line[9]!='0'):
            dates.append( "20"+(line[0])[7:9:1]  +"-"+ (line[0])[3:6:1] +"-"+(line[0])[0:2:1]  )
          
            #print ( "20"+(line[0])[7:9:1]  +"-"+ (line[0])[3:6:1] +"-"+(line[0])[0:2:1]  )

print (dates)

print ("\nHello Lord")
