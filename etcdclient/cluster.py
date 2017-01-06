import time

import service as _service

from instance import Instance
from state_machine import StateMachine
from descriptor import BaseDescriptor

STATES = ['starting', 'active', 'host-error', 'stopping', 'stopped']
PARITION_TYPES = ['none', 'key-space', 'hash-key-space']

# Optionals: If no region, then global; if no site then regional
REQUIRED = ['name',
            'min_count',
            'max_count',
            'partition_type',
            'partition_key']


class Descriptor(BaseDescriptor):
    def __init__(self, app, **kwargs):
        BaseDescriptor.__init__(self)
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
        self.validate_init(app) 


    def base_path(self):
        return 'clusters'


    def validate_init(self, app):
        BaseDescriptor.validate_init(self, app)
        self.check_required(REQUIRED)
        self.check_enum('partition_type', PARITION_TYPES)


class Cluster(Instance):
    def __init__(self, app, **kwargs):
        Instance.__init__(self)
        self.desc = ClusterDesc(app, **kwargs)
        self.app = app
        self.bind_property('path', lambda: None)


