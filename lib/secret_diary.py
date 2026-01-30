class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        return self.diary.read() if self.locked == False else 'Go away!'

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False