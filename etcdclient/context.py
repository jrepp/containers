
class Context(object):
    def __init__(self, etcd_client):
        self.etcd_client = etcd_client
        self.base_path = '' # will just expand as /, any key will expand as /key/
