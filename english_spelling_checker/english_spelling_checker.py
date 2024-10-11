from spellchecker import SpellChecker
import re 

# Initialize the spell checker
spell = SpellChecker()

# The input string with some misspelled words
string = "Applee Oranje Lotues schol Elephant Car"

# Use regular expression to extract words from the string
docx = re.findall("[a-zA-Z]+", string)
print(docx)  # Print the list of words extracted

# Find the misspelled words in the document
misspelled = spell.unknown(docx)

# For each misspelled word, print the correction and possible corrections
for word in misspelled:
    print(word, "-->", spell.correction(word))  # Print the corrected word
    print(spell.candidates(word), end="\n\n")  # Print possible corrections