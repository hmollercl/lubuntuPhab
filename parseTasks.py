#!/usr/bin/python3
# uses
# sudo apt install python3-bs4
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import os

directory ="./Tasks"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        with open(directory + "/" + filename) as fp:
            parsed_html = BeautifulSoup(fp, features="lxml")
        title = parsed_html.title.string
        for par in parsed_html.body.find_all('p'):
            description = str(par).replace('\n','') #remove tags and \n


        continue
    else:
        continue

#print(parsed_html.title.string)
#print(parsed_html.body.find_all('div', attrs={'class':'phui-main-column'}))
#print(parsed_html.body.find_all('div', attrs={'class':'phui-box phui-box-border phui-object-box mlt mll mlr phui-box-blue-property'}))

#print(str(parsed_html.body.find_all('p')).replace('\n',''))

#for par in parsed_html.body.find_all('p'):
    #if par.string is not None:
        #print(str(par.string).replace('\n','')) #remove tags and \n
#    print(str(par).replace('\n','')) #remove tags and \n
