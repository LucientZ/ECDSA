"""
Module which contains any functionality that doesn't fit into any of the libraries
"""


def read_file(path: str):
    """
    Snippet that returns file as string
    """
    with open(path, "r") as f:
        return f.read()
