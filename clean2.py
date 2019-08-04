from dates import negative_dates
import io
import re
from _collections import OrderedDict

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

stop_words = set(stopwords.words('english'))
bad_chars = ['`',';','~','@','#','^','&','*','(',')','-','_','+','=','[',']','{','}', '–', '\''  ,'/',  '|',':','<','>','.','/','?',"'","\,",'‘','’','\'',',','”','”','“','…']
             

#########   positive_date  ##########

for xx in negative_dates:
    
    try:
        
        file1 = open(xx+".txt" ,encoding="utf8")
        print (xx)

        line = file1.read()
        #whitespace
        line=" ".join(line.split())
        #Number
        line = re.sub(r'\d+', '', line)
        #duplicate
        line_modified = OrderedDict().fromkeys(line.split())
        line=(' '.join(line_modified))

        #spl symbol
        for i in bad_chars : 
            line = line.replace(i, '')
            #print ("removed  " +i)

        words = line.split()


        #print ("hello-1")
               
        for r in words:
            if not r in stop_words:
                appendFile = open('cleaned_negative/'+xx+'.txt','a',encoding="utf8")
                w=lemmatizer.lemmatize(r)
                y=ps.stem(w)
                appendFile.write(" "+y)
                #print (r +"  "+w +" "+y)
        appendFile.write(" , negative")
        appendFile.close()
    except:
        #pass
        print (xx + "Not Found Date")






print ("\n\nhello Lord")

"""
1-separate data a/c to
2- via program fetch the file and after cleaning write positive and end
3-similar with the file of negative results
4-train
"""
