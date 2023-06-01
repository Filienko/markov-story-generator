import random

import nltk


class Node:
    def __init__(self, value: str, my_children, my_count: int = 1):
        self.my_value: str = value
        self.my_children: list[Node] = my_children
        self.my_count: int = my_count

    def __eq__(self, other):
        return self.my_value == other.my_value


# Source code that implements the hash table/linked structure.
def output(text: str):
    # develop new text with model
    f = open("output.txt", "w")
    f.write(text)
    # Close the new file
    f.close()


class Markov:
    # Could we instead set up nested dictionaries of children, where value of a parent = {child_token: child's children}
    # The graph is parent -> child_n, child_1, rather than parent child1-> children

    def __init__(self, text: str, n: int):
        self.my_text: str = text
        self.my_n: int = n
        self.my_vocab: list[Node] = []

    def prepare_vocab(self):
        # tokenize the text into a list of words
        tokens = nltk.tokenize.word_tokenize(self.my_text)

        for i in range(len(tokens) - 3):
            curr_node = Node(tokens[i + 2], [])

            parent_node = Node(tokens[i + 1], [])
            parent_node.my_children.append(curr_node)

            grandparent_node = Node(tokens[i], [])
            grandparent_node.my_children.append(parent_node)

            # Updating the count and also child str list if elements exists, if no = create

            # nodes = [x for x in self.my_vocab if x.my_value == tokens[i]]
            item = next((x for x in self.my_vocab if x.my_value == tokens[i]), None)

            if item is None:
                self.my_vocab.append(grandparent_node)
            else:
                # Assuming 1 non-duplicate node
                child_nodes = item.my_children
                item = next((x for x in child_nodes if x.my_value == tokens[i + 1]), None)
                if item is None:
                    child_nodes.append(parent_node)
                else:
                    # Assuming 1 non-duplicate node
                    item.my_count = item.my_count + 1
                    item.my_children.sort(key=lambda x: x.my_count, reverse=True)
                    child_nodes = item.my_children
                    item = next((x for x in child_nodes if x.my_value == tokens[i + 2]), None)
                    if item is None:
                        child_nodes.append(curr_node)
                    else:
                        item.my_count = item.my_count + 1
                        item.my_children.sort(key=lambda x: x.my_count, reverse=True)

    def produce_output(self, n: int, starting_words: str) -> str:
        # Produce n words given the 2 starting text tokens
        answer: str = starting_words
        i: int = 0
        while i < n:
            last_binary_tokens = nltk.tokenize.word_tokenize(answer)[-2:]
            answer += self.predict_word(last_binary_tokens)
            i += 1

        return answer

    def predict_word(self, bi_param: list[str]) -> str:
        potential_answers: list[Node] = []

        for word_node in self.my_vocab:
            if bi_param[0] == word_node.my_value:
                children = word_node.my_children
                for child_node in children:
                    if bi_param[1] == child_node.my_value:
                        potential_answers.extend(child_node.my_children)

        top = 0
        # Returns random of top n most statistically probable text tokens, given the length of the options
        if len(potential_answers) > 6:
            top = 6
        elif len(potential_answers) > 3:
            top = 3
        elif len(potential_answers) > 2:
            top = 2

        answer: str = " " + potential_answers[random.randint(0, top)].my_value

        return answer

    def initialize(self, starting_words: str):
        self.prepare_vocab()
        if not starting_words:
            starting_words = self.my_vocab[random.randint(0, len(self.my_vocab) - 1)].my_value

        item = next((x for x in self.my_vocab if x.my_value == starting_words), None)
        # Choosing highest probable next word
        starting_words += " " + item.my_children[0].my_value
        answer = self.produce_output(self.my_n, starting_words)
        output(answer)
