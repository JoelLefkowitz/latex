import os


def output_segments(path: str, ext: str) -> tuple[str, str]:
    """
    >>> output_segments('', '.pdf')
    ('.', '.pdf')

    >>> output_segments('a', '.pdf')
    ('.', 'a.pdf')

    >>> output_segments('a.py', '.pdf')
    ('.', 'a.pdf')

    >>> output_segments('a/b.py', '.pdf')
    ('a', 'b.pdf')
    """
    tail, head = os.path.split(path)
    filename, _ = os.path.splitext(head)
    return "." if tail == "" else tail, filename + ext
