#Básico:
#Login de usuario-administrador: Al ejecutar el programa, solicitar al usuario sus datos #de acceso (nombre de
#usuario y contraseña) y permitir visualizar el reporte #siempre que los datos sean
#correctos.
#Definir dentro del código el siguiente usuario que deberá tener permisos de
#administrador:
#nombre de usuario: emtech
# contraseña: caso1
#Productos más vendidos y productos rezagados:
#Generar un listado de los 5 productos con mayores #ventas y uno con los 10
#productos con mayor búsquedas.
 # generar un listado con los 5 productos #con menores ventas y
#uno con los 10 productos con menores búsquedas.

Nombredeusuario= input("Escribe tu nombre de usuario(emtech): ")
listadeproductosconmayorventa=[
  "lista de los 5 productos  más vendidos: "
                              
  "1-Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, SixCore, 16MB L3 Cache, con Disipador Wraith Stealth, "
  "2-Tarjeta Madre ASRock Micro ATX B450M Steel Legend,S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD, "
  "3-SSD XPG SX8200 Pro, 256GB, PCI Express, M.2, "
  "4-SSD Adata Ultimate SU800, 256GB, SATA III, 2.5'' "
  "5-Tarjeta de Video EVGA NVIDIA GeForce GTX 1660 Ti SC Ultra Gaming, 6GB 192-bit GDDR6, PCI 3.0"
  ""]  


productosconmayorbusqueda=["los 10 productos con mayor busqueda son:  " 
                           "1-Procesador AMD Ryzen 5 3600, S-AM4, 3.60GHz, 32MB L3 Cache, con Disipador Wraith Stealth,"
                           "2-Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, Six-Core, 16MB L3 Cache, con Disipador Wraith Stealth,"
                           "3-Procesador AMD Ryzen 3 3200G con Gráficos Radeon Vega 8, S-AM4, 3.60GHz, Quad-Core, 4MB L3, con Disipador Wraith Spire,"
                           "4-Procesador Intel Core i3-9100F, S-1151, 3.60GHz, Quad-Core, 6MB Cache (9na. Generación - Coffee Lake),"
                           "5-SSD Kingston A400, 120GB, SATA III, 2.5'', 7mm,"
                           "6-Logitech Audífonos Gamer G635 7.1, Alámbrico, 1.5 Metros, 3.5mm, Negro/Azul,"
                           "7-SSD Adata Ultimate SU800, 256GB, SATA III, 2.5'', 7mm,"
                           "8-arjeta Madre ASUS micro ATX TUF B450M-PLUS GAMING, S-AM4, AMD B450, HDMI, 64GB DDR4 para AMD,"
                           "9-Procesador Intel Core i7-9700K, S-1151, 3.60GHz, 8-Core, 12MB Smart Cache (9na. Generación Coffee Lake),"
                           "10-SSD Kingston A2000 NVMe, 1TB, PCI Express 3.0, M2' , 2559 , 'discos duros,"
                          ]

listadeproductosconmenorventa=[ "lista de los 5 productos  menos vendidos: "
                              
                                "1-Tarjeta de Video EVGA NVIDIA GeForce GT 710, 2GB 64-bit GDDR3, PCI Express 2.0' , 1439 , 'tarjetas de video' "
                                "2-Tarjeta de Video EVGA NVIDIA GeForce GTX 1660 Ti SC Ultra Gaming, 6GB 192-bit GDDR6, PCI 3.0' , 8439 , 'tarjetas de video, "
                                "3-Tarjeta de Video EVGA NVIDIA GeForce RTX 2060 SC ULTRA Gaming, 6GB 192-bit GDDR6, PCI Express 3.0' , 9799 , 'tarjetas de video, "
                                "4-Makena Smart TV LED 40S2 40'', Full HD, Widescreen, Negro, "
                                "5- Tarjeta de Video Gigabyte NVIDIA GeForce GTX 1650 OC Low Profile, 4GB 128-bit GDDR5, PCI Express 3.0 x16' , 4509 , 'tarjetas de video'"
                               "                        "
                                
                                 ]

productosconmenorbusqueda=[ "Los 10 productos con menor busqueda son: "
                              
                                "1-Tarjeta de Video MSI Radeon X1550, 128MB 64 bit GDDR2, PCI Express x16' , 909 , 'tarjetas de video, "
                                "2-Tarjeta de video PNY NVIDIA GeForce RTX 2080, 8GB 256-bit GDDR6, PCI Express 3.0 \xa0 ' , 30449 , 'tarjetas de video, "
                                "3-arjeta de Video EVGA NVIDIA GeForce GT 710, 2GB 64-bit GDDR3, PCI Express 2.0' , 1439 , 'tarjetas de video, "
                                "4-ASUS Audífonos Gamer ROG Theta 7.1, Alámbrico, USB C, Negro' , 8359 , 'audifonos' , "
                                "5-Tarjeta Madre ASUS ATX ROG STRIX Z390-E GAMING, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel' , 6369 , 'tarjetas madre',"
                                " 6-Getttech Audífonos con Micrófono Sonority, Alámbrico, 1.2 Metros, 3.5mm, Negro/Rosa' , 149 , 'audifonos,"
                                "7-Tarjeta Madre ASRock Z390 Phantom Gaming 4, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel \xa0 ' , 4309 , 'tarjetas madre'  ,"
                                " 8-Tarjeta Madre ASUS ATX PRIME Z390-A, S-1151, Intel Z390, HDMI, 64GB DDR4 para Intel \xa0 ' , 4269 , 'tarjetas madre',"
                                " 9-arjeta Madre ASUS ATX ROG STRIX B550-F GAMING WI-FI, S-AM4, AMD B550, HDMI, máx. 128GB DDR4 para AMD' , 5289 , 'tarjetas madre',"
                                "10-Tarjeta de Video Gigabyte NVIDIA GeForce RTX 2060 SUPER WINDFORCE OC, 8 GB 256 bit GDDR6, PCI Express x16 3.0' , 11509 , 'tarjetas de video',"
                          "                            "]    

                   
if Nombredeusuario=="emtech":
  contraseña=input("escriba su contraseña(caso1): ")
else:
  print("El nombre de usuario es incorrecto ")
  
if contraseña=="caso1":
  print ("A contunuación se muestran las listas de produtos más vendidos, menos vendidos, más buscados y menos buscados:                                      ")
  print(listadeproductosconmayorventa)
  print(productosconmayorbusqueda)
  print(listadeproductosconmenorventa)
  print(productosconmenorbusqueda)
else:
  print("contraseña incorrecta")




 