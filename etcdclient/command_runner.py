import json

from command_desc import CommandDesc

class CommandRunner(object):
    def __init__(self, base_path, context):
        self._base_path = base_path
        self._context = context
    

    def add(self, name, args=[], user='default'):
        cmd = CommandDesc(self._base_path, self._context,
                **{ 
                    'region': 'default',
                    'name': name,
                    'args': args,
                    'user': user
                })
        cl = self._context.etcd_client
        try:
            path = cmd.path()
            data = cmd.to_json()
            print 'writing command', path, ', data: ', data 
            cl.write(path, data)
        except Exception, e: 
            print 'write failed', str(e)


    def update(self):
        cl = self._context.etcd_client 
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
                    cmd = CommandDesc(self._base_path, self._context, **doc)
                else:
                    print 'value empty'
            except Exception, e:
                print 'command pop failed', str(e)
                running = False


