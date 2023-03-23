
import docx2txt
import nltk
nltk.download('punkt')
nltk.download('stopwords')
 
# you may read the database from a csv file or some other database
SKILLS_DB = [
    'machine learning',
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
    "tensorflow", "keras", "pytorch", "opencv", "reactjs", "pythonqt", "opengl", "openmp", "mpi", "android studio", "pandas"
    ]
 
 
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
 
    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
 
    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
 
    # we create a set to keep the results in.
    found_skills = set()
 
    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token.lower())
 
    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills
 
 
if __name__ == '__main__':
    text = extract_text_from_docx('resume.docx')
    skills = extract_skills(text)
 
    print(skills)  # noqa: T001
 