class Views(dict):
    '''A view collection object that store jenkins views'''
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __setitem__(self, name, value):
        self.__dict__[name] = value

    def __getitem__(self, name):
        return self.__dict__[name]
