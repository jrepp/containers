
class Discovery(object):
    def __init__(self, app):
        self.app = app


    def build_container_path(self, descriptor):
        container_parts = descriptor.build_container_path_parts(self.app)
        path = '/'.join(map(str, container_parts))
        return path


    def find_by_type(self, match_descriptor):
        search_path = self.build_container_path(match_descriptor, self.app)
        self.app.log.debug('searching', search_path)

        cl = self.app.etcd_client
        results = cl.read(search_path, recursive=True)
        if type(results) is type([]):
            return results
        else:
            return [results]


    def find_by_name(self, scope, name):
        pass


