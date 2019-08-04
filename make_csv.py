
#2018-02-25
appendFile = open('All/Bdata.csv','a',encoding="utf8")
appendFile.write('HeadLines , Status \n')
appendFile.close()
                    
for i in range(0,10):
    for j in range(1,10):
        for k in range(0,4):
            for m in range(0,10):
                xx=("201"+str(i)+"-0"+str(j)+"-"+str(k)+str(m))
                
                try:
                    file1 = open(xx+".txt", "r",encoding="utf8")
                    print (xx)
                    line = file1.read()
                    #words = line.split()
                    appendFile = open('All/Bdata.csv','a',encoding="utf8")
                    appendFile.write(line+'\n')
                    appendFile.close()
                except:
                    print (xx + "Not Found Date")
                


for i in range(0,10):
    for j in range(10,13):
        for k in range(0,4):
            for m in range(0,10):
                xx=("201"+str(i)+"-"+str(j)+"-"+str(k)+str(m))
                
                try:
                    file1 = open(xx+".txt", "r",encoding="utf8")
                    print (xx)
                    line = file1.read()
                    #words = line.split()
                    appendFile = open('All/Bdata.csv','a',encoding="utf8")
                    appendFile.write(line+'\n')
                    appendFile.close()
                except:
                    print (xx + "Not Found Date")
                

