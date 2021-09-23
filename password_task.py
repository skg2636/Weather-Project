def validatePassword(s1, s2):
    uc, lc, d, s = 0, 0, 0, 0

    if s1 == s2:
        if len(s1) >= 6:
            for _ in s1:
                if _.islower():
                    lc += 1
                if _.isupper():
                    uc += 1
                if _.isdigit():
                    d += 1
                if _ in ['!', '@', '#', '$', '^', '&', '*', '(', ')', '_', '-']:
                    s += 1
            if uc >= 1 and lc >= 1 and d >= 1 and s >= 1:
                return True, "Success"
            else:
                return False, "Invalid Password"
        else:
            return False, "Password too short"
    else:
        return False, "Password doesn't matches"




def encryptPassword(password):
    original = password
    encryptedPass = 0
    for i in original:
        encryptedPass += (((ord(i)%19)+16)*5*556 )+200
    return str(encryptedPass)


