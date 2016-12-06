import time

from desc import Desc

STATES = ['starting', 'active', 'host-error', 'stopping', 'stopped']
PARITION_TYPES = ['none', 'key-space', 'hash-key-space']

# Optionals: If no region, then global; if no site then regional
REQUIRED = ['name',
            'min_count',
            'max_count',
            'partition_type',
            'partition_key']


class ClusterDesc(Desc):
    def __init__(self, context, **kwargs):
        Desc.__init__(self)
        self.name = kwargs.get('name')
        self.region = kwargs.get('region')
        self.site = kwargs.get('site')
        self.state = STATES[0]
        self.created = time.time()
        self.modified = time.time()
        self.min_count = kwargs.get('min_count')
        self.max_count = kwargs.get('max_count')
        self.members = []
        self.joining = []
        self.leaving = []
        self.partition_type = kwargs.get('partition_type')
        self.partition_key = kwargs.get('partition_key')
        self.validate_init(context) 


    def base_path(self):
        return 'clusters'


    def validate_init(self, context):
        Desc.validate_init(self, context)
        self.check_required(REQUIRED)
        self.check_enum('partition_type', PARITION_TYPES)

