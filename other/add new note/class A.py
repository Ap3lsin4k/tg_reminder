global lang
lang = '1'
print(lang)
class NOTE:
    global lang
    lang = '2'
    def __init__(self, lang):
        self.lang = lang
        print(lang)
        print(self.lang)

    def out(self):
        print(self.lang)
pitbul = NOTE("3")
print(lang)
lang = '4'
pitbul.out()
