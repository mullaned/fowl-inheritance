from BirdPack.Bird import Bird

class SeaBird(Bird):
    def __init__(self, kind, call, diving_depth):
        self.depth= diving_depth
        super(SeaBird,self).__init__(kind,call)

    def details(self):
        return super(SeaBird, self).details() + ' and dives to a depth of %s metres' % self.depth