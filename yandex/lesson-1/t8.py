# lessons
from importlib.machinery import FrozenImporter


def flats_per_stage(k, n):
    perStage = 1
    while True:
        if (k - 1) / perStage == n:
            break
        perStage = perStage + 1
    return perStage


print(flats_per_stage(2, 1))
