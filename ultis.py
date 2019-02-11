def load_file(path_file):
    lines = list(open(path_file, 'r', encoding='utf8', errors='ignore').readlines())
    lines = [l.strip() for l in lines]
    return lines
