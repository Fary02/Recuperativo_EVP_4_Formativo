
# Se crea array que alamacenara cada objeto / diccionario;

libros = []; 

# Se crean functions a utilizar;

def menu_principal ():

  # Menu principal;
   
  print("\n********MENU PRINCIPAL********"); 
  print("1. Agregar libro"); 
  print("2. Buscar libro"); 
  print("3. Eliminar libro"); 
  print("4. Actualizar disponibilidad"); 
  print("5. Mostrar libros"); 
  print("6. Salir"); 

def opcion_ingresada ():

  # Solicita una opcion;
   
  opcion = int(input("\nPor favor, digite una opcion: ")); 

  # Retorna la opcion;

  return opcion; 

def agregar_libro ():

  # Intenta solicitar datos del libro;

  try: 

    titulo_libro = str(input("\nDigite el nombre del libro: ")); 

    filtro_libro_len = len(titulo_libro); 

    # Si se cumplen las condiciones;

    if filtro_libro_len >= 1 and titulo_libro.strip():

      copias_libro = int(input("\nDigite el stock disponible: ")); 

      if copias_libro >= 1 and copias_libro != 0 or copias_libro < 0: 

        prestamo_libro = int(input("\nDigite la cantidad de dias para prestar el libro: ")); 
 
        if prestamo_libro > 0:

          disponibilidad_libro = False; 

          # Diccionario / objeto con la informnacion del libro;

          libro = {

            "Libro": titulo_libro,

            "Stock": copias_libro,

            "Prestamo": prestamo_libro,

            "Disponibilidad": disponibilidad_libro

          }

          # Agrega el diccionario al array de libros;

          libros.append(libro); 

          # Mensaje de confirmacion;

          print(f"\n{libro}, agregado correctamente"); 
  
  # except ValueError para manejo de errores; # No toma el mensaje de error;
  
  except ValueError: 

    print("\n¡ERROR!, ingrese un valor valido"); 

def buscar_libro(libros, nombre):
  
  # Recorre el array buscando el nombre del libro;

  for nombre in range(len(libros)):

    # Si el nombre coincide con el titulo;

    if libros[nombre]["Libro"] == nombre:

      # Retorna el numero del index;

      return nombre; 

def buscar_titulo ():

  # Se solicita el nombre del libro;

  buscar_libro = str(input("\nDigite el nombre del libro a buscar: ")); 
      
  # Se llama a la function pasandole el array y el nombre;

  posicion_libro = buscar_libro(libros, buscar_libro); 

  if posicion_libro != -1:

    # Mensaje informativo sobre la posicion del libro en el index;

    print(f"\nTitulo encontrado en la posicion {posicion_libro}: ");  

    # Se imprime el libro en la posicion del index;

    print(libros[posicion_libro]); 

  # De lo contrario avisa al usuario que el libro no esta registrado;

  else:

    print(f"\nEl libro: {buscar_titulo}, no esta registrado."); 

def eliminar_libro ():

  # Se solicita el nombre del libro a eliminar;

  libro_eliminar = str(input("\nDigite el nombre del libro que desea eliminar: ")); 

  # Se recicla la function de busqueda;

  posicion_libro = buscar_libro(libros, libro_eliminar); 

  # Si tiene un index valido se elimina;

  if posicion_libro != 1:

    libro_eliminado = libros.pop(posicion_libro); 

    # Mensaje informativo con la confirmacion;

    print(f"\nEl libro: {libro_eliminar} ha sido eliminado exitosamente."); 

    # De lo contrario mensaje informativo;

  else:

    print(f"\nEl libro: {libro_eliminar} no se encuentra registrado, registrelo en la opcion 1."); 

def actualizar_disponibilidad(libros):

  # Recorre el array de libros;

  for libro in libros:

    # Si las copias son mayor o igual a 1 cambia a True;

    if libro ["Stock"] >= 1:

      libro ["Disponibilidad"] = True; 
    
      # Mensaje informativo;

      print("\nDisponibilidad actualizada"); 

    # De lo contrario mantiene en False;

    else:

      libro ["Disponibilidad"] = False; 

def mostrar_libros ():

  # Filtro para cuando el array este vacio;

  filtro_libros_len = len(libros); 

  # Si el array esta vacio;
  
  if filtro_libros_len == 0:

    # Imprime el mensaje informativo;

    print("\n¡Usted no posee libros, agreguelos en la opcion 1!"); 
  
  # De lo contrario;
  
  else:

    # Mensaje decorativo;

    print("\nLibros: "); 

    # Por cada libro en libros;

    for libro in libros:

      # Muestrame cada libro;

      print(f"\n{libro}"); 

def salir ():

  # Mensaje de finalizacion de sistema;

  print("\nGracias por usar el sistema. ¡Vuelva Pronto!"); 

# Comienzo de bucle;

while True:
    
    # Muestra el menu;

    menu_principal(); 

    # Intenta lo siguiente;

    try:

      # Definimos la function nuevamente para validar la opcion ingresada;
        
      opcion = opcion_ingresada(); 

      # Si la opcion es 1;
    
      if opcion == 1:

        # Agrega el libro;

        agregar_libro(); 
      

      # Si la opcion es 2;

      if opcion == 2:

        # Busca el titulo del libro;

        buscar_titulo(); 
      
      # Si la opcion es 3:

      if opcion == 3:

        # Elimina el libro;

        eliminar_libro(); 
      
      # Si la opcion es 4:

      if opcion == 4:

        # Actualiza la disponibilidad;

        actualizar_disponibilidad(libros); 

      # Si la opcion es 5;
    
      if opcion == 5:
         
        # Muestra los libros;
         
         mostrar_libros(); 

      # Si la opcion es 6;
    
      if opcion == 6:

        # Salir del sistema;

        salir(); 

        # Cierre de ciclo;

        break; 
    
      # Si no es una opcion disponible;

      if not opcion > 0 and opcion <= 6:

        print("\n¡ERROR!, digite una opcion disponible"); 
         
    # Manejo de errores a nivel de menu;

    except ValueError:
        
      print("\n¡ERROR!, digite una opcion valida"); 