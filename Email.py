import random
from collections import defaultdict

def build_markov_chain(emails):
    chain = defaultdict(list)
    for email in emails:
        for i in range(len(email) - 1):
            chain[email[i]].append(email[i + 1])
    return chain

def generate_random_email_markov(chain, length=10):
    start = random.choice(list(chain.keys()))
    email = start
    for _ in range(length - 1):
        next_char = random.choice(chain[email[-1]])
        email += next_char
    return email + "@gmail.com"

# Example usage
sample_emails = ["john@example.com", "mary@example.com", "alex@example.com"]
markov_chain = build_markov_chain(sample_emails)
random_email = generate_random_email_markov(markov_chain)
print(random_email)