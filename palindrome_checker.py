#!/usr/bin/env python3

__author__ = "Yash Tandon"
__version__ = "2026-02-19"

from atds import Deque


class PalindromeChecker:

    def __init__(self):
        self.strict_mode = False

    def set_strict_mode(self, value):
        self.strict_mode = value

    def sanitize(self, phrase):
        cleaned = ""
        for ch in phrase:
            if ch.isalpha():   #I learned this a few summers ago, I know we haven't learned it yet, but I think it's more efficient.
                cleaned += ch.lower()
        return cleaned

    def is_palindrome(self, phrase):
        if not self.strict_mode:
            phrase = self.sanitize(phrase)
        if len(phrase) == 0:
            return False
        d = Deque()
        for char in phrase:
            d.add_rear(char)
        while d.size() > 1:
            front = d.remove_front()
            rear = d.remove_rear()
            if front != rear:
                return False
        return True


def main():
    checker = PalindromeChecker()
    print("Palindrome Checker!")
    mode = input("Do you want strict mode 1) on, or 2) off? --> ")
    if mode == "1":
        checker.set_strict_mode(True)
    else:
        checker.set_strict_mode(False)
    phrase = input("Phrase: ")
    if checker.is_palindrome(phrase):
        print("Is a palindrome.")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()