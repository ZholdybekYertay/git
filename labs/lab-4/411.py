import json

def json_merge_patch(source, patch):
    if not isinstance(patch, dict):
        return patch
    if not isinstance(source, dict):
        source = {}

    for key, value in patch.items():
        if value is None:
            if key in source:
                source.pop(key)
        else:
            source[key] = json_merge_patch(source.get(key), value)
            
    return source

line1 = input().strip()
line2 = input().strip()

source_obj = json.loads(line1)
patch_obj = json.loads(line2)

result = json_merge_patch(source_obj, patch_obj)

print(json.dumps(result, sort_keys=True, separators=(',', ':')))