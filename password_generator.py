import random, string
chars=string.ascii_letters + string.digits + string.punctuation
password=''.join(random.choice(chars)for i in range(12))
print("Your password is: ", password)