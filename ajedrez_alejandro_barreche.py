### AJEDREZ ###

# Definición de las posiciones iniciales de las fichas
pos_inicial_peon_blanco = ((6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7))
pos_inicial_peon_negro = ((1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7))
pos_inicial_alfil_blanco = ((7,2), (7,5))
pos_inicial_alfil_negro = ((0,2), (0,5))
pos_inicial_caballo_blanco = ((7,1), (7,6))
pos_inicial_caballo_negro = ((0,1), (0,6))
pos_inicial_torre_blanco = ((7,0), (7,7))
pos_inicial_torre_negro = ((0,0), (0,7))
pos_inicial_reina_blanco = ((7,3),)
pos_inicial_reina_negro = ((0,3),)
pos_inicial_rey_blanco = ((7,4),)
pos_inicial_rey_negro = ((0,4),)

# Clase Tablero
class Tablero:
    def __init__(self):
        self.tablero = []
        self.filas = 8
        self.columnas = 8
        self.peon_blanco = "♙"
        self.alfil_blanco = "♗"
        self.caballo_blanco = "♘"
        self.torre_blanco = "♖"
        self.reina_blanco = "♕"
        self.rey_blanco = "♔"
        self.peon_negro = "♟"
        self.alfil_negro = "♝"
        self.caballo_negro = "♞"
        self.torre_negro = "♜"
        self.reina_negro = "♛"
        self.rey_negro =  "♚"

    '''
    tablero: list
    filas: int
    columnas: int
    todas las fichas: str
    '''


    # Pedir el nombre del archivo.txt que se cree
    def pedir_nombre_archivo(self):
        while True:
            nom = input("Dime el nombre del archivo: ")
            try:
                nom = str(nom)
                self.nombre_archivo = nom
                break
            except:
                nom = input("Dime el nombre del archivo: ")
     
    # Creamos el tablero y lo rellenamos con las piezas        
    def crear_tablero(self):
        for i in range(self.filas):
            x = []
            for j in range(self.columnas):
                if (i,j) in pos_inicial_peon_blanco:
                    x.append(self.peon_blanco)
                elif (i,j) in pos_inicial_peon_negro:
                    x.append(self.peon_negro)
                elif (i,j) in pos_inicial_alfil_blanco:
                    x.append(self.alfil_blanco)
                elif (i,j) in pos_inicial_alfil_negro:
                    x.append(self.alfil_negro)
                elif (i,j) in pos_inicial_caballo_blanco:
                    x.append(self.caballo_blanco)
                elif (i,j) in pos_inicial_caballo_negro:
                    x.append(self.caballo_negro)
                elif (i,j) in pos_inicial_torre_blanco:
                    x.append(self.torre_blanco)
                elif (i,j) in pos_inicial_torre_negro:
                    x.append(self.torre_negro)
                elif (i,j) in pos_inicial_reina_blanco:
                    x.append(self.reina_blanco)
                elif (i,j) in pos_inicial_reina_negro:
                    x.append(self.reina_negro)
                elif (i,j) in pos_inicial_rey_blanco:
                    x.append(self.rey_blanco)
                elif (i,j) in pos_inicial_rey_negro:
                    x.append(self.rey_negro)
                else:
                    x.append(" ")
            self.tablero.append(x)
    
    # Muestra por pantalla el tablero        
    def mostrar_tablero(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                print(self.tablero[i][j], end="\t")
            print()
        
    # Manda al archivo.txt creado el tablero    
    def guardar_tablero_archivo(self,numero_movimiento):
        with open(self.nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"\nEste es el tablero número {numero_movimiento}:\n")
            for fila in self.tablero:
                archivo.write("\t".join(fila) + "\n")
                numero_movimiento += 1

#Clase Movimiento heredada de tablero
'''
Esta clase está destinada únicamente al movimiento de las fichas del tablero
'''
class Movimiento(Tablero):
    def __init__(self):
        super().__init__(self)
        self.tablero = []
        self.filas = 8
        self.columnas = 8
        self.peon_blanco = "♙"
        self.alfil_blanco = "♗"
        self.caballo_blanco = "♘"
        self.torre_blanco = "♖"
        self.reina_blanco = "♕"
        self.rey_blanco = "♔"
        self.peon_negro = "♟"
        self.alfil_negro = "♝"
        self.caballo_negro = "♞"
        self.torre_negro = "♜"
        self.reina_negro = "♛"
        self.rey_negro =  "♚"
        
    def preguntar_fila(self):
        while True:
            fila_inicial = input("Dime la fila de la ficha que quieres mover: ")
            try:
                fila_inicial = int(fila_inicial)
                if 1 <= fila_inicial <= 8:
                    self.fila_inicial = fila_inicial
                    print(self.fila_inicial)
                    return self.fila_inicial
                else:
                    print("Entrada no válida. Introduce un número del 1 al 8")
            except:
                print("Entrada no válida. Introduce un número del 1 al 8")
                
    def preguntar_columna(self):
        while True:
            columna_inicial = input("Dime la columna de la ficha que quieres mover: ")
            try:
                columna_inicial = int(columna_inicial)
                if 1 <= columna_inicial <= 8:
                    self.columna_inicial = columna_inicial
                    print(self.columna_inicial)
                    return self.columna_inicial
                else:
                    print("Entrada no válida. Introduce un número del 1 al 8")
            except:
                print("Entrada no válida. Introduce un número del 1 al 8")
        
    def preguntar_donde_ir_fila(self):
        while True:
            fila_final = input("Dime la fila a la que te quieres mover: ")
            try:
                fila_final = int(fila_final)
                if 1 <= fila_final <= 8:
                    self.fila_final = fila_final
                    print(self.fila_final)
                    return self.fila_final
                else:
                    print("Entrada no válida. Introduce un número del 1 al 8")
            except ValueError:
                print("Entrada no válida. Introduce un número del 1 al 8")

    def preguntar_donde_ir_columna(self):
        while True:
            columna_final = input("Dime la columna a la que te quieres mover: ")
            try:
                columna_final = int(columna_final)
                if 1 <= columna_final <= 8:
                    self.columna_final = columna_final
                    print(self.columna_final)
                    return self.columna_final
                else:
                    print("Entrada no válida. Introduce un número del 1 al 8")
            except ValueError:
                print("Entrada no válida. Introduce un número del 1 al 8")

    def mover_pieza(self):   
        x = self.tablero[self.fila_inicial - 1][self.columna_inicial - 1]
        self.tablero[self.fila_inicial - 1][self.columna_inicial - 1] = " "
        self.tablero[self.fila_final - 1][self.columna_final - 1] = x
                
    def preguntar_todo(self):
        self.preguntar_fila()
        self.preguntar_columna()
        self.preguntar_donde_ir_fila()
        self.preguntar_donde_ir_columna() 
        
def seguir_jugando():
    while True:
        pregunta = input("Pulsa 'f' para dejar de jugar, o pulsa enter para seguir jugando: ")
        try:
            pregunta = str(pregunta)
            if pregunta == "f" or pregunta == "":
                return pregunta
            else:
                print("Pulsa una tecla válida")
                print()
        except:
            print("Pulsa una tecla válida")


def main():
    tablero1 = Movimiento()

    tablero1.crear_tablero()
    tablero1.pedir_nombre_archivo()

    numero_intento = 1
    seguir = ""
    while seguir != "f":
        tablero1.mostrar_tablero()
        print()
        tablero1.guardar_tablero_archivo(numero_intento)
        tablero1.preguntar_todo()
        tablero1.mover_pieza()
        seguir = seguir_jugando()
        numero_intento += 1
            
if __name__ == "__main__":
    main()