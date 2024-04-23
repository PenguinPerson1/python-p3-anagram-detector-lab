# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,match_list):
        return_list = []
        for item in match_list:
            if(sorted([*self.word])==sorted([*item])):
                return_list.append(item)
        return return_list