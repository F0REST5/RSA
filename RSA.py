import sympy
import random
import functools 
import operator 


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

 
qtCreatorFile = "RSA.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
         

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inv(a, n):
    gcd, x, y = egcd(a, n)
    if gcd != 1:
        print("Chyba")
    else:
        return x % n



def generuj_kluce():
    
   p = sympy.randprime(10**12, 10**13) 

   q = sympy.randprime(10**12, 10**13) 
    
   n = p * q
   
   phi = (p - 1) * (q - 1)
   
   e = random.randrange(1, phi)
   
   g = gcd(e , phi)
   
   while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)


   d = inv(e , phi)
   
   
   return ((e,n) , (d,n))


def spaces (text, length):
    return list((text[i:i+length] for i in range(0,len(text),length)))


def TextDec(text):
    
    list_ord = [ord(char) for char in text]
    
    return list_ord


def DecBin(text):
    
    bins = [str(bin(x))[2:].zfill(12) for x in text]
    
    bins = functools.reduce(operator.add , (bins))
  
    return ''.join(bins)


def BinInt(text):    
    
    ints = [int(text[i:i+60], 2) for i in range(0, len(text), 60)]
    
    return ints
    

def IntBin(text):
    
    bins = [str(bin(x))[2:].zfill(60) for x in text]  
    
    bins = functools.reduce(operator.add , (bins))
    
    bins = bins.replace("000000000000","")
  
    return ''.join(bins)
    
    #return bins
    
def BinDec(text):
    
    ints = [int(text[i:i+12], 2) for i in range(0, len(text), 12)]
    
    return ints
        
def DecText(text):
    
    list_char = [chr(i) for i in text]
    
    list_char = functools.reduce(operator.add , (list_char))
  
    return ''.join(list_char)
    

def Sifruj(e,n,text):
     
    blocks = []
    
    
    for blok in text:
     blocks.append(pow(blok,e,n))
    
    return blocks
    

def Desifruj(d,n,sifra):
    
    blocks = []


    for blok in sifra:
        blocks.append(pow(blok,d,n))
        
    return blocks   

    

class RSA(QMainWindow, Ui_MainWindow):
    
    def generuj(self):
        
        public_kluc , private_kluc = generuj_kluce()
        
        self.public_key_gen.setText(str(public_kluc))
        self.private_key_gen.setText(str(private_kluc))
        
        
    def sifruj(self):
                               
        text = self.text_edit.text()
        e = self.e_edit.text()
        n = self.n1_edit.text()
        
       
        textbytes = TextDec(text)
        textbins = DecBin(textbytes)
        textints = BinInt(textbins)
        
        sifra = Sifruj(int(e),int(n),textints)
        self.sifra_browser.setText(str(sifra))
        
        
    def desifruj(self):
        
        text = self.text_edit.text()
        e = self.e_edit.text()
        n = self.n1_edit.text()
        
       
        textbytes = TextDec(text)
        textbins = DecBin(textbytes)
        textints = BinInt(textbins)
        
        sifra = Sifruj(int(e),int(n),textints)
        self.sifra_browser.setText(str(sifra))
        
        
        
        d = self.d_edit.text()
        n = self.n2_edit.text()
               
        desifra = Desifruj(int(d),int(n),sifra)
            
        intbins = IntBin(desifra)
        binsints = BinDec(intbins)
        intschar = DecText(binsints)
        self.desifra_browser.setText(str(intschar))
        
    def vymaz(self):
        self.public_key_gen.clear()
        self.private_key_gen.clear()
        self.text_edit.clear()
        self.e_edit.clear()
        self.n1_edit.clear()
        self.sifra_browser.clear()
        self.d_edit.clear()
        self.n2_edit.clear()
        self.desifra_browser.clear()
        
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.GenButton.clicked.connect(self.generuj)
        self.SifrujButton.clicked.connect(self.sifruj)
        self.DesifrujButton.clicked.connect(self.desifruj)
        self.ClearButton.clicked.connect(self.vymaz)
    
    
    
if __name__ == "__main__":
   
    
   app = QApplication(sys.argv)
   window = RSA()
   window.show()
   sys.exit(app.exec_())
  

    
    
    
    

    

    
  
    

    
    