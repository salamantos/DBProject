class DBAccessError(Exception):
    def __init__(self, text):
        self.text = text
