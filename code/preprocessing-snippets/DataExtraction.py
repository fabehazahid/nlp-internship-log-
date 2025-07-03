import re

# Step 1: Create a sample .txt file
def create_sample_file(filename="data.txt"):
    content = """
Name: Fabeha Zahid
Email: fab.zahid123@gmail.com
Phone: +92-300-1234567

---
Name: Usman Tariq
Email: tariq_990@yahoo.com
Phone: +92-333-8889987

---
Random note: Please call after 5PM.
Contact: Sara, Phone: 0321-5554444, Email: sara_k@outlook.com

---
Note: No email provided.
Name: Adeel Khan
Phone: 0300-7865432

---
Messy Entry: phone is 0345 9988776 and email = weird.mail+test@domain.co.uk
"""
    with open(filename, "w") as file:
        file.write(content.strip())

# Step 2: Extract data using regex
def extract_data_from_file(filename="data.txt"):
    with open(filename, "r") as file:
        text = file.read()

    # Regex patterns
    name_pattern = r"Name:\s*(.+)"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"((?:\+92[-\s]?|0)?3\d{2}[-\s]?\d{7})"

    names = re.findall(name_pattern, text)
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    # Output
    print("Names:")
    for name in names:
        print(f"- {name.strip()}")

    print("\nEmails:")
    for email in emails:
        print(f"- {email}")

    print("\nPhone Numbers:")
    for phone in phones:
        print(f"- {phone}")

# Run the script
create_sample_file()
extract_data_from_file()
