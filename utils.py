def extract_code(content, tag):
    try:
        start = content.index(f"---{tag}---") + len(f"---{tag}---")
        end = content.index(f"---{tag}---", start)
        return content[start:end].strip()
    except ValueError:
        return ""