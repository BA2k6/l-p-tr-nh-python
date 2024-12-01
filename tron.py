from math import *
class Hinh:
    def __init__(self, c, h):
        self.c = c
        self.h = h

class tron(Hinh):
    def dt(self):
            return self.c ** 2 * 3.14
    def cv(self):
        return 2 * self.c * 3.14
class vuong(Hinh):
    def dt(self):
        return self.c ** 2
    def cv(self):
        return 4 * self.c
class tamgiacdeu(Hinh):
    def dt(self):
        return (sqrt(3)/4)*self.c**2
    def cv(self):
        return 3*self.c
class lucgiacdeu(Hinh):
    def dt(self):
        return (sqrt(3)/4)*self.c**2*6
    def cv(self):
        return 6*self.c
class ngugiacdeu(Hinh):
    def dt(self):
        return (sqrt(3)/4)*self.c**2*5
    def cv(self):
        return 5*self.c
class batgiacdeu(Hinh):
    def dt(self):
        return (sqrt(3)/4)*self.c**2*8
    def cv(self):
        return 8*self.c

class HinhTru(tron):
    def v(self):
        return self.dt() * self.h
class HinhHopVuong(vuong):
    def v(self):
        return self.dt() * self.h
class LangTruTamGiac(tamgiacdeu):
    def v(self):
        return self.dt() * self.h

class LangTruLucGiac(tamgiacdeu):
    def v(self):
        return self.dt() * self.h

class LangTruNguGiac(ngugiacdeu):
    def v(self):
        return self.dt() * self.h

class LangTruBatGiac(batgiacdeu):
    def v(self):
        return self.dt() * self.h
c = int(input("Nhập cạnh / bán kính: "))
h= int(input("Nhập chiều cao: "))
print()
htron = HinhTru(c,h)
hvuong = HinhHopVuong(c,h)
htgdeu = LangTruTamGiac(c,h)
hlgdeu = LangTruLucGiac(c,h)
hngdeu = LangTruNguGiac(c,h)
hbgdeu = LangTruBatGiac(c,h)

print(f"Hình tròn:\nChu vi = {htron.cv()}\nDiện tích = {htron.dt()}\nThể tích khối trụ tròn = {htron.v()}\n")
print(f"Hình vuông:\nChu vi = {hvuong.cv()}\nDiện tích = {hvuong.dt()}\nThể tích khối trụ vuông = {hvuong.v()}\n")
print(f"Tam giác đều:\nChu vi = {htgdeu.cv()}\nDiện tích = {htgdeu.dt()}\nThể tích khối trụ tam giác đều = {htgdeu.v()}\n")
print(f"Lục giác đều:\nChu vi = {hlgdeu.cv()}\nDiện tích = {hlgdeu.dt()}\nThể tích khối trụ lục giác đều = {hlgdeu.v()}\n")
print(f"Ngũ giác đều:\nChu vi = {hngdeu.cv()}\nDiện tích = {hngdeu.dt()}\nThể tích khối trụ ngũ giác đều = {hngdeu.v()}\n")
print(f"Bát giác đều:\nChu vi = {hbgdeu.cv()}\nDiện tích = {hbgdeu.dt()}\nThể tích khối trụ bát giác đều = {hbgdeu.v()}\n")