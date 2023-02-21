import json


def tafigy_json_splitter(tag_json_string):
    # TAGGIT_TAGS_FROM_STRING = 'appname.utils.comma_splitter'
    tags = []
    j = json.loads(tag_json_string)
    for item in j:
        tags.append(item['value'])
    # return [t.strip().lower() for t in tag_string.split(',') if t.strip()]

    print(f"SPLITTER got '{tag_json_string}' - returning {repr(tags)}")
    return tags


def tagify_json_joiner(tags):
    tag_values = []
    for t in tags:
        tag_values.append({"value": str(t)})
    ret = json.dumps(tag_values)
    print(f"JOINER got {repr(tags)} - returning '{ret}'")
    return ret
