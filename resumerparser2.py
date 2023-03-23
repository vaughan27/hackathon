import spacy
from spacy.matcher import Matcher

# load the language model
nlp = spacy.load('en_core_web_sm')

# define the matcher to extract name, email, and phone number
matcher = Matcher(nlp.vocab)

# pattern to match names
name_pattern = [{'ORTH': 'name: '},{'POS': 'PROPN'}, {'POS': 'PROPN'}]
matcher.add('Name', [name_pattern])

# pattern to match email addresses
email_pattern = [{'TEXT': {'REGEX': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'}}]
matcher.add('Email', [email_pattern])

# pattern to match phone numbers
phone_pattern = [{'ORTH': '+'}, {'SHAPE': 'dd'}, {'SHAPE': 'ddddd'},{'SHAPE': 'ddddd'}]
matcher.add('phone', [phone_pattern])

# load the resume
with open('resume.txt', 'r') as f:
    resume_text = f.read()

# parse the resume with spaCy
doc = nlp(resume_text)

# iterate over the matches and extract the relevant information
matches = matcher(doc)
for match_id, start, end in matches:
    if nlp.vocab.strings[match_id] == 'Name':
        print('Name:', doc[start:end])
    elif nlp.vocab.strings[match_id] == 'Email':
        print('Email:', doc[start:end])
    elif nlp.vocab.strings[match_id] == 'Phone':
        print('Phone:', doc[start:end])
