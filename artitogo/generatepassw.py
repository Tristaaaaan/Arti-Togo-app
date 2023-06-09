import hashlib


class Password:
    def __init__(self):
        pass

    def generate_passw(self, user_id):

        salt = "av3g1gj1"

        # Concatenate the user ID and salt
        salted_input = user_id + salt

        # Hash the salted input using SHA-256
        hashed_value = hashlib.sha256(salted_input.encode()).hexdigest()

        # Extract the first 11 digits from the hashed value
        passw = hashed_value[:11]

        return passw

hehe = Password()

print(hehe.generate_passw('20789239'))
