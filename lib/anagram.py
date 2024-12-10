class Anagram:
    def __init__(self, word):
        # Store the sorted version of the input word for comparison
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, word_list):
        # Filter and return words that are anagrams of the stored word
        return [
            word for word in word_list
            if word.lower() != self.word and sorted(word.lower()) == self.sorted_word
        ]
