import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='ashmitiscool',auth_plugin='mysql_native_password',database='cinemax')
mycursor = mycon.cursor()
# mycursor.execute('')
# mycon.commit()
print('Hello')
var = input('Do you want to Add or Edit anything of the movies?\nEnter y or n')
if var == 'y':
    choice = input('Enter e to edit movie, a to add movie')
    if choice == 'a':
        mn = input('Enter movie name you want to add')
        mi = input('Enter movie image path you want to add')
        mdesc = input('Enter movie description you want to add')
        mdate = input('Enter movie date you want to add (In YYYY-MM-DD format)')
        try:
            mycursor.execute(f'insert into movies values(\"{mn}\",\"{mi}\",\"{mdesc}\",\"{mdate}\")')
        except:
            print('Error exporting to sql')
        mycon.commit()


    elif choice == 'e':
        movi = input('Which movie? (Enter movie name)')

        # Check if the movie exists in the table
        query = f"SELECT MovieName FROM movies WHERE MovieName = '{movi}'"
        mycursor.execute(query)
        result = mycursor.fetchone()

        if result is None:
            print('Movie not found in the database')
        else:
            wht = input('Enter mn to edit movie name\nEnter mi to edit movie image\nEnter mdesc to edit movie description\nEnter mdate to edit movie date')
            if wht == 'mn':
                new_movie_name = input('Enter the new movie name: (Type cancelxx to cancel edit)')
                if new_movie_name!='cancelxx':
                    query = f"UPDATE movies SET MovieName = '{new_movie_name}' WHERE MovieName = '{movi}'"
                    mycursor.execute(query)
                    mycon.commit()
                    print('Movie name updated successfully!')
                else:
                    print('Cancelled')

            elif wht == 'mi':
                new_image_path = input('Enter the new movie image path (Type cancelxx to cancel edit): ')
                if new_image_path != 'cancelxx':
                    query = f"UPDATE movies SET MovieImage = '{new_image_path}' WHERE MovieName = '{movi}'"
                    mycursor.execute(query)
                    mycon.commit()
                    print('Movie image path updated successfully!')
                else:
                    print('Cancelled')

            elif wht == 'mdesc':
                new_description = input('Enter the new movie description (Type cancelxx to cancel edit): ')
                if new_description != 'cancelxx':
                    query = f"UPDATE movies SET MovieDesc = '{new_description}' WHERE MovieName = '{movi}'"
                    mycursor.execute(query)
                    mycon.commit()
                    print('Movie description updated successfully!')
                else:
                    print('Cancelled')

            elif wht == 'mdate':
                new_date = input('Enter the new movie date (In YYYY-MM-DD format) (Type cancelxx to cancel edit): ')
                if new_date != 'cancelxx':
                    query = f"UPDATE movies SET MovieDate = '{new_date}' WHERE MovieName = '{movi}'"
                    mycursor.execute(query)
                    mycon.commit()
                    print('Movie date updated successfully!')
                else:
                    print('Cancelled')
            else:
                print('Wrong choice, Execute again')
