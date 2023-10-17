import random


def generate_random_array(dimension=500, min_value=1, max_value=100):
  return [random.uniform(min_value, max_value) for _ in range(dimension)]
