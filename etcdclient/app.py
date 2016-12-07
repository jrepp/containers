import logging as _logging
import start as _start

TYPES = {
            'service': ServiceDesc,
            'cluster': ClusterDesc,
            'command': CommandDesc
        }

class App(object):
    def __init__(self, name, etcd_client=None):
        # Use the default client
        if etcd_client is None:
            self.etcd_client = _start.setup_client()

        self.etcd_client = etcd_client

        # A base with blank name expands as /
        # A base with any key will expand as /key
        self.base_path = '' 

        # Setup the default logger
        self.log  = _logging.getLogger(name)
    

    def __enter__(self):
        return self


    def __exit__(self, type, value, traceback):
        pass


    def from_json(self, json_text):
        doc = json.loads(json_text)

        constructor = TYPES.get(doc.get('type'))
        if constructor is None:
            raise ValueError('The "type" attribute was not in the template: "{0}'.format(json_text))

        desc = constructor(self, **doc)
        if desc is None:
            raise ValueError('The constructor "{0}" failed'.format(constructor))

        return desc


