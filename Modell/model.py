class model:
    def __init__(self, name, gender, language, pitch, volume, orientation, style, complexity, dialect, activation, deactivation):
        self.name = name
        self.gender = gender
        self.language = language
        self.pitch = pitch
        self.volume = volume
        self.orientation = orientation
        self.style = style
        self.complexity = complexity
        self.dialect = dialect
        self.activation = activation
        self.deactivation = deactivation

    def check(self):
        if((self.activation == 0 and self.deactivation != 0) or (self.activation != 0 and self.deactivation == 0)):
            return False       
        return True
        
    pass

