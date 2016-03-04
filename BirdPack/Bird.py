class Bird(object):
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call

    def details(self):
        return 'A %s goes %s' % (self.kind, self.call)