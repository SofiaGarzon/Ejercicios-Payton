#Se hace el metodo principal
def main():
    numero_tabla = int(input("Digite el numero del cual quiere saber la tabla: "))
    
    #Se iteran los numeros de 0 a 10, se pone +1 para empezar desde 1
    for i in range(10):
        print(f"{numero_tabla} x {i + 1} = {numero_tabla * (i + 1)}")
    
main()