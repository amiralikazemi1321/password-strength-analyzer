common_passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "123123", "1234567890", "000000", "qwerty123", "1q2w3e4r", "abc123", "password1", "iloveyou", "admin", "welcome", "monkey", "login", "dragon", "master", "football", "letmein", "princess", "qwertyuiop", "solo", "starwars", "passw0rd", "hello", "freedom", "whatever", "trustno1", "654321", "666666", "112233", "121212", "987654321", "00000000", "password123", "admin123", "welcome123", "qwerty1", "qwerty12", "qwerty1234", "abc1234", "abc12345", "123321", "123456789a", "123456a", "12345678a", "1234567890a", "11111111", "111111111", "222222", "22222222", "333333", "33333333", "444444", "44444444", "555555", "55555555", "777777", "77777777", "888888", "88888888", "999999", "99999999", "987654", "98765432", "123654", "159753", "147258369", "2580", "1230", "1234qwer", "qwer1234", "qwertyui", "asdfgh", "asdfghjkl", "zxcvbn", "zxcvbnm", "asdf1234", "qazwsx", "qazwsxedc", "1qaz2wsx", "1qazxsw2", "qwe123", "qweasd", "qweasdzxc", "zaq12wsx", "wsx123", "test", "test123", "test1234", "testing", "guest", "guest123", "user", "user123", "root", "root123", "administrator", "administrator123", "default", "default123", "changeme", "secret", "secret123", "login123", "pass", "pass123", "pass1234", "password12", "password1234", "password2020", "password2021", "password2022", "password2023", "password2024", "password2025", "password2026", "passwd", "passwd123", "passw0rd123", "p@ssword", "p@ssw0rd", "p@ssword123", "welcome1", "welcome12", "welcome1234", "hello123", "hello1234", "helloworld", "helloworld123", "iloveyou1", "iloveyou123", "loveme", "loveyou", "love123", "summer", "summer123", "winter", "winter123", "spring", "spring123", "autumn", "autumn123", "sunshine", "shine1", "sunshine123", "flower", "flower123", "princess1", "princess123", "pokemon", "pokemon123", "pokemon1", "minecraft", "minecraft123", "minecraft1", "computer", "computer123", "internet", "internet123", "qwerty2020", "qwerty2021", "qwerty2022", "qwerty2023", "qwerty2024", "qwerty2025", "qwerty2026", "football1", "football123", "soccer", "soccer123", "baseball", "baseball123", "basketball", "basketball123", "hockey", "hockey123", "liverpool", "chelsea", "arsenal", "barcelona", "real madrid", "manchester", "superman", "batman", "batman123", "spiderman", "spiderman123", "pokemon123", "shadow", "shadow123", "killer", "killer123", "computer1", "internet1", "whatever1", "freedom1", "trustno1", "master123", "dragon123", "monkey123", "letmein123", "login123", "adminadmin", "adminadmin123", "admin1", "admin12", "admin2020", "admin2021", "admin2022", "admin2023", "admin2024", "admin2025", "admin2026", "123456789!", "12345678!", "password!", "Password1", "Password123", "Password123!", "Qwerty123", "Qwerty123!", "Admin123", "Admin123!", "Welcome123", "Welcome123!", "Test123", "Test123!", "User123", "User123!", "123abc", "123abc456", "abc123456", "abcd1234", "abcd12345", "abcdef", "abcdefg", "abcdef123", "abcdef1234", "qwerty12345", "qwerty123456", "12345678910", "12345678901", "101010", "10101010", "112358", "11235813", "131313", "232323", "343434", "454545", "565656", "676767", "787878", "898989", "909090", "121314", "123789", "456789", "6543210", "0987654321", "000000000", "1111111111"]
i = input('enter password: ')

def check_common():
    if i in common_passwords:
        print('your password is bad')
        return False
    else:
        print('correct')
        return True

def check_len():
    if len(i) < 8:
        print('your password is short and bad')
        return False
    else:
        print('correct')
        return True

def check_digit():
    if any(c.isdigit() for c in i):
        print('has number')
        return True
    else:
        print('add number')
        return False

def check_capital():
    if any(c.isupper() for c in i):
        print("Has uppercase")
        return True
    else:
        print("No uppercase add a capital letter")
        return False

def check_lowercase():
    if any(c.islower() for c in i):
        print('Has lowercase')
        return True
    else:
        print('No lowercase add a lowercase letter')
        return False

def check_special_character():
    if any(not c.isalnum() for c in i):
        print('correct')
        return True
    else:
        print('add special character')
        return False

res1 = check_common()
res2 = check_len()
res3 = check_digit()
res4 = check_capital()
res5 = check_lowercase()
res6 = check_special_character()

n = 0

if res1:
    n += 1

if res2:
    n += 1

if res3:
    n += 1

if res4:
    n += 1

if res5:
    n += 1

if res6:
    n += 1

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)

if n <= 2:
    strength = "Weak"
elif n <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print(f"result = {n}/6")
print(f"strength = {strength}")