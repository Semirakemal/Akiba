
import string


def clean_text(text):
    """Convert text to lowercase and remove basic punctuation."""
    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text


def get_words(text):
    """Return a list of words from cleaned text."""
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    return words


def count_words(text):
    """Count the words in the paragraph."""
    words = get_words(text)
    return len(words)


def count_characters(text):
    """Count characters excluding whitespace."""
    count = 0

    for character in text:
        if not character.isspace():
            count += 1

    return count


def count_vowels_consonants(text):
    """Count vowels and consonants, ignoring case."""
    vowels = 0
    consonants = 0

    for character in text.lower():
        if character in "aeiou":
            vowels += 1
        elif character.isalpha():
            consonants += 1

    return vowels, consonants


def find_longest_word(text):
    """Return the longest word in the paragraph."""
    words = get_words(text)

    if len(words) == 0:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def count_word_frequency(text):
    """Count how many times each word appears."""
    words = get_words(text)
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def find_repeated_words(text):
    """Return words that appear more than once."""
    frequency = count_word_frequency(text)
    repeated = []

    for word, count in frequency.items():
        if count > 1:
            repeated.append(word)

    return repeated


def five_most_frequent_words(text):
    """Return up to five most frequent words without external libraries."""
    frequency = count_word_frequency(text)
    sorted_words = []

    # Put each word into a list with its frequency.
    for word, count in frequency.items():
        sorted_words.append([word, count])

    # Sort by frequency, highest first.
    # If frequencies tie, alphabetical order is used.
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if (
                sorted_words[j][1] > sorted_words[i][1]
                or (
                    sorted_words[j][1] == sorted_words[i][1]
                    and sorted_words[j][0] < sorted_words[i][0]
                )
            ):
                sorted_words[i], sorted_words[j] = (
                    sorted_words[j],
                    sorted_words[i]
                )

    return sorted_words[:5]


def analyze_text(text):
    """Generate and display the complete text analysis."""

    words = get_words(text)
    frequency = count_word_frequency(text)
    vowels, consonants = count_vowels_consonants(text)
    repeated = find_repeated_words(text)
    top_words = five_most_frequent_words(text)

    print("\nTEXT ANALYSIS")
    print("=" * 40)

    print("Original text:", text)
    print("Word count:", count_words(text))
    print("Characters excluding whitespace:", count_characters(text))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest word:", find_longest_word(text))

    print("\nWord frequencies:")
    if len(frequency) == 0:
        print("No words found.")
    else:
        for word, count in frequency.items():
            print(f"{word}: {count}")

    print("\nRepeated words:")
    if len(repeated) == 0:
        print("None")
    else:
        print(", ".join(repeated))

    print("\nFive most frequent words:")
    if len(top_words) == 0:
        print("No words found.")
    else:
        for word, count in top_words:
            print(f"{word}: {count} time(s)")


def main():
    print("TEXT STATISTICS AND WORD ANALYZER")
    print("=" * 40)

    text = input("Enter a paragraph: ")

    analyze_text(text)


if __name__ == "__main__":
    main()
