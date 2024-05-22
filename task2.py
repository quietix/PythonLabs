import numpy as np
from random import randint, choices
from pprint import pprint


def mean_by_region(votes, regions):
    votes = np.array(votes)
    regions = np.array(regions)
    uniq_regions = np.unique(regions)
    region_mean_votes = {}

    for region in uniq_regions:
        region_votes = votes[regions == region]
        region_mean_votes[region] = np.round(np.mean(region_votes), 2)

    return region_mean_votes


if __name__ == "__main__":
    region_names = ["Київ", "Вінниця", "Львів", "Харків", "Дніпро", "Хмельницький"]
    k = 15

    votes = [randint(50, 1500) for i in range(k)]
    regions = choices(region_names, k=k)

    print("votes:", votes)
    print("regions:", regions, end="\n\n")

    res = mean_by_region(votes, regions)
    pprint(sorted(res.items(), key=lambda p: p[1], reverse=True))
