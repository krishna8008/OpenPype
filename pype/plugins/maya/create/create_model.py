import avalon.maya


class CreateModel(avalon.maya.Creator):
    """Polygonal static geometry"""

    name = "modelMain"
    label = "Model"
    family = "model"
    icon = "cube"
    defaults = ["Main", "Proxy"]

    def __init__(self, *args, **kwargs):
        super(CreateModel, self).__init__(*args, **kwargs)

        # Vertex colors with the geometry
        self.data["writeColorSets"] = False

        # Include attributes by attribute name or prefix
        self.data["attr"] = ""
        self.data["attrPrefix"] = ""

        # Whether to include parent hierarchy of nodes in the instance
        self.data["includeParentHierarchy"] = False
