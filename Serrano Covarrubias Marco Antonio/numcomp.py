class NumeroComplejo:
    parteReal=0
    parteImag=0
    
    def __init__(self, real=0, imag=0):
        self.parteReal=real
        self.parteImag=imag
        
    def impNumComp(self):
        print(str(self.parteReal)+" + " + str(self.parteImag)+ "i")
        
    def cambParteReal(self, real):
        self.parteReal=real
        
    def cambParteImag(self, imag):
        self.parteImag=imag
    
    def obtenerParteReal(self):
        return self.parteReal
    
    def obtenerParteImag(self):
        return self.parteImag
    
    def sumaComp(self, numero):
        self.parteReal=self.parteReal+ numero.parteReal
        self.parteReal=self.parteImag+ numero.parteImag
    
    def restaComp(self, numero):
        self.parteReal=self.parteReal- numero.parteReal
        self.parteReal=self.parteImag- numero.parteImag
    
    def __add__(self, numero):
        self.parteReal=self.parteReal+ numero.parteReal
        self.parteReal=self.parteImag+ numero.parteImag
        
    def multComp(self, numero):
        AuxReal=self.parteReal* numero.parteReal- self.parteImag*numero.parteImag
        self.parteImag=self.parteReal* numero.parteImag+ self.parteImag*numero.parteReal
        self.parteReal=AuxReal
        
    def conj(self):
                self.parteImag=self.parteImag*(-1)
                
    def incr(self):
             self.parteReal=self.parteReal+1
             self.parteImag=self.parteImag+1
             
numComp1= NumeroComplejo(10.0,5.0)
print("numero complejo 1")
numComp1.impNumComp()
    
numComp2=NumeroComplejo()
print("numero complejo 2")
numComp2.impNumComp()
    
numComp3=NumeroComplejo(3,4)
print("numero complejo 3")
numComp3.impNumComp()
    
numComp1.sumaComp(numComp3)
print("numero complejo 1")
numComp1.impNumComp()
    
numComp1+numComp3
print("numero complejo 1")
numComp1.impNumComp
    
numComp1.cambParteImag(20)
print("numero complejo 1")
numComp1.impNumComp()
    
numComp1.incr()
print("numero complejo 1 incrementado")
numComp1.impNumComp()
    
numComp1.conj()
print("numero complejo 1 conjugado")
numComp1.impNumComp()
  
numComp6=NumeroComplejo(3.0,2.0)
print("numero complejo 6")
numComp6.impNumComp()
    
print(numComp6.obtenerParteReal())
print(numComp6.obtenerParteImag())
    
numComp7=NumeroComplejo(-2.0,3.0)
print("numero complejo 7")
numComp7.impNumComp()
 
print(numComp7.obtenerParteReal())
print(numComp7.obtenerParteImag())
    
numComp6.multComp(numComp7)
print("numero complejo 6")
numComp6.impNumComp()
    
print(numComp6.obtenerParteReal())
print(numComp6.obtenerParteImag())
 
print(numComp7.obtenerParteReal())
    
print(numComp7.obtenerParteImag())
    
parteR= float(input("\n Ingresa real  "))
parteI= float(input("\n Ingresa imaginaria  "))
 
numComp20=NumeroComplejo(parteR,parteI)
print("Numero complejo 20")
numComp20.impNumComp()    