from collections import Counter

## Type names for simpler comparison later
dictType=type(dict())
listType=type(list())
unicodeType=type(u'')
noneType=type(None)

class json_stats_tracker:

    def __init__(self, raw_json):
        self.raw_json = raw_json

    def parse_json(self, json_node, parent_path=""):

        this_node_type = type(json_node)

        if this_node_type == unicodeType:
            this_key = parent_path
            this_value = json_node
            self.keys_found.update([this_key,])

        elif this_node_type == listType:
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
        self.parse_json(self.raw_json)
        return self.keys_found