import time
import json

from instance import Instance
from state_machine import StateMachine
from descriptor import BaseDescriptor

REQUIRED = [ 'name', 
             'ip',
             'ports',
             'service_class',
             'provides' ]

LEADER = 'leader'
MEMBER = 'member'
PROMOTING = 'promoting'
DEMOTING = 'demoting'

ROLES = [   LEADER, 
            MEMBER, 
            PROMOTING, 
            DEMOTING ]

class Descriptor(BaseDescriptor):
    def __init__(self, app, **kwargs):
        BaseDescriptor.__init__(self)
        self.name = kwargs.get('name')
        self.region = kwargs.get('region')
        self.site = kwargs.get('site')
        self.cluster = kwargs.get('cluster')
        self.created = time.time()
        self.modified = time.time()
        self.ip = kwargs.get('ip')
        self.ports = kwargs.get('ports')
        self.service_class = kwargs.get('service_class')
        self.provides = kwargs.get('provides')
        self.role = kwargs.get('role', MEMBER)
        self._commands = []
        self._variables_source = []
        self._variables_runtime = []
        self.lifecycle = 'starting'
        self.validate_init(app)


    def base_path(self):
        return 'services'


    def validate_init(self, app):
        BaseDescriptor.validate_init(self, app)

        # Verify all required arguments
        self.check_required(REQUIRED)
        self.check_enum('role', ROLES)

class Service(Instance):
    def __init__(self, context, **kwargs):
        Instance.__init__(self)
        self.desc = ServiceDesc(context, **kwargs)
        self.context = context 
        self.bind_property('path', lambda: None )
        self.lifecycle = Service.start
    
    
    def start(self):
        path = self.desc.path()
        data = self.desc.to_json()
        self.read_or_write(path, data)
        self.lifecycle = Service.starting


    def starting(self):
        print 'starting...'
        self.lifecycle = Service.running


    def stopping(self):
        self.lifecycle = Service.stopped

    
    def running(self):
        pass
    
    def stopped(self):
        pass

    def update(self):
        self.lifecycle(self)

