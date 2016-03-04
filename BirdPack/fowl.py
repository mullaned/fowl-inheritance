from BirdPack.Bird import Bird

class Fowl(Bird):
    def __init__(self, kind, call,fowltype):
        self.fowltypes = {
                            'landfowl': 'Landfowl are heavy birds',
                            'waterfowl': 'Waterfowl have 180 species'
                        }
        self.fowltype = fowltype
        super(Fowl, self).__init__(kind, call)

    def details(self):
        return super(Fowl,self).details() + '\n' + 'Some interesting facts about the %s : A %s is of type of %s and %s' \
                                                   % (self.kind, self.kind, self.fowltype,
                                                        self.fowltypes[self.fowltype.lower()])
