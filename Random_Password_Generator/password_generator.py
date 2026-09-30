import string
import secrets


def generate_password():
    length = secrets.randbelow(7) + 10

    special_characters = "!@#$%^&*"

    characters = (
        string.ascii_letters
        + string.digits
        + special_characters
    )

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(special_characters)
    ]

    password += [
        secrets.choice(characters)
        for _ in range(length - 4)
    ]

    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return ''.join(password)


if __name__ == "__main__":
    print(generate_password())
