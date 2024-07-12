import random
import string

class RandomMail:
    @staticmethod
    def generate_mail():
        domains = ["example.com", "test.com", "mail.com", "mail.ru", "ya.ru"]
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))
        domain = random.choice(domains)
        return f"{name}@{domain}"

random_mail = RandomMail()

