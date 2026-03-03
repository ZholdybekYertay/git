import json

def get_diff(obj1, obj2, path, differences):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        all_keys = sorted(set(obj1.keys()) | set(obj2.keys()))
        for key in all_keys:
            new_path = f"{path}.{key}" if path else key
            
            if key not in obj1:
                val2 = json.dumps(obj2[key], sort_keys=True, separators=(',', ':'))
                differences.append(f"{new_path} : <missing> -> {val2}")
            elif key not in obj2:
                val1 = json.dumps(obj1[key], sort_keys=True, separators=(',', ':'))
                differences.append(f"{new_path} : {val1} -> <missing>")
            else:
                get_diff(obj1[key], obj2[key], new_path, differences)
    elif obj1 != obj2:
        val1 = json.dumps(obj1, sort_keys=True, separators=(',', ':'))
        val2 = json.dumps(obj2, sort_keys=True, separators=(',', ':'))
        differences.append(f"{path} : {val1} -> {val2}")

def solve():
    line1 = input().strip()
    line2 = input().strip()
    
    obj1 = json.loads(line1)
    obj2 = json.loads(line2)
    
    differences = []
    get_diff(obj1, obj2, "", differences)
    
    if not differences:
        print("No differences")
    else:
        differences.sort()
        for diff in differences:
            print(diff)

if __name__ == "__main__":
    solve()