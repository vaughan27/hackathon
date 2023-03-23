import spacy
import re
import pdftotxt

nlp = spacy.load("en_core_web_sm")

# Load resume text
# with open("resume.txt", "r") as f:
#     resume_text = f.read()

# Process resume text with spaCy
doc = nlp(pdftotxt.text)

# Extract name
name = None
for ent in doc.ents:
    if ent.label_ == "PERSON":
        name = ent.text
        break

# Extract email
email = None
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_match = re.search(email_regex, pdftotxt.text)
if email_match:
    email = email_match.group()

# Extract phone number
phone = None
phone_regex = r"\+?\d{2}\s?\d{5}\s?\d{5}"
phone_match = re.search(phone_regex, pdftotxt.text)
if phone_match:
    phone = phone_match.group()

# Extract skills
predefined_skills = ['machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'english',
    "ms office",
    "word", "excel", "outlook", "powerpoint", "access"
    'google drive',
    "docs", "drive", "forms", "gmail", "spreadsheets"
    "excel", "google drive", "open office", "pivot tables", "vertical lookups", "macros"
    ,"filters", "folders",
    "powerpoint", "google slides", "tableau", "keynote"
    "macos", "microsoft windows",
    "css", "wordpress", "seo", "content management", "mailchimp", "google analytics", "moz",
    "java", "javascript", "python", "ruby on rails", "perl", "php", "xml", "c#", "c++", "html",
    "apache", "mysql", "sas", "json", "machine learning", "data mining", "sqlite", "rapidminer", "machine learning", 
    "ms access", "oracle", "teradata", "mysql", "sql", "ibm db2", "sap bi"    
    "bcp", "crm", "e-commerce", "hr management", "erp", "quikbooks", "freshbooks", "xero", 
    "dreamweaver", "illustrator", "indesign", "lightroom", "photoshop", "acrobat", "corel draw", "autocad", "microsoft publisher"
    "hardware configuration", "system administration", "tech support", "software installation", "linux","unix",
    "network automation", "cloud management", "wan/lan", "dns", "dhcp",
    "arm","matlab",
    "ava", "javascript", "ocaml", "prolog", "vhdl", "verilog", "arm assembly", "bash", "sql", "q",
    "tensorflow", "keras", "pytorch", "opencv", "reactjs", "pythonqt", "opengl", "openmp", "mpi", "android studio", "pandas"]
skills = []
for sent in doc.sents:
    for token in sent:
        if token.text.lower() not in ["resume", "name", "email", "phone"] and token.text.lower() in predefined_skills:
            skills.append(token.text)

# Print results
print("Name:", name)
print("Email:", email)
print("Phone number:", phone)
print("Skills:", skills)
