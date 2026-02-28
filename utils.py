import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def calculate_keyword_match(resume_text, job_description):
    resume_words = resume_text.lower().split()
    jd_words = job_description.lower().split()

    matched = set(resume_words).intersection(set(jd_words))

    if len(jd_words) == 0:
        return 0

    match_percentage = (len(matched) / len(set(jd_words))) * 100
    return round(match_percentage, 2)