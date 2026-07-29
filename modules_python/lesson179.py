import secrets
import string as s
from secrets import SystemRandom as Sr

print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

random = secrets.SystemRandom()

print(secrets.randbelow(100))
print(secrets.choice([10, 20, 30]))

