#Ejercicio
#Retador #4
#Sentencias condicionales:
#if, if-else, if-elif-else
#El programa deberá solicitarle al responsable del almacén de distribución ingresar la siguiente
#información: cantidad de cajas a vender y el tipo de producto por ID (Ver tabla 1).
#Posterior a esto, el programa deberá mostrar como salida, el nombre del producto que se
#seleccionó, el precio unitario por caja para ese producto y el monto total de la venta, teniendo
#en cuenta un costo de envío de $1,500 pesos, siempre y cuando la cantidad de cajas a vender
#sea menor o igual a 100 unidades.

cajas= input("número de cajas a vender ")
Id= input("Deme el id del producto ")

Id1=int(Id)
caja1=int(cajas)
pepino=334.72
tomateverde=129.00
Maizgrano=285.55

cajadepepino= caja1*pepino+1500
cajadetomateverde= caja1*tomateverde+1500
cajademaizgrano= caja1*Maizgrano+1500
cajadepepino2= caja1*pepino
cajadetomateverde2= caja1*cajadetomateverde
cajademaizgrano2=caja1*cajademaizgrano

if  Id1==1   and  caja1<=100:
  print("el producto es maíz grano")
  print("el precio de la caja es $285.55")
  print("El costo total a pagar es",cajademaizgrano)
elif Id1==1 :
  print("el producto es maíz grano")
  print("el precio de la caja es 285.55")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajademaizgrano) 
if  Id1==2 and  caja1<=100:
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("El costo total a pagar es",cajadepepino)
elif Id1==2 :
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajadepepino2)
if  Id1==3 and  caja1<=100:
  print("el producto es tomate verde")
  print("el precio de la caja es $129.00")
  print("El costo total a pagar es",cajadetomateverde)
elif Id1==3 :
  print("el producto es tomate verde")
  print("el precio de la caja es $129.00")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajadetomateverde2)
else:
  print("el número de iD es incorrecto, haga el favor de ingresar otro")
  