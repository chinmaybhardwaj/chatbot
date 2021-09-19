from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import nltk

# =============================================================================
# Parse HTML and enitre body text
# URL: https://en.wikipedia.org/wiki/
# =============================================================================

class MyWikiScrapper:
    
    base_url = 'https://en.wikipedia.org/wiki/'
    
    def __init__(self):

        self.get_wiki_detail(text='Tesla')
    
    #
    # Request HTML page for url
    #
    def get_wiki_page(self, keyword=''):
        url = self.base_url + keyword
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        
        return soup
    
    def tag_visible(self, element):
        # kill all script and style elements
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    
    #
    # Parse HTMl to get list of all movies and their title, link, cast, genre, production
    #
    def parse_html(self, soup):    
        
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)

        return u" ".join(t.strip() for t in visible_texts)
    
    #
    # Save the movie details in year_name.csv
    #
    def save_to_file(self, result):        
        # Write DataFrame to chatbot.txt
        result = result.strip().ljust(30)
        with open("chatbot.txt", "w") as file:
            file.write(result)
    
        print(__name__, 'chatbot.txt', 'csv created!')  
        
    def get_keywords(self, text):
        keyword = text
    
    
    
        return keyword
    
        
    #
    # Main function to check if csv/html file exists or not.
    # If file does not exist request html page and parse response
    #
    def get_wiki_detail(self, text=''):
        keyword = self.get_keywords(text)
        soup = self.get_wiki_page(keyword = keyword) 
        result = self.parse_html(soup)
        self.save_to_file(result)
      
    
            
if __name__ == '__main__':
    MyWikiScrapper()