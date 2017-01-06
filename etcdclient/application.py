import os
import etcd
import json

import logging as _logging
import service as _service
import cluster as _cluster
import command as _command
import discovery as _discovery

TYPES = {
            'service': _service.Descriptor,
            'cluster': _cluster.Descriptor,
            'command': _command.Descriptor
        }


def default_client():
    addr = os.getenv('ETCD_ADDR')
    port = int(os.getenv('ETCD_PORT', 0))
    if not addr or not port:
        return None

    client = etcd.Client(
            host=addr,
            port=port,
            allow_reconnect=True,
            allow_redirect=True)
    return client


def default(name="default"):
    return Application(name, default_client())


class Application(object):
    def __init__(self, name, etcd_client=None, **kwargs):
        # Use the default etcd client if one is not specified
        if etcd_client is None:
            self.etcd_client = setup_client()

        self.etcd_client = etcd_client
        
        # Initiaize discovery
        self.discovery = _discovery.Discovery(self)

        # Store off all the application properties
        self.properties = kwargs

        # A base with blank name expands as /
        # A base with any key will expand as /key
        self.base_path = ''

        # Setup the default logger
        self.log  = _logging.getLogger(name)

        # Local services
        self.services = []
    

    def __enter__(self):
        return self


    def __exit__(self, type, value, traceback):
        pass


    def from_json(self, json_text):
        """
        Convert a piece of JSON content into an object instance
        """
        doc = json.loads(json_text)

        constructor = TYPES.get(doc.get('type'))
        if constructor is None:
            raise ValueError('The "type" attribute was not in the template: "{0}'.format(json_text))

        desc = constructor(self, **doc)
        if desc is None:
            raise ValueError('The constructor "{0}" failed'.format(constructor))

        return desc


    def register(self, service):
        if len(service.name) == 0:
            raise ValueError("Application.register: service must specify a valid name")

        existing = self.services.get(service.name)
        if existing:
            self.log.info("replacing service: {0}".format(service.name))
        self.services[service.name] = service


