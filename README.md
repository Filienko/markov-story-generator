# markov-story-generator
NLP predicting project utilizing probabilistic Machine Learning model, markov trigram

For the arguments, you can alter the text sources on which the Markov Model will be changed by specifying the
system path to a folder with text, or simply putting new text in the texts folder.
Alternatively, to alternate the length of the story, utilize second argument and change it to number of tokens you desire to
further predict-generate
If you prefer to use a custom word to start the story, you can use use 3rd argument and input the new word.

Remember the word should be encountered in the novel before for hte probabilistic model to utilize, as I am
utilizing Markov without a certain corresponding smoothing

For the example novel generated, output.txt
