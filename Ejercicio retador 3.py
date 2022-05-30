#ejercicio retador 3
#En este sentido, el director de logística de la empresa te solicita un programa en Python que les
#permita saber si se podrá realizar o no la entrega de un pedido según las restricciones
#anteriores y el número de costales de cemento y yeso que fueron requeridos por el cliente.

costalesdecemento= input("Dame la cantidad de costales de cemento ")
costalesdeyeso= input ("Dame la cantidad de costales de yeso ")
costalesdecemento12=int(costalesdecemento)
costalesdeyeso123=int(costalesdeyeso)
pesocemento=40
pesoyeso=30

pesocemento1= costalesdecemento12*pesocemento
pesoyeso2= costalesdeyeso123*pesoyeso
pesototal= pesocemento1+pesoyeso2

print("el peso total es ",pesototal,"kg")

if pesototal<=3254  and pesototal>1627:
  print("¿Se puede realizar el envío?: Sí")
else :
  print("¿Se puede realizar el envío?:No")
