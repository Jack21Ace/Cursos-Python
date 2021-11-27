# # declaracion de diccionario global
# global diccClient
# diccClient = {}

# def message(sms):
#     print(f"\n{sms}")
#     print("-" * len(sms))


# def opciones():
#     mgc = "Gestor de Clientes"
#     message(mgc)
#     opcMenu = {1:"Registrar Cliente", 2:"Listar Clientes", 3:"Buscar Clientes", 4:"Salir"}
#     for op, opm in opcMenu.items():
#         print(f"{op}. {opm}.")

# def registrarCliente():
#     mgc = "Registrando Cliente"
#     message(mgc)
#     idCliente = str(input("Ingrese su DNI: "))
#     nombreCliente = str(input("Ingrese su nombre: "))
#     diccClient[idCliente]=nombreCliente
#     print(f"\n{idCliente} ---> {nombreCliente}")


# def listarCliente():
#     mgc = "Listado de clientes"
#     message(mgc)
#     for id, cli in diccClient.items():
#         print(f"\t{id}: {cli}")

# def buscarCliente():
#     mgc = "Buscar Cliente"
#     message(mgc)
#     idC = input("Ingrese Identificación ")
#     if diccClient.get(idC, 0) == 0:
#         print("Cliente no registrado")
#     else:
#         print(f"\t{idC}: {diccClient[idC]}")

# def menu():
#     op = 0
#     while op != 4:
#         opciones()
#         op = int(input("Indique una opción [1..4] -> "))
#         if op in range(1,5):
#             if op == 1:
#                 registrarCliente()
#             elif op == 2:
#                 listarCliente()
#             elif op == 3:
#                 buscarCliente()
#             else:
#                 print("\tBye")
#         else:
#             print(f"Opcion no valida -> {op}")
#             return menu()

# menu()