
if __name__ == '__main__':

    class TriangleClassifier:
        def __init__(self, x, y, z):
            self.angle1 = x
            self.angle2 = y
            self.angle3 = z

    class Triangle(TriangleClassifier):
        def __init__(self, x, y, z):
            super().__init__(x, y, z)

        def checkt(self):
            if self.angle1 + self.angle2 + self.angle3 == 180 and self.angle1 > 0 and self.angle2 > 0 and self.angle3 > 0:
                return True

    class Equilateral(Triangle):
        def __init__(self, x, y, z):
            super().__init__(x, y, z)

        def checke(self):
            if super().checkt():
                if self.angle1 == self.angle2 == self.angle3:
                    return True

    class Isosceles(Triangle):
        def __init__(self, x, y, z):
            super().__init__(x, y, z)

        def checki(self):
            if super().checkt():
                if self.angle1 == self.angle2 or self.angle1 == self.angle2 or self.angle2 == self.angle3:
                    return True

    class Scalene(Triangle):
        def __init__(self, x, y, z):
            super().__init__(x, y, z)

        def checks(self):
            if super().checkt():
                return True

    my_angles = []
    with open('input.csv', 'r') as f:
        for line in f.readlines():
            angles = line[:-1].split(',')
            my_angles.append(angles)

    dict = {'Equilateral': 0, 'Isosceles': 0, 'Scalene' : 0, 'None': 0}

    for i in my_angles:
        t = Triangle(float(i[0]),float(i[1]),float(i[2]))
        E = Equilateral(float(i[0]), float(i[1]), float(i[2]))
        I = Isosceles(float(i[0]), float(i[1]), float(i[2]))
        S = Scalene(float(i[0]), float(i[1]), float(i[2]))
        if t.checkt() != True:
            dict['None'] += 1
        elif E.checke():
            dict['Equilateral'] +=1
        elif I.checki():
            dict['Isosceles'] +=1
        elif S.checks():
            dict['Scalene'] += 1

    print(dict)





