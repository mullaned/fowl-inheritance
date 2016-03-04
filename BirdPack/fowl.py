from BirdPack.Bird import Bird

class Fowl(Bird):
    def __init__(self, kind, call,fowltype):
        self.type = fowltype
        super(Fowl, self).__init__(kind, call)

    def details(self):
        return super(Fowl,self).details() + ' and is a %s' % self.type
