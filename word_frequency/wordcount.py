import os
import string

os.chdir('.\word_frequency')

def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def save_word_count(word_count, filename):
    with open(filename, 'w') as file:
        for word, count in word_count.items():
            file.write(f'{word}:{count}\n')

def main():
    filename = 'sample.txt'
    text = load_file(filename)
    clean_text = remove_punctuation(text)
    word_count = count_words(clean_text)
    save_word_count(word_count, 'wordcount.txt')
    print(text)
    print(word_count)

if __name__ == '__main__':
    main()