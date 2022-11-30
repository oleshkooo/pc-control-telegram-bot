
class Fitter():
     def __init__(self):
        self.field1 = 0

        # Imported methods
        from ._plotstuff import plot as _plot, clear as _clear
        self.plot = _plot(self)

     # static methods need to be set
    #  from ._static_example import something
    #  something = staticmethod(something)

     # Some more small functions
     def printHi(self):
         print("Hello world")