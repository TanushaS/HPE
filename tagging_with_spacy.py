'''from __future__ import unicode_literals, print_function

import plac #  wrapper over argparse
import random
from pathlib import Path
from tqdm import tqdm # loading bar
import spacy

def tagging(data):
      with open('{}'.format(data.replace('pdf','txt')),'r') as file:
          content=file.read()
      #replacing \n, /, : and , with space 
      content=content.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
      #creating a list to store all the read words
      #l=content.split()
      output_dir=Path("C:/Users/Admin/Downloads/FINAL")
      # test the saved model
      print("Loading from", output_dir)
      nlp2 = spacy.load(output_dir)
      doc = nlp2(content)
      print('Entities', [(ent.text, ent.label_) for ent in doc.ents])'''

import spacy
import csv

#################### version parser ########################################
def version_parser(txtfile,referenceKB,newKb):
    #Opening the document in .txt format
    with open(txtfile,"r") as file:
        content=file.read()
    #replacing \n, /, : and , with space 
    content=content.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
    #creating a list to store all the read words
    l=content.split()
    ver=[]#list to store versions of the tech words
    ver_ind=[]#list to store indices of the versions
    for i in range(len(l)):
        try:
            if (l[i][0]=="v" or l[i][0]=="V") and l[i][1].isdigit():
                ver.append(l[i])
                ver_ind.append(i)
            elif i<len(l)-2:
                if (l[i]=="version" or l[i]=="Version") :
                    if  l[i+1][0].isdigit():
                        ver.append(l[i+1])
                        ver_ind.append(i+1)
                    elif  l[i+2][0].isdigit():
                        ver.append(l[i+2])
                        ver_ind.append(i+2)
        except:
            continue
    
    #list to store tech words in knowledge base
    words=[]
    #reading knowledgeBase.csv file
    with open(referenceKB) as csv_file:
        reader = csv.reader((line.replace('\0','') for line in csv_file), delimiter=",",skipinitialspace=True)
        for row in reader:
            words.extend(row)
    #converting all strings in words list to lowercase 
    for i in range(len(words)):
        j=words[i].replace(" ","")
        j=j.lower()
        words[i]=j
    w=[]#list to store tech words found in the document
    ind=[]#list to store indices of those tech words

    #to find tech words in the document
    for i in range(len(l)):
        if  l[i].lower() in words and l[i] not in w:
            w.append(l[i])
            ind.append(i)
        elif i<(len(l)-2):
            m=l[i].lower() +l[i+1].lower()
            if m in words and (l[i]+l[i+1]) not in w:
                w.append(l[i]+l[i+1])
                ind.append(i)
                continue
            n=l[i].lower() +l[i+1].lower()+l[i+2].lower()
            if n in words and (l[i]+l[i+1]+l[i+2]) not in w:
                w.append(l[i]+l[i+1]+l[i+2])
                ind.append(i)
    with open(newKb,'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in range(len(ind)):
            try:
                if ind[i] < ver_ind[0] and ind[i+1]>ver_ind[0] :
                    #print("TECH:",w[i],"VERSION:",l[ver_ind.pop(0)])
                    writer.writerow((w[i],l[ver_ind.pop(0)]))
                    if len(ver_ind)==0:
                        break
            except:
                continue
        for word in words:
            if word not in w:
                writer.writerow((word,"NA"))
    print("DONE....")

def tagging(data):
    prdnlp = spacy.load("C:/Users/Admin/Downloads/FINAL")
    txtfile='{}'.format(data.replace('pdf','txt'))
    with open(txtfile,'r') as f: #Give the text extracted file here for tagging
        content1=f.read()
        content1=content1.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
        content=content1.split(' ')
        for i in range(len(content)):
            if '\n' in content[i]:
                l=content[i].split('\n')
                for w in l:
                    if not w.isdigit():
                        content.insert(i,w)

    doc = prdnlp(content1[:len(content1)])

    items = [x.text for x in doc.ents]

    # Update KB with new words

    new_words=set(items)#[w for w in items if not w in words] # words tagged by spacy which are not there in the KB
    referenceKB='{}'.format(data.replace('pdf','csv'))
    with open(referenceKB,'w', newline='') as file:
        writer=csv.writer(file)
        for w in new_words:
            writer.writerow([w])
            
    newKB=data[:-4]
    newKB=newKB+"1.csv"

    version_parser(txtfile,referenceKB,newKB)



