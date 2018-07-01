""" Война двух армий. Ранодомно выбирается кто кому нанесет первый удар  Удаляется каждый мертвый воин из массива

"""

import random


class Voiny:

    def __init__(self, gizni, udar):

        self.gizni = gizni

        self.udar = udar

class Chislin:

    def __init__(self):

        self.b = []

    def postroenie(self, count):

        for i in range(count):

            voin = Voiny(100, 25)

            self.b.append(voin)

    """Достается воин из массива"""

    def get_next(self):

        voin = self.b[0]

        return voin

    """Удаляется каждый мертвый воин из массива"""

    def deleteVoin(self, voin):

        self.b.remove(voin)


otrjd1 = Chislin()

otrjd1.postroenie(12)

otrjd2 = Chislin()

otrjd2.postroenie(12)



voin1 = None

voin2 = None


while len(otrjd1.b) > 0 and len(otrjd2.b) > 0:


    if voin1 == None:

        voin1 = otrjd1.get_next()


    if voin2 == None:

        voin2 = otrjd2.get_next()


    ochered = random.randint(1, 2)

    """Ранодомно выбирается кто кому нанесет первый удар"""

    while voin1 != None and voin2 != None:

        if ochered == 1:

            voin2.gizni = voin2.gizni - voin1.udar * random.randint(0, 1)

            if voin2.gizni <= 0:

                otrjd2.deleteVoin(voin2)

                voin2 = None

            ochered = 2

        else:

            voin1.gizni = voin1.gizni - voin2.udar * random.randint(0, 1)

            if voin1.gizni <= 0:

                otrjd1.deleteVoin(voin1)

                voin1 = None

            ochered = 1


print(len(otrjd1.b))

print(len(otrjd2.b))
