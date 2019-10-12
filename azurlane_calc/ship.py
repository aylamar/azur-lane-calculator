class VangShip:
    def __init__(self, name, level, mvp, morale):
        self.name = name
        self.level = level
        self.mvp = mvp
        self.morale = morale

class MainShip:
    def __init__(self, name, level, mvp, morale, flagship):
        self.name = name
        self.level = level
        self.mvp = mvp
        self.morale = morale
        self.flagship = flagship