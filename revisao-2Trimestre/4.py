import sqlite3

def connection_db():                                          
    connection = sqlite3.connect('hotelaria.db')     # ==========================================
    cursor = connection.cursor()                     # FUNÇÃO DE CONEXÃO CENTRALIZADA (Princípio DRY)
    cursor.execute("PRAGMA foreign_keys = ON")       # ==========================================
    return connection, cursor                        # Por que criar isso?
#                                                      Em vez de repetir as configurações de conexão, cursor e PRAGMA
#                                                      em todas as funções (o que gerava código repetitivo), nós centralizamos tudo aqui.
                                                                                          
#                                                      Como funciona:
#                                                       1. Abre a conexão com o banco de dados SQLite ('hotelaria.db').
#                                                       2. Cria um objeto cursor para executar os comandos SQL.
#                                                       3. Ativa as chaves estrangeiras (PRAGMA foreign_keys = ON),
#                                                          já que o SQLite vem com elas desativadas por padrão.
#                                                       4. Retorna ambos os objetos para que as funções possam consultar
#                                                            e salvar alterações, mantendo o código limpo e fácil de manter.
#                                                       ==========================================                                                  



def create_database():
    connection = None    # Inicializa a variável para evitar UnboundLocalError
    cursor = None

    try:
        connection, cursor = connection_db()

        cursor.execute('''CREATE TABLE IF NOT EXISTS hotels (
                       id_hotel INTEGER PRIMARY KEY AUTOINCREMENT,
                       hotel_name TEXT,
                       hotel_city TEXT
                       )
                       ''')
        

        # daily_rate = preco_diaria
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                       id_room INTEGER PRIMARY KEY AUTOINCREMENT,
                       number_room INTEGER NOT NULL,
                       daily_rate REAL NOT NULL,
                       id_hotel_room INTEGER,
                       FOREIGN KEY (id_hotel_room) REFERENCES hoteis (id_hotel)
                       )
                       ''')
        
        connection.commit()

    except sqlite3.IntegrityError as e:
        print("-" * 30)
        print(" Integrity Error.", e)
        print("-" * 30)
        return
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: database error; check the SQL code.", e)
        print("-" * 30)
        return
    
    finally:
        # Só fecha se a conexão foi estabelecida de verdade
        if connection:
            connection.close()





def register_room():
    connection = None    # Inicializa a variável para evitar UnboundLocalError
    cursor = None

    try:
        connection, cursor = connection_db()
        
        print("\n ==== REGISTER HOTEL ====")
        print("-" * 30)
        name_hotel = input("What is the name of the hotel?: ")
        print("-" * 30)
        city_hotel = input("What is the name of the city where the hotel is located?: ")  # qual o nome da cidade que o hotel está localizado?
        print("-" * 30)

        print("\n ==== REGISTER ROOMS ====")
        print("-" * 30)
        number_room = int(input("What is the hotel room number?: "))
        print("-" * 30)
        daily_rate = float(input("What is the nightly rate for the room?: "))    # preco_diaria - qual o preço da diaria do quarto?
        print("-" * 30)
        id_hotel = int(input("What is the hotel room ID?: ")) # qual é o ID do hotel do quarto?

        cursor.execute("INSERT INTO hotels (hotel_name, hotel_city) VALUES (?, ?)", (name_hotel, city_hotel))
        cursor.execute("INSERT INTO rooms (number_room, daily_rate, id_hotel_room) VALUES (?, ?, ?)", (number_room, daily_rate, id_hotel))

        connection.commit()

        print("-" * 30)
        print("Information successfully added!")
        print("-" * 30)
    
    except ValueError as e:
        print("-" * 30)
        print("Error: enter valid information.", e)
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError as e:
        print("-" * 30)
        print(" Integrity Error.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operation cancelled by the user; program terminated.")
            print("-" * 30)
            return
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: database error; check the SQL code.", e)
        print("-" * 30)
        return
    
    finally:
        # Só fecha se a conexão foi estabelecida de verdade
        if connection:
            connection.close()






def see_room():
    connection = None    # Inicializa a variável para evitar UnboundLocalError
    cursor = None

    try:
        connection, cursor = connection_db()

        cursor.execute('''
                SELECT rooms.id_room, rooms.number_room, rooms.daily_rate, hotels.hotel_name, hotels.hotel_city 
                FROM rooms
                INNER JOIN hotels ON rooms.id_hotel_room = hotels.id_hotel
                ''')

        rooms = cursor.fetchall()

        print("\n ==== REGISTRATIONS ====")   # "data" = dados
        if not rooms:
            print("-" * 30)
            print("There are no rooms registered in the system.")
            print("-" * 30)
            return
        
        for room in rooms:
            room_id, number_room, daily_rate, hotel_name, hotel_city = room

            print(f"Room ID: {room_id} / hotel name: {hotel_name} / hotel city: {hotel_city}")
            print(f"number room: {number_room} / daily rate: ${daily_rate}")
            print("-" * 30)
            
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: database error; check the SQL code.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operation cancelled by the user; program terminated.")
            print("-" * 30)
            return
    
    finally:
        # Só fecha se a conexão foi estabelecida de verdade
        if connection:
            connection.close()





def update_room():
    connection = None    # Inicializa a variável para evitar UnboundLocalError
    cursor = None

    try:
        connection, cursor = connection_db()
        see_room()

        cursor.execute("SELECT * FROM rooms")
        data = cursor.fetchall()

        which_one_to_change = int(input("Which ID do you wish to change?: "))    #"which_one_to_change" = qual_mudar  -  qual ID deseja mudar?

        if not data:
            print("-" * 30)
            print("There is no record in the system.")  # não há nenhum cadastro no sistema.
            print("-" * 30)
            return

        print("\n ==== MENU DE ALTERAÇÃO ====")
        number_room = int(input("What is the hotel room number?: "))
        print("-" * 30)
        daily_rate = float(input("What is the nightly rate for the room?: "))    # preco_diaria - qual o preço da diaria do quarto?
        print("-" * 30)
        id_hotel = int(input("What is the hotel room ID?: ")) # qual é o ID do hotel do quarto?

        cursor.execute("UPDATE rooms SET number_room = ?, daily_rate = ?, id_hotel_room = ? WHERE id_room = ?", (number_room, daily_rate, id_hotel, which_one_to_change))

        connection.commit()

        print("-" * 30)
        print("Information successfully updated!")  # informações atualizadas com sucesso!
        print("-" * 30)

    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: database error; check the SQL code.", e)
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError as e:
        print("-" * 30)
        print(" Integrity Error.", e)
        print("-" * 30)
        return
        
    except ValueError as e:
        print("-" * 30)
        print("Error: enter valid information.", e)
        print("-" * 30)
        return
    
    except IndexError as e:
        print("-" * 30)
        print("ERROR: Attempt to access non-existent data in the table/column.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operation cancelled by the user; program terminated.")
            print("-" * 30)
            return
    
    finally:
        # Só fecha se a conexão foi estabelecida de verdade
        if connection:
            connection.close()





def delete_room():
    connection = None    # Inicializa a variável para evitar UnboundLocalError
    cursor = None

    try:
        connection, cursor = connection_db()

        see_room()

        cursor.execute("SELECT * FROM rooms")
        data = cursor.fetchall()

        if not data:
            print("-" * 30)
            print("There is no record in the system.")  # não há nenhum cadastro no sistema.
            print("-" * 30)
            return
        
        print("\n ==== DELETE ACCOUNT ==== ")
        which_one_to_change = int(input("Which ID do you want to delete?: "))
        print("-" * 30)

        cursor.execute("DELETE FROM rooms WHERE id_room = ?", (which_one_to_change, ))  # "which_one_to_change" = qual_mudar

        connection.commit()

        print("Record successfully deleted! ")
        print("-" * 30)
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: database error; check the SQL code.", e)
        print("-" * 30)
        return

    except ValueError as e:
        print("-" * 30)
        print("Error: enter valid information.", e)
        print("-" * 30)
        return
    
    except IndexError as e:
        print("-" * 30)
        print("ERROR: Attempt to access non-existent data in the table/column.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operation cancelled by the user; program terminated.")
            print("-" * 30)
            return
    
    finally:
        # Só fecha se a conexão foi estabelecida de verdade
        if connection:
            connection.close()




def menu():
    try:
        while True:
            print("\n ==== USER INTERACTION MENU ==== ")
            print("1. REGISTER ROOM")
            print("2. SEE ROOMS")
            print("3. UPDATE ROOM")
            print("4. DELETE ROOM")
            print("5. EXIT")

            print("-" * 30)
            option = int(input("Which option will you choose?: "))  # qual opção vai escolher?
            print("-" * 30)

            if option == 1: register_room()
            elif option == 2: see_room()
            elif option == 3: update_room()
            elif option == 4: delete_room()
            elif option == 5:
                print("-" * 30)
                print("closing program...")
                print("-" * 30)
                break
            else:
                print("-" * 30)
                print("Invalid option. Try again.")
                print("-" * 30)
                continue
        
    except ValueError as e:
        print("-" * 30)
        print("Error: enter valid information.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operation cancelled by the user; program terminated.")
            print("-" * 30)
            return
    


create_database()
menu()