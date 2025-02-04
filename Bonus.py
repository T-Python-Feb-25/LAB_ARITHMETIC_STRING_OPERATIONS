
sentence = "Learning Python is fun because Python is very versatile and powerful."


word = "Python"

 
print(f"Length of the sentence: {len(sentence)}")


print(f"First occurrence of the word '{word}': {sentence.find(word)}")


print(f"Number of times the word '{word}' appears: {sentence.count(word)}")
                                                    
print(f"Sentence in uppercase: {sentence.upper()}")


print(f"Sentence in lowercase: {sentence.lower()}")

new_word = "programming"
new_sentence = sentence.replace(word, new_word)
print(f"Sentence after replacing '{word}' with '{new_word}': {new_sentence}")


print(f"Last character of the sentence: '{sentence[-1]}'")