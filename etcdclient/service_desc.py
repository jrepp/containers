import time
import json
from desc import Desc

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

class ServiceDesc(Desc):
    def __init__(self, context, **kwargs):
        Desc.__init__(self)
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
        self.validate_init(context)


    def validate_init(self, context):
        Desc.validate_init(self, context)

        # Verify all required arguments
        self.check_required(REQUIRED)
        self.check_enum('role', ROLES)


def test_service(context):
    return ServiceDesc(
        context,
        name='foo',
        service_class='foo',
        ip='192.168.0.2',
        ports=[4242],
        provides=['foo'])
    

