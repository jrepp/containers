import desc

def build_container_path(desc, context):
    container_parts = desc.build_container_path_parts(context)
    path = '/'.join(map(str, container_parts))
    return path

def find_by_type(match_desc, context):
    search_path = build_container_path(match_desc, context)
    cl = context.etcd_client
    print 'searching', search_path
    results = cl.read(search_path, recursive=True)
    if type(results) is type([]):
        return results
    else:
        return [results]

def find_by_name(scope, name):
    pass


