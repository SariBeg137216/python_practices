import random
import string
import secrets

# for i in range(3):
#     print(random.randrange(100, 999, 5))
# tickets = []
# for i in range(1000):
#     tickets.append(random.randrange(100000000, 999999999))
#
# winner = random.sample(tickets, 2)
# print(winner)

# secretGenerator = secrets.SystemRandom()
# OTP = secretGenerator.randrange(100000, 999999)
#
# print(OTP)
#
# name = 'pynative'
# print(random.choice(name))

# str_rand = string.ascii_letters + string.ascii_uppercase
# my_chars = random.sample(str_rand, 5)
# for char in my_chars:
#     print(''.join(char), end="")


string_password = string.ascii_uppercase + string.digits + string.punctuation
password = random.sample(string_password, 10)



