import sqlite3

def create_bank():
    try:
        connection = sqlite3.connect('hotelaria.db')
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''CREATE TABLE IF NOT EXISTS hoteis (
                       id_hotel INTEGER PRIMARY KEY AUTOINCREMENT,
                       name_hotel TEXT,
                       city_hotel TEXT
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
        connection.close()

def sign_up():
    try:
        connection = sqlite3.connect('hotelaria.db')
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
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

        cursor.execute("INSERT INTO hoteis (name_hotel, city_hotel) VALUES (?, ?)", (name_hotel, city_hotel))
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
        connection.close()

def see():
    try:
        connection = sqlite3.connect('hotelaria.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM rooms")
        data = cursor.fetchall()

        print("\n ==== REGISTRATIONS ====")   # "data" = dados
        for room in data:
            print(room)
    
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
        connection.close()

def to_update():
    try:
        connection = sqlite3.connect('hotelaria.db')
        cursor = connection.cursor()

        see()

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
        connection.close()

def delete():
    try:
        connection = sqlite3.connect('hotelaria.db')
        cursor = connection.cursor()

        see()

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
        connection.close()

def menu():
    try:
        while True:
            print("\n ==== USER INTERACTION MENU ==== ")
            print("1. SIGN UP")
            print("2. SEE")
            print("3. TO UPDATE")
            print("4. DELETE")
            print("5. EXIT")

            print("-" * 30)
            option = int(input("Which option will you choose?: "))  # qual opção vai escolher?
            print("-" * 30)

            if option == 1: sign_up()
            elif option == 2: see()
            elif option == 3: to_update()
            elif option == 4: delete()
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

create_bank()
menu()