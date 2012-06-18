""" Generate smudge-attack-resistant passwords. """

from math import sqrt
from random import choice

from .keyboard import swype


class Candidate(object):
  """ Represents a password under consideration. Gathers all interesting
  properties into a single data structure. """
  def __init__(self, word):
    self.word = word
    # Scores are relative values that are not meaningful other than in
    # comparison to results of the same code on other words.
    self.score = 0
    # A swerve is a reversal in horizontal travel.
    self.swerves = 0

  def __repr__(self):
    return "%s {score: %.2f, swerves: %d}" % (self.word, self.score,
                                              self.swerves)


def _evaluate(kboard, word):
  """ Evaluate the strength of an individual word. Returns a Candidate
  structure. """
  def distance(start, finish):
    delta_x = finish[0] - start[0]
    delta_y = finish[1] - start[1]
    return sqrt((delta_x * delta_x) + (delta_y * delta_y))

  def direction(start, finish):
    """ Returns a 2-tuple indicating whether a swipe from start to finish is
    moving right and whether it is moving up. A value of None indicates no
    movement in that axis. """
    if finish[0] - start[0] > 0:
      moving_right = True
    elif finish[0] - start[0] < 0:
      moving_right = False
    else:   # No horizontal movement.
      moving_right = None
    if finish[1] - start[1] > 0:
      moving_up = True
    elif finish[1] - start[1] < 0:
      moving_up = False
    else:   # No vertical movement.
      moving_up = None
    return (moving_right, moving_up)

  # To calculate a score, sum up the straight-line distance from each letter to
  # the next.
  cand = Candidate(word)
  # None indicates that we start at rest
  moving_right = None
  for fst, snd in zip(word[:-1], word[1:]):
    cand.score += distance(kboard[fst], kboard[snd])
    moved_right, _ = direction(kboard[fst], kboard[snd])
    # If we moved horizontally between this pair of letters...
    if moved_right is not None:
      # If we were already moving horizontally and the direction has
      # reversed...
      if moving_right is not None and moved_right != moving_right:
        cand.swerves += 1
      # Either way, update the direction we are moving.
      moving_right = moved_right
  return cand


def genpass(**kwargs):
  """ Generate a password. """
  maxswerves = 0
  if 'maxswerves' in kwargs:
    maxswerves = kwargs['maxswerves']
  kb = swype
  # TODO: Use a tmpfile to speed this up.
  scores = list()
  with open("words.txt", 'r') as wordfile:
    for line in wordfile:
      word = line.strip().strip('%').lower()
      scores.append(_evaluate(kb, word))
  # Filter out all words with too many swerves.
  if maxswerves:
    scores = [s for s in scores if s.swerves <= maxswerves]

  def getscore(candidate):
    return candidate.score
  scores.sort(key=getscore)
  scores.reverse()
  candidates = scores[:(len(scores) / 10)]
  return choice(candidates)

