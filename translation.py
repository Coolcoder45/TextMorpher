def maay(text):
    words = text.split()

    new_words = []

    for w in words:

        if len(w) == 3 or len(w) == 4:
            new_word = "yam" + w[::-1] + "may"
            new_words.append(new_word)

        elif w[0] in "aeiou":
            new_word = w + "am"
            new_words.append(new_word)

        else:
            vowel_pos = 0

            for letter in w:

                if letter not in "aeiou":
                    vowel_pos = vowel_pos + 1
                else:
                    break

            cons = w[:vowel_pos]
            the_rest = w[vowel_pos:]
            new_word = the_rest + "^" + cons + "ay"
            new_words.append(new_word)

    new_words = new_words[::-1]
    return(" ".join(new_words))

def rev_maay(text):
    words = text.split()

    words = words[::-1]

    new_words = []

    for w in words:

        if w[:3] == "yam" and w[-3:] == "may":
            w = w[3:-3]
            new_word = w[::-1]
            new_words.append(new_word)

        elif w[-2:] == "am":
            new_word = w[:-2]
            new_words.append(new_word)

        elif w[-2:] == "ay":
            w = w[:-2]
            cap = 0

            for letter in w:

                #if letter.islower():
                if letter != "^":
                    cap = cap + 1
                else:
                    break

            low = w[:cap]
            up = w[cap+1:]
            new_word = up + low
            new_words.append(new_word)

    return(" ".join(new_words).title())