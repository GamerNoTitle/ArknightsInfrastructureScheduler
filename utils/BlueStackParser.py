from utils.PropertiesParser import parse

class BlueStack():
    def __init__(self, pos):
        self.config = pos
        self.port = parse(self.config).get('bst.instance.Nougat64.status.adb_port', '5555')