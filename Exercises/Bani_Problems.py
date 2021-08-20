# Removing all vowels
def shorten(s: str):
    ans = ''
    vowels = 'aeiou'
    for letter in s:
        if letter.lower() not in vowels:
            ans += letter
    return ans


print(shorten('Hi, my name is Samin Azhan'))


# Checking dictionary major
def check_major(name: str, major: str, major_dict: dict):
    if major not in major_dict.keys():
        return False
    else:
        if name not in major_dict[major]:
            return False
        else:
            return True


majors_1 = {
    "Engineering": ["Josh", "Robert", "Irene"],
    "Accounting": ["Carol", "Christine", "Charles"],
    "Art History": ["Douglas"],
    "Underwater Basket Weaving": ["Nick"]
}
print("#1", check_major("Douglas", "Art History", majors_1) is True)
print("#2", check_major("Irene", "A Major That Doesn't Exist", majors_1) is False)
print("#3", check_major("Nick", "Underwater Basket Weaving", majors_1) is True)
