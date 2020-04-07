# Functiona containing both args and kwargs

def cheesehop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all of", kind
    for arg in arguments():
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
