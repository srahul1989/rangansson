from xml.etree.ElementTree import parse

class XMLTreeNotPrunedError(BaseException):
    def __init__(self, message=None):
        BaseException.__init__(self, message)


class XMLMonster(object):


    def __init__(self):
        self.filename = None
        self.tree = None
        self._pruned = False
        self._result = None

    def read(self, filename):
        """
        Reads the initial XML file
        """
        self.filename = filename
        self.tree = parse(self.filename)
        self._pruned = False

    def write(self):
        """
        Writes the family tree stored in the database into an XML file
        """
        pass

    def prune(self):
        """
        Go through the newly imported data and make sure there are no unlinked
        nodes and that each link that needs to be unique is unique
        """
        pass

    @property
    def result(self):
        """
        Use this function to obtain the pruned XML data in a nice(TM) format
        """
        if not self._pruned:
            raise XMLTreeNotPrunedError("Run XMLMonster.prune() after reading \
                    XML data to sanitize the data")
        return self._result

