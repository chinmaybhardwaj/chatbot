import nltk
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MyChatBot:
    
    def __init__(self):
        original = ''
        
        with open('chatbot.txt', 'r') as f:
            original = f.read().lower()
        
        # Uncomment next 2 line when using first time
        #nltk.download('punkt') 
        #nltk.download('wordnet')
        
        # Converts original text into a list of sentences
        self.sent_tokens = nltk.sent_tokenize(original)
        # Converts original text into a list of words
        self.word_tokens = nltk.word_tokenize(original)
        
        #
        self.lemmer = nltk.stem.WordNetLemmatizer()  
        #
        self.remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        self.USER_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
        self.BOT_RESPONSES = ["hi", "hey", "hey what's up", "hi there", "hello", "I am glad! You are talking to me"]
        #
        print("BOT: To exit the program, say Bye!")
    
    #WordNet is a semantically-oriented dictionary of English included in NLTK.
#    def LemTokens(self, tokens):
#        return [self.lemmer.lemmatize(token) for token in tokens]
   
   
    def LemNormalize(self, text):
        word_tokn = nltk.word_tokenize(text.lower().translate(self.remove_punct_dict))
        return [self.lemmer.lemmatize(token) for token in word_tokn]
#        return self.LemTokens(nltk.word_tokenize(text.lower().translate(self.remove_punct_dict)))
    
    
    #
    # If the sentence is a greeting relpy with random greeting responses
    #
    def get_random_greeting(self, sentence):
     
        for word in sentence.split():
            if word.lower() in self.USER_INPUTS:
                return random.choice(self.BOT_RESPONSES)
            
            
    # =============================================================================
    #  Get response from the text file scrapped from wikipedia
    # =============================================================================
    
    def get_response(self, user_response):
        bot_response=''
        
        self.sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=self.LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        
        if(req_tfidf==0):
            bot_response = bot_response + "I am sorry! I don't understand you"
            return bot_response
        else:
            bot_response = bot_response + self.sent_tokens[idx]
            return bot_response
        
        
            
    def chatbot_reply(self, user_response):
        reply = ''  
    
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response == 'thanks' or user_response == 'thank you'):
                print("BOT: You are welcome..")
                reply = "You are welcome.."
            else:
                if(self.get_random_greeting(user_response) != None):
                    reply = self.get_random_greeting(user_response)
                    print('BOT:', reply)
                else:
                    reply = self.get_response(user_response)
                    print("BOT:", reply)
                    self.sent_tokens.remove(user_response)
        else:
            reply = "Bye! take care.."
            print("BOT: Bye! take care..")
                
        return reply
        