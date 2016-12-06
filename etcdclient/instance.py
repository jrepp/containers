import etcd

class Instance(object):
    def __init__(self):
        self.desc = {} # to be replaced by descriptor
        self.bindings = {}


    def bind_property(self, name, func):
        self.bindings[name] = func
    

    def __getattr__(self, name):
        return self.desc.__dict__.get(name)

    
    def update(self):
        pass

    def read_or_write(self, path, value):
        cl = self.context.etcd_client
        try:
            print 'reading path', path
            result = cl.read(path)
        except etcd.EtcdKeyNotFound:
            print 'no key, writing path', path, 'value:', value
            # result = cl.write(path, value, ttl=10)

