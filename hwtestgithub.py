Class flowers:
def __init__(self, name, color, season, height):
    self.name = name
    self.color = color
    self.season = season
    self.height = height
    def grow(self):
        return 'i can grow!'
    def get_name(self):
        return f'Hello! I am a pretty flower! I am called {self.name}.'
flower1 = flowers('rose', 'red', 'summer', 'midium')
flower2 = flowers('tulip', 'pink', 'spring', 'low')
print(flower1.name)
print(flower1.get_name())
print(flower2.name)
