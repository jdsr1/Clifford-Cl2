#!/usr/bin/python

class Clifford2(object):
    def __init__(self, u0, u1, u2, u12):
        self.u0 = u0
        self.u1 = u1
        self.u2 = u2
        self.u12 = u12

    def __str__(self):
        eps = 1.0e-6
        if abs(self.u0) < eps:
            su0 = "0"
        else:
            su0 = f"{self.u0}"

        if abs(self.u1) < eps:
            su1 = "0"
        elif self.u1 < 0:
            if abs(1-abs(self.u1)) < eps:
                su1 = "-e1"
            else:
                su1 = f"{self.u1}e1"
        else:
            if abs(1-abs(self.u1)) < eps:
                su1 = "e1"
            else:
                su1 = f"{self.u1}e1"

        if abs(self.u2) < eps:
            su2 = "0"
        elif self.u2 < 0:
            if abs(1-abs(self.u2)) < eps:
                su2 = "-e2"
            else:
                su2 = f"{self.u2}e2"
        else:
            if abs(1-abs(self.u2)) < eps:
                su2 = "e2"
            else:
                su2 = f"{self.u2}e2"

        if abs(self.u12) < eps:
            su12 = "0"
        elif self.u12 < 0:
            if abs(1-abs(self.u12)) < eps:
                su12 = "-e12"
            else:
                su12 = f"{self.u12}e12"
        else:
            if abs(1-abs(self.u12)) < eps:
                su12 = "e12"
            else:
                su12 = f"{self.u12}e12"

        sui = [su0, su1, su2, su12]
        su = f"({su0}, {su1}, {su2}, {su12})"
        return su

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        ru0 = self.u0 + other.u0
        ru1 = self.u1 + other.u1
        ru2 = self.u2 + other.u2
        ru12 = self.u12 + other.u12

        return Clifford2(ru0, ru1, ru2, ru12)

    def __sub__(self, other):
        ru0 = self.u0 - other.u0
        ru1 = self.u1 - other.u1
        ru2 = self.u2 - other.u2
        ru12 = self.u12 - other.u12

        return Clifford2(ru0, ru1, ru2, ru12)

    def __mul__(self, other):
        ru0 = self.u0*other.u0 + self.u1*other.u1 + self.u2*other.u2 \
            - self.u12*other.u12
        ru1 = self.u0*other.u1 + self.u1*other.u0 - self.u2*other.u12 \
            + self.u12*other.u2
        ru2 = self.u0*other.u2 + self.u1*other.u12 + self.u2*other.u0 \
            - self.u12*other.u1
        ru12 = self.u0*other.u12 + self.u1*other.u2 - self.u2*other.u1 \
             + self.u12*other.u0

        return Clifford2(ru0, ru1, ru2, ru12)

    def conj(self):
        return Clifford2(self.u0, -self.u1, -self.u2, -self.u12)

    def reverse(self):
        return Clifford2(self.u0, self.u1, self.u2, -self.u12)

    def grade_involute(self):
        return Clifford2(self.u0, -self.u1, -self.u2, self.u12)

    @property
    def norm2(self):
        uu = self*self.conj()
        r = uu.u0 + uu.u1 + uu.u2 + uu.u12
        return r

    def inverse(self):
        uu = self.norm2
        ucon = self.conj()
        ru0 = ucon.u0/uu
        ru1 = ucon.u1/uu
        ru2 = ucon.u2/uu
        ru12 = ucon.u12/uu

        return Clifford2(ru0, ru1, ru2, ru12)

def dot(self,other):
    ru0  = self.u0*other.u0 + self.u1*other.u1 + self.u2*other.u2 \
           - self.u12*other.u12
    ru1  = self.u0*other.u1 + self.u1*other.u0
    ru2  = self.u0*other.u2 + self.u2*other.u0
    ru12 = self.u0*other.u12 + self.u12*other.u0

    return Clifford2(ru0, ru1, ru2, ru12)

def wedge(self,other):
    ru0  = 0
    ru1  = self.u12*other.u2 - self.u2*other.u12
    ru2  = self.u1*other.u12 - self.u12*other.u1
    ru12 = self.u1*other.u2  - self.u2*other.u1

    return Clifford2(ru0, ru1, ru2, ru12)
