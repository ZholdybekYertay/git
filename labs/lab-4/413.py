import json

def resolve_query(data, query):
    current = data
    i = 0
    n = len(query)
    
    while i < n:
        if query[i] == '.':
            i += 1
            start = i
            while i < n and query[i] not in '.[ ]':
                i += 1
            key = query[start:i]
            
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return "NOT_FOUND"
                
        elif query[i] == '[':
            i += 1
            start = i
            while i < n and query[i] != ']':
                i += 1
            idx_str = query[start:i]
            i += 1
            
            try:
                idx = int(idx_str)
                if isinstance(current, list) and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return "NOT_FOUND"
            except ValueError:
                return "NOT_FOUND"
                
        else:
            start = i
            while i < n and query[i] not in '.[ ]':
                i += 1
            key = query[start:i]
            
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return "NOT_FOUND"

    return json.dumps(current, sort_keys=True, separators=(',', ':'))

def solve():
    line1 = input().strip()
    if not line1: return
    data = json.loads(line1)
    line2 = input().strip()
    if not line2: return
    num_queries = int(line2)

    for _ in range(num_queries):
        query = input().strip()
        print(resolve_query(data, query))

if __name__ == "__main__":
    solve()