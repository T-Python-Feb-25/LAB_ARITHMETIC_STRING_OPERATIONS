Sentence:str= "Manchester United"
Word:str= "United"

#The length of the sentence
print("The length of the sentence is: ", len(Sentence))

#The number of index
print("Tne number of index is", Sentence.find(Word))

#The number of times the word appears
print("The number of times has word appears is: ", Sentence.count(Word))

#The sentence in uppercase
print("The sentence with uppercase is", Sentence.upper())

#The sentence in lowercase
print("The sentence with lowercase is", Sentence.lower())

#The sentence with the word replaced
print(Sentence.replace("United", "City"))
