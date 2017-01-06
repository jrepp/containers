import time

from descriptor import BaseDescriptor
from instance import Instance

import command as _command

REQUIRED = [
        'region',
        'name',
        'args',
        'user' ]


class Descriptor(BaseDescriptor):
    def __init__(self, base_path, app, **kwargs):
        BaseDescriptor.__init__(self)

        # Commands descriptors are stored as a child under an existing base path
        # not neccessarily the app's base path
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
        self.validate_init(app)


    def base_path(self):
        return self._base_path

    
    def validate_init(self, app):
        BaseDescriptor.validate_init(self, app)
        self.check_required(REQUIRED)

class Command(Instance):
    def __init__(self):
        pass


class Runner(object):
    def __init__(self, base_path, app):
        self._base_path = base_path
        self._app = app
    

    def add(self, name, args=[], user='default'):
        cmd = _command.Descriptor(self._base_path, self._app,
                **{ 
                    'region': 'default',
                    'name': name,
                    'args': args,
                    'user': user
                })
        cl = self._app.etcd_client
        try:
            path = cmd.path()
            data = cmd.to_json()
            print 'writing command', path, ', data: ', data 
            cl.write(path, data)
        except Exception, e: 
            print 'write failed', str(e)


    def update(self):
        cl = self._app.etcd_client 
        executed = 0
        max_cmds_per_update = 5
        running = True
        while running and executed < max_cmds_per_update:
            try:
                path = '/'.join(['', self._base_path, 'default', ''])
                print 'pop path:', path
                result = cl.pop(path, recursive=True)
                
                if result and result.value and len(resulst.value) > 0:
                    doc = json.loads(result.value)
                
                    print 'loading from key:', result.key, 'value:', doc
                    cmd = CommandDesc(self._base_path, self._app, **doc)
                else:
                    print 'value empty'
            except Exception, e:
                print 'command pop failed', str(e)
                running = False


