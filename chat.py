  
import nltk
import csv
import random
#import testing_for_generic
flag1=0
def genericResponse(question):
    if(question in ['Bye','bye','Bye!','bye!']):
        return "Bye! take care.."
    elif (question.lower() in ['thanks','thank you']):
        return "You are welome:)"
    elif(greeting(question)!=None):
        return greeting(question)
    fin=open("F:/upload/uploads/qna_chitchat_friendly.tsv")
    read_tsv=csv.reader(fin,delimiter="\t")
    global flag1
    for row in read_tsv:
        if(row[0].lower()==question):
            #print(row[1])
            flag1=1;
            return row[1]
    '''if flag1==0:
        q2=testing_for_generic.main(question)
        flag1=2
        response(q2)'''
    

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

    
def main():
   flag=True
   print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type bye!")
   while(flag==True):
      user_response = input("Ask a question :").lower()
      #user_response.lower()
      if(user_response!='bye'):
          if(user_response=='thanks' or user_response=='thank you' ):
              flag=False
              print("ROBO: You are welcome..")
          else:
              if(greeting(user_response)!=None):
                  print("ROBO: "+greeting(user_response))
              else:
                  print("ROBO: ",end="")
                  flag1=0
                  print(response(user_response))
                
      else:
          flag=False
          print("ROBO: Bye! take care..")

if __name__=='__main__':
    main()
