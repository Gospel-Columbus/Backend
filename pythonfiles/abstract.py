from abc import ABC, abstractmethod

#Abstract class contains one or more method.
class Shape(ABC):
    @abstractmethod
    def area(self):
            pass
    @abstractmethod
    def perimeter(self):
            pass
    
class Square(Shape):
        def _init(self,side): 
            self.__side = side #side is equal to 5.
                
            def area(self):
                        
              return self.__side * self.__side
              
              
        def perimeter(self):
                return 4 * self._side
        
#instantiating
mysquare = Square(5)

print(mysquare.area())

print(mysquare.perimeter())