class New_file(object):

    def __init__(self, name, size, path) -> None:
        self.name = name
        self.size = size
        self.path = path
    
    def __str__(self) -> str:
        return f'{self.name} {self.size} {self.path}'