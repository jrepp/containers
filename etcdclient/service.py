from instance import Instance
from service_desc import ServiceDesc
from state_machine import StateMachine

class Service(Instance):
    def __init__(self, context, **kwargs):
        Instance.__init__(self)
        self.desc = ServiceDesc(context, **kwargs)
        self.context = context 
        self.bind_property('path', lambda: None )
        self.lifecycle = Service.start
    
    
    def start(self):
        path = self.desc.path()
        data = self.desc.reflect()
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

