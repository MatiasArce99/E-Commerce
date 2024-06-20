def loginUsuario(): #Nombre de rama "desarrollo"
    print('\nLogin de usuarios\n')
    usuario = input('Ingrese nombre de usuario: ')
    if usuario in au.keys():
        clave = input('Ingrese contraseña: ')
        if clave in au.values():
            print('\nBienvenido {}'.format(usuario))
        else:
            print('\nContraseña incorrecta')
    else:
        print('\nUsuario incorrecto')

def almacenarUsuario():    
    nombreUsuario = input('Ingrese nombre del usuario a registrar: ')
    claveRegistrada = input('Ingrese clave a registrar: ')
    bandera = 1    
    baseDatos = {}
    while bandera == 1:        
       baseDatos.update({nombreUsuario:claveRegistrada})
       registro = input('Desea registrar otro usuario s/n?: ')        
       if registro == 's':
           nombreUsuario = input('Ingrese nombre del usuario: ')
           claveRegistrada = input('Ingrese clave a registrar: ')
           if nombreUsuario in baseDatos.keys():
               print('El usuario {} ya existe. Ingrese uno diferente'.format(nombreUsuario))
               print('\nFin del registro de usuarios')
               break
       else:           
           print('Fin del registro de usuarios\n')
           bandera = 0
           break
    return baseDatos

def mostrarUsuarios():
    print('\nListado de usuarios registrados:\n')
    print(au)

au = almacenarUsuario()
loginUsuario()
mostrarUsuarios()