import spacy
import PyPDF2

#load english library
nlp=spacy.load("en_core_web_sm")

#function to convert .pdf to .txt file.
def pdftotxt(pdfname):
    pdfob=PyPDF2.PdfFileReader(pdfname)
    with open('G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karhis.txt','w') as f:
        for i in range(pdfob.getNumPages()):
            data=pdfob.getPage(i).extractText()
            f.write(data)
            
pdftotxt("G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karnataka_history.pdf")

f1=open("G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karhis.txt")
content=f1.readlines()
text=""
for i in content:
    text+=i
# Process whole documents
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
