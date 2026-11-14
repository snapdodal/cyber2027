ciphertext = "UEKGPVKUVU JCXG FKUEQXGTGF VJCV UQOG DKTFU ECP UGG VJG"

with open("words") as file:
    known_words = {line.strip().lower() for line in file if line.strip()}


def english_score(text):
    sentence_words = text.lower().split()
    count = 0

    for word in sentence_words:
        if word in known_words:
            count += 1

    return count


best_score = -1
best_key = None
best_text = ""

for key in range(26):
    current_try = ""

    for char in ciphertext:
        if "A" <= char <= "Z":
            current_try += chr((ord(char) - ord("A") - key) % 26 + ord("A"))
        else:
            current_try += char

    score = english_score(current_try)
    print(key, "   score:",score, current_try)

    if score > best_score:
        best_score = score
        best_key = key
        best_text = current_try

print("Best key:", best_key)
print("Best score:", best_score)
print("Best text:", best_text)