import numpy as np
import keyboard as kb

col= 4
righe =4
class grid():
    def __init__(self):
        self.griglia=np.zeros((righe,col),int)
        
    def stampa(self):
        return print(np.flip(self.griglia,0))
        
        
    def inizio_g(self):
        posx = np.random.randint(4, size=2)
        posy = np.random.randint(4, size=2)
        while posx[0] == posx[1] and posy[0] == posy[1]:
            posx = np.random.randint(4, size=2)
            posy = np.random.randint(4, size=2)
        self.griglia[posx[0]][posy[0]] = 2
        self.griglia[posx[1]][posy[1]] = 2
        
    def ins_num(self):
        while True:
            posx=np.random.randint(4)
            posy=np.random.randint(4)
            if self.griglia[posx][posy]==0:
                self.griglia[posx][posy]=np.random.choice([2,4])
                break
    
    def comprimi(self,griglia):
        g1=np.zeros((righe,col),int)

        for i in range (righe):
                pos=0
                for e in range (col):
                    if griglia[i][e]!=0:
                        g1[i][pos]=griglia[i][e]
                        pos+=1
        return g1
    def somma(self,griglia):
        for i in range(righe):
                for j in range(col-1):
                    if griglia[i][j] == griglia[i][j + 1] and griglia[i][j] != 0:
                        griglia[i][j] *= 2
                        griglia[i][j + 1] = 0
        return griglia


        
    def muovi(self,dir):
        if dir == "w":
            self.griglia = np.rot90(self.griglia, -1)

            self.griglia = self.comprimi(self.griglia)
            self.griglia = self.somma(self.griglia)
            self.griglia = self.comprimi(self.griglia)
                
            self.griglia = np.rot90(self.griglia, 1)
            self.ins_num()
            self.stampa()
                

        elif dir == "s":
            self.griglia = np.rot90(self.griglia, 1)

            self.griglia = self.comprimi(self.griglia)
            self.griglia = self.somma(self.griglia)
            self.griglia = self.comprimi(self.griglia)

            self.griglia = np.rot90(self.griglia, -1)
            self.ins_num()
            self.stampa()
                

        elif dir== "a":
            self.griglia = self.comprimi(self.griglia)
            self.griglia = self.somma(self.griglia)
            self.griglia = self.comprimi(self.griglia)
            self.ins_num()
            self.stampa()               
                

        elif dir == "d":
            self.griglia = np.fliplr(self.griglia)

            self.griglia = self.comprimi(self.griglia)
            self.griglia = self.somma(self.griglia)
            self.griglia = self.comprimi(self.griglia)
                
            self.griglia = np.fliplr(self.griglia)
            self.ins_num()
            self.stampa() 



if __name__ == "__main__":
    g=grid()
    g.inizio_g()
    g.stampa()




