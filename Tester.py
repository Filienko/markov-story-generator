# tester file that reads input files, connects to the Markov source code, and generates the output story
import os
import sys
from Markov import Markov
import string
import re

texts = ''
text_source = '/texts'
starting_word = ""

# Determine the size of the future text
n = 2000

# For the arguments, you can alter the text sources on which the Markov Model will be changed by specifying the
# system path to a folder with text, or simply putting new text in the texts folder.
# Alternatively, to alternate the length of the story, utilize second argument and change it to number of tokens you desire to
# further predict-generate
# If you prefer to use a custom word to start the story, you can use use 3rd argument and input the new word.

# Remember the word should be encountered in the novel before for hte probabilistic model to utilize, as I am
# utilizing Markov without a certain corresponding smoothing



def process_novel(file_text: str) -> str:
    file_text = " ".join(file_text.split())
    punct = string.punctuation
    # Currently, experimenting with keeping lexically important punctuation mark
    file_text = file_text.lower()
    punct = punct.replace("'", "")
    # punct = punct.replace('?', '')
    # punct = punct.replace('.', '')
    file_text = re.sub("\n|\r", " ", file_text)
    file_text = re.sub(' +', ' ', file_text)
    translating = str.maketrans(punct, ' ' * len(punct))
    file_text = file_text.translate(translating)
    file_text = re.sub(' +', ' ', file_text)
    return file_text


# Initiated the main python solving test program
if __name__ == '__main__':
    # Before proceeding with the provided empty values
    if len(sys.argv) > 1:
        text_source = sys.argv[1]
    if len(sys.argv) > 2:
        n = sys.argv[2]
    if len(sys.argv) > 3:
        starting_word = sys.argv[3]

    # read the book files
    for file in os.listdir(os.getcwd() + text_source):
        with open(os.path.join(os.getcwd() + text_source, file), 'r') as f:
            # preprocess the file to our favor
            text: str = f.read()
            text = process_novel(text)
            texts += text

    # Initialize the nlp markov chain
    markov_chain = Markov(texts, n)
    markov_chain.initialize(starting_word)

exit()
