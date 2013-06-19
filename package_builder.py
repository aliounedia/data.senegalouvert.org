#! /usr/bin/env python

"""
Take The  --ansd_package_entity_get_tojson.json -- file and
And informations needed by senegalouvert.org, because The site
is a clone of http://data.okfn.org/ and We should respect the
packages (json file) needed. For exemple add (description) item
to each  element of dict,  readme , ect .
For This moment I am adding only the description to each
element/dataset.
"""

import json
def build(json_file):
    list = json.load(open(json_file))
    list1 = []
    for dict in list:
        print dict , type(dict)
        if dict.has_key("notes") and \
            dict["notes"].strip() != "" :
              dict["description"] = dict["notes"]
              list1.append(dict)
    json.dump(list1, open(
                'ansd_data_packages_index.json', 'wb'),
                indent=4, sort_keys=True)
    
if __name__ =="__main__" :
    build("ansd_package_entity_get_tojson.json")
