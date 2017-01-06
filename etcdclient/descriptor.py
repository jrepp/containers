import uuid
import json
import inspect

GLOBAL = 'global'
REGIONAL = 'regional'
SITE = 'site'

SCOPES = [GLOBAL, REGIONAL, SITE]

class BaseDescriptor(object):
    def __init__(self):
        """
        Create a new descriptor, not valid till path and uuid calculated
        """
        self._path = None
        self._uuid = None
    

    def __getitem__(self, key):
        return self.__dict__[key]


    def path(self):
        return self._path


    def uuid(self):
        return self._uuid


    def validate_init(self, app):
        """
        Base descriptor validation
        """
        self.build_uuid()
        self.build_path(app)
        self.check_enum('scope', SCOPES)


    def check_required(self, required):
        """
        Check a required list of arguments
        """
        for k in required:
            if self.__dict__.get(k) is None:
                raise ValueError(
                        "Required argument: '{0}' not provided".format(k))


    def check_enum(self, name, values):
        """
        Verify a key value in a set of values, raises ValueError
        """
        v = self.__dict__.get(name)
        if v not in values:
            raise ValueError(
                "Invalid value: {0}='{1}', not in '{2}'".format(name, v, values))


    def to_json(self):
        """
        Emit contents as JSON
        """
        doc = {}
        for k, v in self.__dict__.iteritems():
            if not inspect.isfunction(v) and not k.startswith('_'):
                doc[k] = v
        return json.dumps(doc)

    
    def from_json(self, json_str):
        doc = json.loads(json_str)
        for k, v in doc.iteritems():
            self.__setattr__(k, v)


    def build_uuid(self):
        """
        Generate the service UUID
        """
        self._uuid = str(uuid.uuid1())
        return self._uuid

    def build_container_path_parts(self, app):
        """
        Generate the containing path of the descriptor"
        """
        parts = []
        parts.append(app.base_path)
        parts.append(self.base_path())

        if self.region and self.site:
            parts.append(self.region)
            parts.append(self.site)
            self.scope = SITE
        elif self.region:
            parts.append(self.region)
            self.scope = REGIONAL
        else:
            parts.append(GLOBAL)
            self.scope = GLOBAL
        return parts


    def build_path(self, app):
        """
        Generate the specific descriptor path
        """
        if not self._uuid:
            raise ValueError("Descriptor UUID not initialized")

        parts = self.build_container_path_parts(app) 
        parts.append(self._uuid)
        self._path = '/'.join(map(str, parts))
        return self._path


