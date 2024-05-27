#Define class Anagram
#initialize the class with a word argument
#Property for word- create a property for word to store and retrieve the initialized word
#Define match method that takes a list of words
# For each word:
#     check if is an anagram of the initialized word
#     if it is, add it to the result list
    
# Return the list of anagrams

class Anagram:
    def __init__(self, word):
        self.word = word
    
    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        self._word = word
        
    def match(self, wordlist):
        anagrams=[]
        sorted_word = sorted(self.word)
        
        for word in wordlist:
            if sorted(word.lower()) == sorted_word:
                anagrams.append(word)
        
        return anagrams
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana', 'silent']))