
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

    print("¡ERROR!, ingrese un valor valido"); 


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

    print("\nLibros: ")

    # Por cada libro en libros;

    for libro in libros:

      # Muestrame cada libro;

      print(f"\n{libro}"); 

def salir ():

  # Mensaje de finalizacion de sistema;

  print("\nGracias por usar el sistema. Vuelva Pronto"); 

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
      
      # Si la opcion es 5;
    
      if opcion == 5:
         
        # Muestra los libros;
         
         mostrar_libros(); 
    
      if opcion == 6:

        # Salir del sistema;

        salir(); 

        # Cierre de ciclo;

        break; 
         
    # Manejo de errores a nivel de menu;

    except ValueError:
        
      print("\n¡ERROR!, digite una opcion valida"); 