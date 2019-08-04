import io
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

stop_words = set(stopwords.words('english'))
#bad_chars = ['`','~','@','#','^','&','*','(',')','-','_','+','=','[',']','{','}',  '\''  ,  '|',':','<','>','.','/','?',"'","\,",'‘','’','\'',',']
             
#','

#########   positive_date  ##########

file1 = open("zzz.txt" ,encoding="utf8")

line = file1.read()

words = line.split()

print ("hello-1")
       
for r in words:
    if not r in stop_words:
        appendFile = open('done.txt','a',encoding="utf8")
        w=lemmatizer.lemmatize(r)
        y=ps.stem(w)
        appendFile.write(" "+y)
        print (r +"  "+w +" "+y)
        appendFile.close()





"""
for r in words: 
	if not r in stop_words: 
		appendFile = open('fzzz.txt','a',encoding="utf8")
		#print (r)
		#appendFile.write(" "+r) 
		appendFile.close() 


#print (token)
"""
print ("\n\nhello Lord")

"""
1-separate data a/c to
2- via program fetch the file and after cleaning write positive and end
3-similar with the file of negative results
4-train
"""
