""" Generate smudge-attack-resistant passwords. """

from math import sqrt
from operator import itemgetter
from random import shuffle

from .keyboard import swype


def _evaluate(kboard, word):
  """ Evaluate the strength of an individual word. The return value is a
  relative score that is not meaningful other than in comparison to the results
  of other calls to this function. """
  def distance(start, finish):
    delta_x = finish[0] - start[0]
    delta_y = finish[1] - start[1]
    return sqrt((delta_x * delta_x) + (delta_y * delta_y))
  # Sum up the straight-line distance from each letter to the next.
  score = 0
  for fst, snd in zip(word[:-1], word[1:]):
    score += distance(kboard[fst], kboard[snd])
  return score


def genpass():
  """ Generate a password. """
  kb = swype
  # TODO: Use a tmpfile to speed this up.
  scores = dict()
  with open("words.txt", 'r') as wordfile:
    for line in wordfile:
      word = line.strip().strip('%').lower()
      scores[word] = _evaluate(kb, word)
  ranked = scores.items()
  ranked.sort(key=itemgetter(1)) 
  ranked.reverse()
  candidates = ranked[:(len(ranked) / 10)]
  shuffle(candidates)
  return candidates[0][0]

