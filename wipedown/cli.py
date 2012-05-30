#!/usr/bin/env python
""" Generate a password designed to defend against smudge attacks. The goal is
that it will be as difficult as possible to identify the password from the
smudge left by entering it with a swiping keyboard (i.e., one where the user
moves his finger from letter to letter, rather than tapping each letter
individually). """

from .genpass import genpass


def main():
  password = genpass()
  print(password)


if __name__ == '__main__':
  main()

