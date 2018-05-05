# Modules
import os

# Set file path
txtpath = os.path.join('raw_data', 'paragraph_1.txt')

# COUNT NUMBER OF WORDS
with open(txtpath) as paragraph:
 
    num_words = 0
    num_sentences = 0
    num_chars = 0
    lines = 0

    for line in paragraph:
        words = line.split()

        num_words += len(words)
        num_chars += len(line)
        lines += 1

        if line.startswith('\n'):
            blanklines += 1
        else:
        # Assume that each sentence ends with . or ! or ?
        # Count these characters
         num_sentences += line.count('.') + line.count('!') + line.count('?')

         #Average word lenght
         average_chars = num_chars/num_words
        
        #Average sentence lenght
        average_sentence = num_words/num_sentences

print("FIRST TEXT ANALYSIS")
print("Number of words: " + str(num_words))
print("Number of sentences: " + str(num_sentences))
print("Average characters per word: " + str(average_chars))
print("Average sentence lenght: "+str(average_sentence))

# Set file path
txtpath2 = os.path.join('raw_data', 'paragraph_2.txt')

# COUNT NUMBER OF WORDS
with open(txtpath2) as paragraph2:
 
    num_words2 = 0
    num_sentences2 = 0
    num_chars2 = 0
    lines2 = 0

    for line in paragraph2:
        words = line.split()

        num_words2 += len(words)
        num_chars2 += len(line)
        lines2 += 1

        # Assume that each sentence ends with . or ! or ?
        # Count these characters
        num_sentences2 += line.count('.') + line.count('!') + line.count('?')

        #Average word lenght
        average_chars2 = num_chars2/num_words2
        
        #Average sentence lenght
        average_sentence2 = num_words2/num_sentences2

print("--------------------------------")
print("SECOND TEXT ANALYSIS")
print("Number of words: " + str(num_words2))
print("Number of sentences: " + str(num_sentences2))
print("Average characters per word: " + str(average_chars2))
print("Average sentence lenght: "+str(average_sentence2))
    