# Ejercicio de cajero automatico
import numpy as np
import random

#saldo = np.random.random_integers(0,5000000,1)
saldo = random.randrange(0,5000000)

def cajero():
    menu = int(input("""
    Wellcome...
    This is a new ATH
    Please choose an option below
    1. Balance Inquiry
    2. Extract Money
    3. Deposit Money
    4. Transfer Money
    5. Exit/Quit
    """))
    if menu in range(1,5):
        if menu == 1:
            print(f"Su saldo disponible es: {saldo}")
            return cajero()
        elif menu == 2:
            monto = int(input("Indique monto a retirar:\n"))
            if monto > saldo:
                print("Saldo no disponible...")
                return cajero()
            else:
                saldo = saldo - monto
                print("Retire su dinero...")
                print(f"Su saldo actual es: {saldo}")
                return cajero()
        elif menu == 3:
            monto = int(input("Indique monto a depositar:\n"))
            saldo = saldo + monto
            print(f"Su saldo actual es {saldo}")
            return cajero()
        elif menu == 4:
            cuenta = input("Indique numero de cuenta a transferir\n")
            monto = int(input("Indique el monto a transferir"))
            if monto > saldo:
                print("La operación no se puede ejecutar: Saldo insuficiente...")
            else:
                saldo = saldo - monto
                print(f"Transferencia realizada exitosamente a la cuenta {cuenta}")
                print(f"Su saldo disponible es: {saldo}")
                return cajero()
        elif menu == 5:
            print("See you soon...")


cajero()