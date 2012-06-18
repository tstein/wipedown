#!/usr/bin/env python
""" Generate a password designed to defend against smudge attacks. The goal is
that it will be as difficult as possible to identify the password from the
smudge left by entering it with a swiping keyboard (i.e., one where the user
moves his finger from letter to letter, rather than tapping each letter
individually). """

from argparse import ArgumentParser

from .genpass import genpass


_DESCRIPTION = 'Generate a password designed to defend against smudge attacks.'
_ARGHELP = dict()
_ARGHELP['-s'] = 'number of swerves allowed in the generated password [unlimited]'
_ARGHELP['-v'] = 'print info about what makes this password strong'


def main():
  parser = _makeparser()
  args = parser.parse_args()
  genpass_kwargs = dict()
  if args.s is not None:
    genpass_kwargs['maxswerves'] = args.s[-1]
  password = genpass(**genpass_kwargs)
  print(password.word)
  if args.v:
    _printstats(password)


def _makeparser():
  """ Initialize an argument parser. """
  parser = ArgumentParser(description=_DESCRIPTION)
  parser.add_argument('-s', metavar='swerves', action='store', nargs=1,
                      type=int, help=_ARGHELP['-s'])
  parser.add_argument('-v', action='store_true', help=_ARGHELP['-v'])
  return parser


def _printstats(password):
  print("score: %5.2f\tswerves: %3d" % (password.score, password.swerves))


if __name__ == '__main__':
  main()

