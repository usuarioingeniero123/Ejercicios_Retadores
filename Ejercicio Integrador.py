#Ejerciciointegrador
#Con esto en cuenta, ahora el programa deberá mostrar como salida, el nombre del producto
#que se seleccionó, el precio unitario por caja para ese producto, si aplica o no el descuento del
#20% según la suma de ventas acorde a la lista ventas_productos y el monto total de la venta
#contemplando el costo de envío de $1,500 pesos siempre y cuando la cantidad de cajas a
#vender sea menor o igual a 100 unidades más y el descuento si las ventas totales superan las
#1500 cajas.


cajas= input("número de cajas a vender: ")
Id= input("Deme el id del producto (tiene que ser del 1-3) ")


Id1=int(Id)
caja1=int(cajas)
pepino=334.72
tomateverde=129.00
Maizgrano=285.55

cajadepepino= caja1*pepino+1500
cajadetomateverde= caja1*tomateverde+1500
cajademaizgrano= caja1*Maizgrano+1500
cajadepepino2= caja1*pepino
cajadetomateverde2= caja1*tomateverde
cajademaizgrano2=caja1*Maizgrano
descuento1=cajadepepino2*0.2
descuento2=cajademaizgrano2*0.2
descuento3=cajadetomateverde2*0.2
cajadepepinocondescuento= cajadepepino2-descuento1
cajademaizgranodescuento= cajademaizgrano2-descuento2
cajadetomateverdedescuento= cajadetomateverde2-descuento3


 
if  Id1==1   and  caja1<=100:
  print("el producto es maíz grano")
  print("el precio de la caja es $285.55")
  print("¿Aplica el descuento del 20%?NO")
  print("El costo total a pagar es",cajademaizgrano)
  
  
elif  Id1==1   and  caja1<1500:
  print("el producto es maíz grano")
  print("el precio de la caja es $285.55")
  print("¿Aplica el descuento del 20%?Sí")
  print("El costo total a pagar es",cajademaizgranodescuento)
  
elif Id1==1:
  print("el producto es maíz grano")
  print("el precio de la caja es 285.55")
  print("la cantidad de cajas es mayor a 100 así que no  se cobra envio su monto a pagares:",cajademaizgrano2)
  

elif Id1==2 and caja1<=100:
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("¿Aplica el descuento del 20%?NO")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envió",cajadepepino) 
  
elif Id1==2 and caja1<1500 :
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("¿Aplica el descuento del 20%?Sí")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajadepepinocondescuento)
 
  
elif Id1==2:
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("la cantidad de cajas es mayor a 100 así que no se que no se cobra envío: ",cajadepepino2) 
  
if  Id1==3 and  caja1<=100:
  print("el producto es tomate verde")
  print("el precio de la caja es $129.00")
  print("¿Aplica el descuento del 20%?NO")
  print("El costo total a pagar es",cajadetomateverde)
  
elif Id1==3 and caja1<1500 :
  print("el producto es tomate verde")
  print("el precio de la caja es $129.00")
  print("¿Aplica el descuento del 20%?Sí")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajadetomateverdedescuento)
  
elif Id==3:
  print("el producto es tomate verde")
  print("el precio de la caja es $129.00")
  print("la cantidad de cajas es mayor a 100 así que no se cobra envio su monto a pagar es:",cajadetomateverde2) 
        
if Id1<10000000 and Id1>3:
  print("el número de iD es incorrecto, haga el favor de ingresar otro")