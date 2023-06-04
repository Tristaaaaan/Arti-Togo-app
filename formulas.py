import math
from datastore import DataStore

datas = DataStore()


class Formula:
    def __init__(self):
        pass

    def calculate_coordinate(self, option, Xa, Ya, Ha, aab, Dab, e):

        if option == 'True':
            A = Dab * math.cos((aab * math.pi) / 180)
            if Xa < 10000:
                result1 = Xa + 100000 + A
                Xb = format(result1, ".0f")
            else:
                result1 = Xa + A
                Xb = format(result1, ".0f")

            B = Dab * math.sin((aab * math.pi) / 180)
            if Ya < 10000:
                result2 = Ya + 100000 + B
                Yb = format(result2, ".0f")
            else:
                result2 = Ya + B
                Yb = format(result2, ".0f")
            result3 = Ha + Dab * math.tan((e * math.pi) / 180)
            Hb = format(result3, ".0f")

            return Xb, Yb, Hb

        else:
            A = Dab * math.cos((aab * math.pi) / 3000)
            if Xa < 10000:
                result1 = Xa + 100000 + A
                Xb = format(result1, ".0f")
            else:
                result1 = Xa + A
                Xb = format(result1, ".0f")

            B = Dab * math.sin((aab * math.pi) / 3000)
            if Ya < 10000:
                result2 = Ya + 100000 + B
                Yb = format(result2, ".0f")
            else:
                result2 = Ya + B
                Yb = format(result2, ".0f")
            result3 = Ha + Dab * math.tan((e * math.pi) / 3000)
            Hb = format(result3, ".0f")

            return Xb, Yb, Hb

    def calculate_distance(self, option, Dab, A, B):
        if option == 'True':
            C = 360 - int(A + B)
            Dac = (math.sin((B * math.pi) / 180) * Dab) / (
                math.sin((C * math.pi / 180)))
            Dac = format(Dac, ".0f")
            Dbc = math.sin((A * math.pi) / 180) * Dab / (
                math.sin((C * math.pi / 180)))
            Dbc = format(Dbc, ".0f")
        else:
            C = 3000 - int(A + B)
            Dac = (math.sin((B * math.pi) / 3000) * Dab) / (
                math.sin((C * math.pi / 3000)))
            Dac = format(Dac, ".0f")
            Dbc = math.sin((A * math.pi) / 3000) * Dab / (
                math.sin((C * math.pi / 3000)))
            Dbc = format(Dbc, ".0f")
        return Dac, Dbc, C

    def calculate_change1(self, pD, pF, pG):

        BCrk = round((-1) * pD / 2)
        Frk = round((-1) * pF * pG)

        return BCrk, Frk

    def calculate_change2(self, pD, pF, pG, BRck, Frk):

        BCx1 = round((-1) * pD / ((-1) * pG))
        Fx1 = round((-1) * pF + 0.01 * (-1) * pD)
        BCrc1 = BRck + BCx1
        Frc1 = Frk + Fx1

        return BCx1, Fx1, BCrc1, Frc1
