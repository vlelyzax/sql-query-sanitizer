import re
FORBIDDEN = [r'--.*', r'/\*.*?\*/', r';', r'\bDROP\b', r'\bUNION\b']
def is_suspicious(query: str) -> bool:
    return any(re.search(pat, query, re.I) for pat in FORBIDDEN)
