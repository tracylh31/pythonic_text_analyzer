from collections import Counter

def read_file(file_name):
    """Read and return the contents of a text file."""
    with open(file_name, "r") as file:
        return file.read()


def process_text(text):
    """Convert text to lowercase and split it into words."""
    return text.lower().split()


def count_words(words):
    """Count how many times each word appears."""
    return Counter(words)


def find_long_words(words):
    """Return words that are longer than three characters."""
    return [word for word in words if len(word) > 3]


def display_results(words, word_counts, long_words):
    """Display the text analysis results."""
    print(f"The total number of words is: {len(words)}")
    print(f"The unique words count is: {len(word_counts)}")
    print("The most frequent words are:")

    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count}")

    print(f"Long words (more than 3 characters): {len(long_words)}")


def main():
    """Run the text analyzer."""
    text = read_file("sample.txt")
    words = process_text(text)
    word_counts = count_words(words)
    long_words = find_long_words(words)
    display_results(words, word_counts, long_words)


if __name__ == "__main__":
    main()