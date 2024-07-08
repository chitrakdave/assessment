import re

def load_predefined_words(filename):
    with open(filename, 'r') as file:
        predefined_words = {line.strip().lower() for line in file}
    return predefined_words

def find_matches(input_file, predefined_words):
    matches = []
    with open(input_file, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in predefined_words:
                    matches.append(word)
    return matches

def main(predefined_words_file, input_file):
    predefined_words = load_predefined_words(predefined_words_file)
    matches = find_matches(input_file, predefined_words)
    print("Matched words:", matches)

if __name__ == "__main__":
    # Example usage
    predefined_words_file = 'predefined_words.txt' 
    input_file = 'input.txt'
    main(predefined_words_file, input_file)
