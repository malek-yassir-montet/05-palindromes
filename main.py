"""Module pour importer l'alphabet minuscule et les nombres"""
from string import ascii_lowercase, digits

def ispalindrome(s):
    """Fonction qui vérifie si un nombre est un palindrome"""
    accents = "àâéèêëîïùûüôöç"
    table = str.maketrans(accents, "aaeeeeiiuuuooc")
    nouveau = ""
    for i in s.lower().translate(table).lower():
        if i in ascii_lowercase + digits:
            nouveau += i

    if nouveau == nouveau[::-1]:
        return True
    return False


def main():
    """Fonction principale appelant la fonction palindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
