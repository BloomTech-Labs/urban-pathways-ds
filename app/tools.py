import mmap


def remove_multiple_periods(text):
    if isinstance(text, int):
        return float(text)
    if isinstance(text, float):
        return text
    while ".." in text:
        text = text.replace("..", ".")
    text = text.replace("$", "")
    return float(text)


def make_names_uniform(name: str) -> str:
    if "," in name:
        return " ".join(reversed(name.split(",")))
    else:
        return name


def mmap_io(file):
    with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
        return mmap_obj.read()
