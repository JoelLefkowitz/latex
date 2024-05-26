def reference(title: str, author: str, publisher: str) -> str:
    """
    >>> reference('Title', 'Author', 'Publisher')
    '\\\\bibitem{title} Author, {\\\\it Title}, Publisher.'
    """
    key = title.lower().replace(" ", "-")
    return f"\\bibitem{{{key}}} {author}, {{\\it {title}}}, {publisher}."
