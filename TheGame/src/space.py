from publicExposure import PublicExposure


class Space:

    def __init__(self):
        self.operations = []
        self.isOpen = False
        self.sizeInSqm = 0
        self.publicExposure = PublicExposure.MINIMUM
        self.infrastructure = []
        self.direction = None
