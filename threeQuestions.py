#importing all required modules
import csv
import nltk
import re
import testing_for_generic
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def ansQuery(query, filename):
    tech_words, versions=[],[]
    #getting the name of .csv file of the uploaded .pdf file
    file=filename[:-4]+"1.csv"

    #opening the .csv file
    with open(file) as f:
        #reading the .csv file
        reader = csv.reader((line.replace('\0','') for line in f), delimiter=",",skipinitialspace=True)
        #creating a list of technical words and versions of those technologies
        for row in  reader:
            tech_words.append(row[0].lower())
            versions.append(row[1])

    #checking whether any technologies used in uploaded .pdf file       
    if re.match( r'(is|are|does).*(support|supports|use|uses|implement|implements)?.*(technology|technologies|tech).*(supported|used|implemented)?.*',query):
        if tech_words:
            return 'Yes'
        else:
            return 'No technology is used'

    #checking wheher the queried tech is used in uploaded .pdf file
    elif re.match( r'(has|is|does).*(used|use|implement|implemented|support|supports|uses|supported|implements).*', query):
        #getting all the english stopwords
        stop_words = set(stopwords.words('english'))
        #tokenizing the user query
        word_tokens = word_tokenize(query)
        #filtering the tokenized query from stop words
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        #checking if filtered sentence has any technical word
        for w in filtered_sentence:
            if w in tech_words:
                return "Yes, "+ str(w)+" is supported."
        return "No, it is not supported."

    #checking for the version of the queried technology
    elif 'version' in query.split(' '):
        #getting all the english stopwords
        stop_words = set(stopwords.words('english'))
        #tokenizing the user query
        word_tokens = word_tokenize(query)
        #filtering the tokenized query from stop words
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        for w in filtered_sentence:
            #checking if filtered word is a technical word
            if w!='version' and w in tech_words:
                #returning the version of the technical word
                return versions[tech_words.index(w)]
        return False

    #checking for all technologies used in the uploaded .pdf file
    elif re.match( r'.*(technologies|tech|technology).*(use|uses|implement|implements|used|implemented|support|supports|supported).*',query):
        #removing the duplicates from tech_words list
        s=set(tech_words)
        #getting all the english stopwords
        stop_words = set(stopwords.words('english'))
        ans=""
        #getting all the tech words
        for i in s:
            if i not in stop_words or not i.isdigit():
                  ans+=i+", "
        ans=ans[:-2]+"."
        return "The technologies used are:"+ans
    
    else:
        return False
    
    


            
