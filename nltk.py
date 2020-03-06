import nltk
import PyPDF2
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#function to convert .pdf to .txt file.
def pdftotxt(pdfname):
    pdfob=PyPDF2.PdfFileReader(pdfname)
    with open('G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karhis.txt','w') as f:
        for i in range(pdfob.getNumPages()):
            data=pdfob.getPage(i).extractText()
            f.write(data)
            
pdftotxt("G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karnataka_history.pdf")

sample_text = state_union.raw("G:/Pycharm/Pycharm Projects/CTYHP/nltk_testing/karhis.txt")

#tokenize using PunktSentenceTokenizer which uses pre-trained model 
tokenized = PunktSentenceTokenizer().tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)

            #visual representation
            namedEnt.draw()
            for subtree in namedEnt.subtrees(filter=lambda t: t.label() == 'PERSON'):
                print(subtree)
            for subtree in namedEnt.subtrees(filter=lambda t: t.label() == 'ORGANIZATION'):
                print(subtree)
            for subtree in namedEnt.subtrees(filter=lambda t: t.label() == 'GPE'):
                print(subtree)
    except Exception as e:
        print(str(e))


process_content()
