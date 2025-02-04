#10 words
sentence = "Success comes from hard work patience perseverance and continuous learning"

#1 word 
word = "hard"

#prints 
print("length of sentence:", len(sentence))

print("Index of first occurrence of the word:", sentence.find(word))

print("Number of occurrences of the word:", sentence.count(word))

print("Sentence in uppercase:", sentence.upper())

print("Sentence in lowercase:", sentence.lower())

#replace word 
new_sentence = sentence.replace(word, "easy")

#print 
print("Modified sentence:", new_sentence)

print("Last character of the sentence:", sentence[-1])