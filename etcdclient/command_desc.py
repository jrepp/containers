import time

from desc import Desc

REQUIRED = [
        'region',
        'name',
        'args',
        'user' ]


class CommandDesc(Desc):
    def __init__(self, base_path, context, **kwargs):
        Desc.__init__(self)

        # Commands descriptors are stored as a child under an existing base path
        self._base_path = base_path

        self.region = kwargs.get('region')
        self.site = kwargs.get('site')
        self.name = kwargs.get('name')
        self.args = kwargs.get('args')
        self.user = kwargs.get('user')
        self.created = time.time()
        self.acknowledged = None
        self.pending = None
        self.duration = None
        self.completed = None
        self.validate_init(context)


    def base_path(self):
        return self._base_path

    
    def validate_init(self, context):
        Desc.validate_init(self, context)
        self.check_required(REQUIRED)


