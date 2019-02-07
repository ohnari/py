
class Test():
    pairs = []
    cnt = 0

    def __init__(self, ps):
        self.pairs = ps

    def count_one(self):
        self.cnt += 1
        return self.cnt


def main():
    a = Test([1, 2])
    print(a.count_one())
    print(a.count_one())


if __name__ == '__main__':
    main()
