#!/usr/bin/env python

"""Retrieve and print words from a URL.

Usage:
    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: the URL of a UFT-8 text document.

    Returns:
        A list of string strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document at a URL.

    Args:
        url: the URL of a UTF-8 text document
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    # 'http://sixty-north.com/c/t.txt'
    url = sys.argv[1]
    main(url)
