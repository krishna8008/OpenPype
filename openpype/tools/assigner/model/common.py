class AssignerToolSubModel(object):
    def __init__(self, main_model):
        self._main_model = main_model

    @property
    def event_system(self):
        return self._main_model.event_system
