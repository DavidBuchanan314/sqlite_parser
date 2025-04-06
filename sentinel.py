"""
me: make me a python class that compares less than any other object, and another that compares greater than any other object. I want to use them as sentinel values.

deepseek:
"""


class MinSentinel:
	"""An object that compares less than any other object (except other MinSentinels)"""

	def __lt__(self, other):
		return not isinstance(other, MinSentinel)

	def __gt__(self, other):
		return False

	def __le__(self, other):
		return True

	def __ge__(self, other):
		return isinstance(other, MinSentinel)

	def __eq__(self, other):
		return isinstance(other, MinSentinel)

	def __repr__(self):
		return "MIN_SENTINEL"


class MaxSentinel:
	"""An object that compares greater than any other object (except other MaxSentinels)"""

	def __lt__(self, other):
		return False

	def __gt__(self, other):
		return not isinstance(other, MaxSentinel)

	def __le__(self, other):
		return isinstance(other, MaxSentinel)

	def __ge__(self, other):
		return True

	def __eq__(self, other):
		return isinstance(other, MaxSentinel)

	def __repr__(self):
		return "MAX_SENTINEL"


# Singleton instances for convenience
MIN_SENTINEL = MinSentinel()
MAX_SENTINEL = MaxSentinel()
