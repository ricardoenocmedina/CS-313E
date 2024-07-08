"""
File: wordleHelperFinalProject.py

Description: The purpose of this program is to help you win at Wordle more consistantly and with less effort.

Student Name: Ricardo Medina

Student UT EID: rem3885

Course Name: CS 313E
"""

INTRO = f"""
--------------------------------------------------------
             Welcome to Wordle Helper!
--------------------------------------------------------"""

CONTROL_MANUAL = """
--------------------------------------------------------
            What services would you like?
--------------------------------------------------------
  1) Autocomplete word based on given prefix. [Type 1]
  2) Find words based on letter and position. [Type 2]
  3) Filter words by letter. [Type 3] 
  4) Filter by letter not in word. [Type 4]
  5) Print out my potential words list. [Type 5]
  6) Exit. [Type 6]
"""

OUTRO = f"""
--------------------------------------------------------
     Thank YOU for using Wordle Helper. Come again!
--------------------------------------------------------"""

from time import time

class TrieNode():
    """Defines the Trie Node class"""
    def __init__(self):
        """Initializes children if is end of word"""
        self.children = {}
        self.is_end_of_word = False

class Trie():
    """Defines the Trie class"""
    def __init__(self):
        """Initializes root"""
        self.root = TrieNode()

    # NOTE: this insert function was directly translated from the pseudocode provided in Zybooks Ch. 39.11
    def insert(self, word):
        """inserts a specified word into the trie"""
        node = self.root
        for char in word:
            # checks for char existence
            if char not in node.children:
                node.children[char] = TrieNode()
            # moves to next node
            node = node.children[char]
        # marks end of the word
        node.is_end_of_word = True

    def search(self, prefix):
        """searches for words with the specified prefix"""
        node = self.root # start of root

        for char in prefix: # iterates over each character in prefix
            if char not in node.children: 
                # checks for character existence
                return [] # not found
            # moves to the next node
            node = node.children[char]

        # returns list of words once all characters in prefix have been found
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix): # uses depth-first search & recusion
        """search helper meant to store a set of words"""
        words = []

        # if the node is the end of the word, appends that word into list
        if node.is_end_of_word:
            words.append(prefix)

        # iterates over children
        for char, child in node.children.items():
            # explores each branch of tree - recursively calls and extends list 
            words.extend(self._collect_words(child, prefix + char))
        return words

    def print_trie(self):
        """prints trie"""
        return self.print_trie_helper(self.root,'')

    def print_trie_helper(self, node, word = ''):
        """helper function to print trie"""
        trie_content = ''

        # checks for end of word
        if node.is_end_of_word:
            trie_content += word + '\n' # forms complete word and concatanates

        # iterates over children
        for char, child in node.children.items():
            # explores each branch of tree - recursively call to append content
            trie_content += self.print_trie_helper(child, word + char)

        return trie_content + '-'

# NOTE: this code was found in Prof. Teymourian's Github
def timer(func):
    """gets the runtime for a specified function"""
    def time_func(*args, **kwargs):
        """gets the runtime for a specified function"""

        before = time()
        ret_val = func(*args, **kwargs)
        after = time()

        print('\nElapsed Time is: ', after - before)
        return ret_val
    return time_func

#@timer
def find_viable_words(lst, letter, pos): # uses linear search
    """returns list of words given a specified letter and position"""
    viable_words = []

    # iterates through every word in list
    for word in lst:
        # appends word if the letter is in the specified position 
        if len(word) == 5 and word[pos] == letter:
            viable_words.append(word)

    return viable_words

def filter_list(lst , letter): # uses linear search
    """returns list of words containing a specified letter in any position"""
    filtered_list = []

    # iterates through every word in list
    for word in lst:
        # appends word to list if it contains specified letter
        if letter in word:
            filtered_list.append(word)
    return filtered_list

def not_in_filter_list(lst, letter):
    """returns list of words that do NOT contain a specified letter"""
    filtered_list = []

    for word in lst:
        # appends word to list if it does NOT contain specified letter
        if letter not in word:
            filtered_list.append(word)
    return filtered_list

def main():
    """Main function"""

    # gets words from txt file and puts it in a nicely formated list
    with open('sgb-words.txt', 'r') as file:
        word_list = file.readlines()
        words = [word.strip() for word in word_list]

    t = Trie() # generates trie

    # insert words into trie
    for word in words:
        t.insert(word)

    print(INTRO)
    # continuous while loop until user types 5 or 6
    while True:
        control = int(input(CONTROL_MANUAL))

        # base case - exits program
        if control == 6:
            print(OUTRO)
            break

        # generates list of words based on the speficied prefix
        elif control == 1:
            prefix = input('\nWhat is the prefix you are looking for? ').lower()
            words = t.search(prefix)
            print(f'Possible words based on the prefix \'{prefix}\': {words}')

        # generates list of words based on a specified word and position
        if control == 2:
            letter = input('\nWhat letter are you looking for? ').lower()
            pos = int(input(f'Where is letter \'{letter}\' located? (1 - 5): ')) - 1

            words = find_viable_words(words, letter, pos)

            print(words)

        # generates list of words that contain a specific letter
        if control == 3:
            letter = input('What letter do you want to filter with? ').lower()
            words = filter_list(words, letter)
            print(words)

        # generates list of words that DO NOT contain specified letter 
        if control == 4:
            letter = input('What letter do you know is not in your list? ').lower()
            words = not_in_filter_list(words, letter)
            print(words)

        # outs a text file of the possible words that your word could be and exits program
        if control == 5:

            t2 = Trie() 

            for word in words:
                t2.insert(word)

            words_list_updated = (t2.print_trie())

            CONTENTS = f"""
            -------------------------
            Your Potential Word List:
            -------------------------

            {words_list_updated}
            """

            with open('wordList.txt', 'w') as file:
                file.write(CONTENTS)
            print('\nYour potential word list has been executed as a text file.')
            print(OUTRO)
            break

if __name__ == '__main__':
    main()
