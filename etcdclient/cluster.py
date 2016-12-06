from instance import Instance
from service_desc import ServiceDesc
from cluster_desc import ClusterDesc
from state_machine import StateMachine

class Cluster(Instance):
    def __init__(self, context, **kwargs):
        Instance.__init__(self)
        self.desc = ClusterDesc(context, **kwargs)
        self.context = context
        self.bind_property('path', lambda: None)
