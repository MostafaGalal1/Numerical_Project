from methods.abstract_method import *
from methods.doolittle import *


class Chelosky(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        Doolittle(self.n, self.a, self.b, self.service).execute()
        l = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        u = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        d = [[0.0 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    l[i][j] = 1.0
                    u[i][j] = 1.0
                    d[i][j] = self.a[i][j]
                elif i < j:
                    u[i][j] = self.a[i][j]
                elif i > j:
                    l[i][j] = self.a[i][j]

        ans = "L = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in l[it])) for it in range(self.n)) + "\n\nD = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in d[it])) for it in range(self.n)) + "\n\nU = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in u[it])) for it in range(self.n))
        return ans
