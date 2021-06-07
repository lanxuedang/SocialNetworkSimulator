class Indexs:
    def GAI(self, p, X, D):
        awareness = 0.0
        for key in X.keys():
            awareness += X[key] * D[key]
        return awareness / p


class City:
    def __init__(self, popluation, tweets, OD):
        self.p = popluation
        self.dictTweets = tweets
        self.dictOD = OD

    def GAI(self):
        g = Indexs()
        return g.GAI(self.p, self.dictTweets, self.dictOD)


if __name__ == "__main__":
    cites = []  # input data here
    globalAwareness = []
    for i in range(len(cites)):
        globalAwareness.append(cites[i].GAI())
