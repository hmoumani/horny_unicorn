class TinyStatistician:
    
    @staticmethod
    def mean(x: list):
        if not x:
            return None
        _sum = 0
        for i in x:
            _sum += i
        return float(_sum / len(x))
    
    @staticmethod
    def median(x: list):
        if not x:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return float((x[len(x) // 2] + x[len(x) // 2 - 1]) / 2)
        else:
            return float(x[len(x) // 2])
        
    @staticmethod
    def quartiles(x: list):
        if not x:
            return None
        x.sort()
        return [float(x[len(x) // 4]), float(x[int(len(x) * 0.75)])]
    
    @staticmethod
    def var(x: list):
        if not x:
            return None
        _mean = TinyStatistician.mean(x)
        _sum = 0
        for i in x:
            _sum += (i - _mean) ** 2
        return float(_sum / len(x))

    @staticmethod
    def std(x: list):
        if not x:
            return None
        return float(TinyStatistician.var(x) ** 0.5)


if __name__ == '__main__':
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.quartiles(a))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862