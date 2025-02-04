sentence:str = "Real Madrid"
word = "Madrid"

print("length of sentence:",len(sentence))

print("first occurrence of the word in the sentence:",sentence.find(word))

print("number of times the word appears in the sentence:",sentence.count(word))

print("sentence in all uppercase letters:",sentence.upper())

print("sentence in all lowercase letters:",sentence.lower())

print("Replace the word in the sentence:",sentence.replace(word,"Club"))

print("Last character:",sentence[-1])