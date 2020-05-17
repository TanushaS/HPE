
from textblob.classifiers import NaiveBayesClassifier, DecisionTreeClassifier 
import textblob

def mainQuery(query):
   generic_questions = ("Let's go","You never wanted to go out with 'me, did you?","Who knows?","What annoys you?",
                     "you've heard of him?","What were you doing?","Thank you anyway","No problem",
                     'She okay?',"Yes, I have a question.","What is your question?","What are your hobbies?",
                     "You know how sometimes you just become this 'persona'?  And you don't know how to quit?",
                     "what's up?",'sup people? I see the weather\'s getting better over there, Ben.',
                     "how are you doing?","Hi","Hello","Hey","How's you?","Have you heard the news?",
                     'i had the same problem your having so thats my i made my own.',"What is your favorite book?",
                     "good night","good morning","good afternoon","good evening","So what's your favorite color?",
                     'What good stuff?',"what's new?","How's life?","That is good to hear",
                     "I am doing well, how about you?","I am doing well, how about you?","I'm also good.",
                     "What are you then?",'What are you working on?',"Who are you?","What is it like?",
                     "How do you work?","Who is your appointment with?","What languages do you like to use?",
        )


   technical_questions=("Clearpass is extended to IT systems using which API?",
                     "Which browsers are supported for ClearPass?",
                     "Which  virtualization platforms  is supported by Clearpass?",
                     "name the authentication/authorization sources used by clearpass.",
                     "does Clearpass use ipv6 or ipv4 addressing?",
                     "how many sessioons can  be provided by ClearPass C2000 Hardware Appliance?",
                     "how does Admin/Operator access security?",
                     'Virtual Appliances are supported on which platforms?',
                     "Name the ClearPass Hardware Appliance Ports.",
                     "What is the expansion of OCSP?",
                     "what are the active Profiling Methods?",
                     "What are cookies?",
                     "what does dynamic authorisation mean?",
                     "Which standard the clearpass Guest is built on?",
                     "which protocol is used by the  NAS  to authenticate the user ?",
                     "Which network connectivity is provisioned for Clearpass Guest?",
                     "What is NAS?",
                     "What are the possible states of a session?",
                     "what does dynamic authorisation mean?",
                     'Which standard the clearpass Guest is built on?',
                     "Which network connectivity is provisioned for Clearpass Guest?",
                     "What is the use of airgroup?",
                     "What are cookies used for?",
                     'Is Windows Server 2008 "Server Core" appropriate for a SQL Server instance?',
                     "Is there any list of the network devices supported by clearpass for 802.1x auth",
                     "How can I Block my users from installing new virtual machines",
                     "Is there any list of medical devices compatible with clearpass ?",
                     "what are Good branching and merging tutorials for TortoiseSVN?",
                     "how to Add scripting functionality to .NET applications",
                     "why is VMWare Server Under Linux Secondary NIC connection",
                     "Setting up Continuous Integration with SVN",
                     "Does CruiseControl.NET run on IIS 7.0?",
                     "what to do  when there are users in both Edmonton and Toronto that access the same “Corpnet” Wireless LAN.",
                     "what are the  three hardware appliance platforms that aruba provides?",
                     "how to Powering Off the ClearPass Hardware Appliance?",
                     "what are the Supported Hypervisors for clearpass?"
                    )


   generic_questions = [(x, 'generic') for x in generic_questions]
   technical_questions = [(x, 'tech') for x in technical_questions]

   training_set = []
   training_set.extend(generic_questions)
   training_set.extend(technical_questions)

   Qclassifier = NaiveBayesClassifier(training_set)
   #print(Qclassifier.show_informative_features(), Qclassifier.labels())

   #test_queries=("What are cookies used for?","what are the Integrated and Third-Party Profiling Methods?","Hi. Good morning","what does dynamic authorisation mean?","Howdy?")
   #for t in test_queries:
   prob_dist = Qclassifier.prob_classify(query)
   #print(t, '\n', prob_dist.max(), prob_dist.prob(prob_dist.max()))
   if(prob_dist.max()=="tech"):
       return "tech"
   elif(prob_dist.max()=="generic"):
       return "generic"
   else:
       return None
    
#print(main("What are cookies used for?"))
