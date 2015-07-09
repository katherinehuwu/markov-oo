import sys
import random 


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        # your code here
        text_file = open(filenames).read()
        corpus = text_file.split()
        return corpus


    def make_chains(self, corpus, n=2):
        """Takes input text as string; stores chains."""

        # your code here
        length_full_text = len(corpus)-n
        ngrams = {}
        for i in range(length_full_text):
            pre_tup = []
            for j in range(n):
                pre_tup.append(corpus[i+j])
            tup = tuple(pre_tup)
            ngrams.setdefault(tup,[]).append(corpus[i+n])

        return ngrams

    def make_text(self, chains, n=2):
        """Takes dictionary of markov chains; returns random text."""

        # your code here
        start = random.choice(chains.keys())
        while start[0][0].isupper() == False:
            start = random.choice(chains.keys())
        first_word = list(start[-(n-1):]) 
        next = random.choice(chains[start])
        result = list(start)
        result.append(next)


        while next[-1] != "." and next[-1]!= "?" and next[-1]!= "!"  :
            new = tuple(first_word+[next]) #should be list converted to tuple--make sure it create n tuple
            next_word = random.choice(chains[new]) #check to see if changing variable "next" works
            result.append(next_word)
            first_word = result[-n:-1] #first_word returns n-1 words
            next = result[-1]


        return " ".join(result)     

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    functions = sys.argv[0]
    text = sys.argv[1]
    # we should make an instance of the class
    generator1 = SimpleMarkovGenerator()
    # we should call the read_files method with the list of filenames
    chain_list = generator1.read_files(text)
    chain_dict = generator1.make_chains(chain_list)
    # we should call the make_text method 5x
    for i in range(5):
        print generator1.make_text(chain_dict)
    pass