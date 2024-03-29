from xml.etree import ElementTree as ET

class XMLTreeNotPrunedError(BaseException):
    def __init__(self, message=None):
        BaseException.__init__(self, message)

class ContinueHereError(BaseException):
    def __init__(self, message=None):
        BaseException.__init__(self, message)

class XMLMonster(object):
    """
    XMLMonster contains functions to read and write XML files that contain
    genealogical data. You should only be using it for first runs or dealing
    with backups. You can't add incremental data as yet

    Functions:
        read(filename) - This reads the XML files and stores the data as a list
                         of Person objects
        write() - Not implemented
        link() - Goes through the list generated by read() and links family
                 members together
        prune() - This needs to be run before the data can be used. It goes
                  through the linked data and makes sure that unique links are
                  indeed unique, and that there are no loose nodes
    """

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
        self.tree = ET.parse(self.filename)
        root = self.tree.getroot()
        self.data = [{}] * len(root.getchildren())
        for index,person in enumerate(root.getchildren()):
            for attribute in person.getchildren():
                self.data[index][attribute.tag] = attribute.text
        self._pruned = False

    def write(self):
        """
        Writes the family tree stored in the database into an XML file
        """
        pass

    def link(self):
        """
        Goes through the input data and links people to one another
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

