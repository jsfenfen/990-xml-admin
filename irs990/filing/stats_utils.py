from collections import Counter
from filing.type_utils import dictType, listType, unicodeType, noneType

class json_stats_tracker:

    def __init__(self, raw_json):
        self.raw_json = raw_json

    def parse_json(self, json_node, parent_path=""):

        this_node_type = type(json_node)

        if this_node_type == unicodeType:
            self.keys_found.update([parent_path,])

        elif this_node_type == listType:

            self.list_roots_found.update([parent_path,])
            for child_node in json_node:
                self.parse_json(child_node, parent_path=parent_path)

        elif this_node_type == dictType:
            keys = json_node.keys()
            for key in keys:
                new_path = parent_path + "/" + key
                self.parse_json(json_node[key], parent_path=new_path)

        elif this_node_type == noneType:
            pass

        else:
            raise Exception ("Unhandled type: %s" % (type(json_node)))

    def parse(self):
        self.keys_found = Counter()
        self.list_roots_found = Counter()
        self.parse_json(self.raw_json)
        return (self.keys_found, self.list_roots_found)