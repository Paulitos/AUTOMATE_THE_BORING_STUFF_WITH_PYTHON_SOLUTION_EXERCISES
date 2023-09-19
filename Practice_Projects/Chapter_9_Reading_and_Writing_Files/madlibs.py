# madlibs Page 224 Chapter 9
import sys, re

# Open and read the text file
if len(sys.argv) == 2:
    print('Opening text file...')
    with open(sys.argv[1]) as textSource:
        textContent = textSource.read()
else:
    print('Usage: madlibs.py <textSource>')
    sys.exit(1)

# Define a regular expression pattern for the keywords
keywordRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB', re.I)

# Find all matches in the text content
matches = keywordRegex.findall(textContent)

# Create a copy of matches to store user inputs
answers = list(matches)

# Prompt the user to replace keywords with their input
for i in range(len(matches)):
    replacement = input(f"Enter an {matches[i].lower()}: ")
    textContent = keywordRegex.sub(replacement, textContent, count=1)

print(textContent)

# Save the modified text to a new file
with open('madlib_result.txt', 'w') as textEdited:
    textEdited.write(textContent)



