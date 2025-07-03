import re

def extract_contacts(text):
    # Email regex pattern
    email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    
    # Pakistani phone number pattern (with or without +92 or 03)
    phone_pattern = r'\b(?:\+92|0092|0)?3\d{9}\b'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return emails, phones

# Sample input text
sample_text = """
Hi, my name is Fabeha. You can contact me at fabehazahid@gmail.com or reach out to my friend at abcdefg@outlook.com.
My number is 03123456789, and hers is +923123456780.
"""

emails, phones = extract_contacts(sample_text)

print(" Emails Found:")
for email in emails:
    print(" -", email)

print("\n Phone Numbers Found:")
for phone in phones:
    print(" -", phone)
