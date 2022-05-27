phrase = input()
if ':)' in phrase:
    phrase = phrase.replace(':)', '🙂')
if ':(' in phrase:
    phrase = phrase.replace(':(', '🙁')

print(phrase)