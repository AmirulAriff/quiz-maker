import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mcq_quiz_maker",

)
cursor = db.cursor()

userlogtype = 0
userID = 1
quizID = 1
Uname = ""


def mainMenu():
    print("==============================")
    print("       MCQ QUIZ PLATFORM")
    print("==============================")
    print("0. Create New Account")
    print("1. Login")
    print("X. Exit")
    print("==============================")
    choice = str(input("Create new account[0], Login[1] or Exit[X]: "))
    if choice == "0":
        return signUp()
    elif choice == "1":
        return signIn()
    elif choice == 'X' or choice == 'x':
        print("Thank you for using mcq quiz platform, have a nice day!")
        print("                              █████████")
        print("           ██████          ███▒▒▒▒▒▒▒▒███")
        print("          █▒▒▒▒▒▒█       ███▒▒▒▒▒▒▒▒▒▒▒▒▒███")
        print("           █▒▒▒▒▒▒█    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        print("            █▒▒▒▒▒█   ██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███")
        print("             █▒▒▒█   █▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██")
        print("           █████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        print("           █▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██")
        print("         ██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██")
        print("        ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██")
        print("        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██")
        print("        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        print("         █▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        print("         ██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
        print("          ████████████   █████████████████")
    else:
        print(input("Please enter the right input, press any key to continue..."))
        return mainMenu()


def signUp():
    global userID

    print("==============================")
    print("Create new account")
    username = str(input("Username: "))

    while len(username) < 6:
        print("Username must be more than 6 characters.")
        username = input("Username : ")
        if len(username) >= 6:
            break

    password = str(input("Password: "))
    while len(password) < 6:
        print("Password must be more than 6 characters.")
        password = input("Password : ")
        if len(password) >= 6:
            break

    # ConfirmationPassword
    password1 = str(input("Confirm Password: "))
    while len(password1) < 6:
        print("Confirm password must be more than 6 characters.")
        password1 = input("Confirm Password : ")
        if len(password1) >= 6:
            break

    # To check if the password and the confirm password is the same or not
    while password1 != password:
        print("Your confirmation password is different, please try again!")
        password = str(input("Password: "))
        while len(password) < 6:
            print("Password must be more than 6 characters.")
            password = input("Password : ")
            if len(password) >= 6:
                break
        password1 = str(input("Confirm Password: "))
        while len(password1) < 6:
            print("Confirm password must be more than 6 characters.")
            password1 = input("Confirm Password : ")
            if len(password1) >= 6:
                break
        if password1 == password:
            break

    # Usertype whether student or teacher
    userType = str(input("Usertype: Teacher [0] or Student [1]:"))
    if userType == "0":
        loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
        cursor.execute(loadname % (username, password, userType))
        # cursor.execute(query)
        checkdata = cursor.fetchall()
        if len(checkdata) > 0:
            print("==============================")
            print("The account is already existed!!")
            return signUp()
        else:

            query = "INSERT INTO user(username,password,type) VALUES (%s, %s, %s)"

            ## storing values in a variable
            values = (username, password, userType)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Account Sucessfully Created!")

            query2 = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
            cursor.execute(query2 % (username, password, userType))
            checkdata = cursor.fetchall()
            if len(checkdata) > 0:
                userID = checkdata[0][0]
                print(str(userID), ":", username)

            return website2()

    elif userType == "1":
        loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
        cursor.execute(loadname % (username, password, userType))
        # cursor.execute(query)
        checkdata = cursor.fetchall()
        if len(checkdata) > 0:
            print("==============================")
            print("The account is already existed!")
            return signUp()
        else:

            query = "INSERT INTO user(username,password, type) VALUES (%s, %s, %s)"

            ## storing values in a variable
            values = (username, password, userType)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Account Sucessfully Created!")

            query2 = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
            cursor.execute(query2 % (username, password, userType))
            checkdata = cursor.fetchall()
            if len(checkdata) > 0:
                userID = checkdata[0][0]
                print(str(userID), ":", username)

            return website()
    else:
        while userType != "0" or userType != "1":
            print("Wrong input!")
            userType = input("Usertype: Teacher [0] or Student [1]:")

            if userType == "0":
                loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
                cursor.execute(loadname % (username, password, userType))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    print("==============================")
                    print("The account is already existed!")
                    return signUp()
                else:

                    query = "INSERT INTO user(username,password, type) VALUES (%s, %s, %s)"

                    ## storing values in a variable
                    values = (username, password, userType)
                    ## executing the query with values
                    cursor.execute(query, values)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Account Sucessfully Created!")

                    query2 = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
                    cursor.execute(query2 % (username, password, userType))
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        userID = checkdata[0][0]
                        print(str(userID), ":", username)

                    return website2()

            if userType == "1":
                loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
                cursor.execute(loadname % (username, password, userType))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    print("==============================")
                    print("The account is already existed!")
                    return signUp()
                else:

                    query = "INSERT INTO user(username,password,type) VALUES (%s, %s, %s)"

                    ## storing values in a variable
                    values = (username, password, userType)
                    ## executing the query with values
                    cursor.execute(query, values)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Account Sucessfully Created!")

                    query2 = "SELECT * FROM user WHERE username = '%s' AND password = '%s' AND type = '%s'"
                    cursor.execute(query2 % (username, password, userType))
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        userID = checkdata[0][0]
                        print(str(userID, ":", username))

                    return website()


def signIn():
    global userID
    global Uname

    print("==============================")
    print("Login")
    username = str(input("Username: "))
    password = str(input("Password: "))

    submit = input("Are you sure you want to login?\n\
      (Y) for yes, (N) for no: ")
    if (submit == 'Y' or submit == 'y'):
        loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s'"
        cursor.execute(loadname % (username, password))
        # cursor.execute(query)
        checkdata = cursor.fetchall()
        if len(checkdata) > 0:
            print("==============================")
            print("Successfully Login!")

            userID = checkdata[0][0]
            Uname = checkdata[0][1]
            print("Username: ", Uname)
            # ni nak check die student ke teacher
            userlogtype = checkdata[0][3]
            if userlogtype == 1:
                return website()
            elif userlogtype == 0:
                return website2()
            # ni nak print je die student ke teacher
            print(userlogtype)
            return website()
        else:
            print("==============================")
            print(
                "The username/password you have entered is incorrect or the account does not exist. Please try again!")
            return signIn()

    elif (submit == 'N' or submit == 'n'):
        return mainMenu()
    else:
        while submit != 'Y' or submit != 'y' or submit == "N" or submit == "n":
            print("_______________________________")
            print("Please enter the correct key...")
            print("_______________________________")
            submit = input("Are you sure you want to login?\n\
            (Y) for yes, (N) for no: ")
            if submit == 'Y' or submit == 'y':
                loadname = "SELECT * FROM user WHERE username = '%s' AND password = '%s'"
                cursor.execute(loadname % (username, password))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    print("==============================")
                    print("Successfully Login!")

                    userID = checkdata[0][0]
                    Uname = checkdata[0][1]
                    print("Username: ", Uname)
                    # ni nak check die student ke teacher
                    userlogtype = checkdata[0][3]
                    if userlogtype == 1:
                        return website()
                    elif userlogtype == 0:
                        return website2()
                    # ni nak print je die student ke teacher
                    print(userlogtype)
                    return website()
                else:
                    print("==============================")
                    print("The username/password you have entered is incorrect. Please try again!")
                    return signIn()

            elif submit == 'N' or submit == 'n':
                return mainMenu()


def website():
    # studentWebsite
    global userID

    print("==============================")
    print("0. New Quizzes")
    print("1. Attempted Quizzes")
    print("2. Show all quz")
    print("X. Log Out")
    print("==============================")

    choice = str(input("Please input your choice: "))
    if choice == '0':
        return newQuiz()
    elif choice == '1':
        return attempQuiz()
    elif choice == '2':
        return answerQuiz()

    # DeleteAccount
    elif choice == '2':
        delete = input("Are you sure you want to delete your account?\n\
          (Y) for yes, (N) for no.")
        if delete == 'Y' or delete == 'y':

            db.autocommit = True
            delequery = "DELETE FROM user WHERE User_ID = " + str(userID) + ""
            db.commit()

            cursor.execute(delequery)
            db.commit()
            print("==============================")
            print("Account deleted!")
            return mainMenu()
        elif delete == 'N' or delete == 'n':
            return website()
        else:
            print("Please enter the correct key...")
            return website()

    # Logout
    elif choice == 'X' or choice == 'x':
        logout = input("Are you sure you want to log out?\n\
          (Y) for Yes, (N) for No: ")
        if logout == 'Y' or logout == 'y':
            return mainMenu()
        elif logout == 'N' or logout == 'n':
            return website()
        else:
            print("Please enter the correct key...")
            return website()
    else:
        print("Please enter the correct key...")
        return website()


def website2():
    # teacherWebsite
    global userID
    global Uname

    print("==============================")
    print("0. View All Quiz Created")
    print("1. Create New Quiz")
    print("2. Edit Quiz")
    print("3. Delete Quiz")
    print("4. Delete Account")
    print("X. Logout")
    print("==============================")

    choice = str(input("Please input your choice: "))
    if choice == '0':
        return viewallQuiz()
    elif choice == '1':
        return createQuiz()
    elif choice == '2':
        return editquizMenu()
    elif choice == '3':
        return deleteQuiz()

    # DeleteAccount
    elif choice == '4':
        delete = input("Are you sure you want to delete your account?\n\
          (Y) for yes, (N) for no:")
        if delete == 'Y' or delete == 'y':

            db.autocommit = True
            delequery = "DELETE FROM user WHERE User_ID = " + str(userID) + ""
            db.commit()

            cursor.execute(delequery)
            db.commit()
            print("==============================")
            print("Account deleted!")
            return mainMenu()
        elif delete == 'N' or delete == 'n':
            return website2()
        else:
            print("Please enter the correct key...")
            return website2()

    # Logout
    elif choice == 'X' or choice == 'x':
        logout = input("Are you sure you want to log out?\n\
          (Y) for Yes, (N) for No: ")
        if logout == 'Y' or logout == 'y':
            return mainMenu()
        elif logout == 'N' or logout == 'n':
            return website2()
        else:
            print("Please enter the correct key...")
            return website2()
    else:
        print("Please enter the correct key...")
        return website2()


def newQuiz():
    print("       NEW QUIZZES")
    print("==============================")
    print("Quiz 1")
    print("Quiz 2")
    print("Quiz 3")
    print("Quiz 4")
    print("==============================")

    response = input("\nPress any key to continue...\n")
    return website()


def attempQuiz():
    print("       ATTEMPTED QUIZZES")
    print("==============================")
    print("Quiz 1")
    print("Quiz 2")
    print("Quiz 3")
    print("Quiz 4")
    print("==============================")

    response = input("\nPress any key to continue...\n")
    return website()


def viewallQuiz():
    global userID
    global quizID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("         ALL QUIZZES")
    print("==============================")

    query = "SELECT quiz_name FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    print("Total numbers of quiz created: ")
    print(len(checkdata))
    print("------------------------------")
    if len(checkdata) > 0:
        query2 = "SELECT quiz_id FROM quiz WHERE User_ID = '" + str(userID) + "'"
        cursor.execute(query2)
        checkdata1 = cursor.fetchall()
        print("List of the quiz you created: ")
        print("Quiz ID/ Number: ", checkdata1)
        print("Quiz Name: ", checkdata)
        print("==============================")
        quiz_id = input("Type the (Quiz ID/ Number) from above if you wish to view the question: ")
        quiz_name = input("Type your (Quiz Name) as well for confirmation : ")
        confirm = input("Are you sure you want to view quiz ( " + quiz_name + " ) question? \n\
         Press (Y) to confirm (N) to cancel or press (B) to exit: ")

        if confirm == 'Y' or confirm == 'y':
            loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
            cursor.execute(loadquizname % (quiz_id))
            checkdata2 = cursor.fetchall()
            print("==============================")
            print(checkdata2[0][0])
            print("==============================")
            response = input("\nPress any key to continue...\n")
            return viewallQuiz()

        elif confirm == 'N' or confirm == 'n':
            return viewallQuiz()

        elif confirm == 'B' or confirm == 'b':
            return website2()

        else:
            while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n' or confirm == 'B' or confirm == 'b':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                confirm = input("Are you sure you want to view quiz ( " + quiz_name + " ) question? \n\
            Press (Y) to confirm (N) to cancel or press (B) to exit:")
                if confirm == 'Y' or confirm == 'y':
                    loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
                    cursor.execute(loadquizname % (quiz_id))
                    checkdata2 = cursor.fetchall()
                    print("==============================")
                    print(checkdata2[0][0])
                    print("==============================")
                    response = input("\nPress any key to continue...\n")
                    return viewallQuiz()

                elif confirm == 'N' or confirm == 'n':
                    return viewallQuiz()

                elif confirm == 'B' or confirm == 'b':
                    return website2()

    else:
        print("List of the quiz you created: ")
        print("None!")
        print("==============================")
        response = input("\nPress any key to continue...\n")
        return website2()


def createQuiz():
    global userID
    global quizID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("       CREATE QUIZZES")
    print("==============================")
    print("Examples: ")
    print("Please enter your name: Justin Bieber")
    print("Please enter your quiz name: Mathematics")
    print("Please enter your quiz topic: Trigonometry")
    print("==============================")

    # Quiz Creator, Quiz Name and Quiz Topic
    quiz_creator = input("Please enter your name: ")
    while len(quiz_creator) <= 1:
        print("------------------------------")
        print("The length of your name is less than 1 character,\n"
              "or you're pressing the incorrect input!")
        print("------------------------------")
        quiz_creator = input("Please enter your name: ")
        if len(quiz_creator) >= 1:
            break
    quiz_name = input("Please enter your quiz name: ")
    while len(quiz_name) <= 1:
        print("------------------------------")
        print("The length of your quiz name is less than 1 character,\n"
              "or you're pressing the incorrect input!")
        print("------------------------------")
        quiz_name = input("Please enter your quiz name: ")
        if len(quiz_name) >= 1:
            break
    quiz_topic = input("Please enter your quiz topic: ")
    while len(quiz_topic) <= 1:
        print("------------------------------")
        print("The length of your quiz topic is less than 1 character,\n"
              "or you're pressing the incorrect input!")
        print("------------------------------")
        quiz_topic = input("Please enter your quiz topic: ")
        if len(quiz_topic) >= 1:
            break

    # Save quiz name, creator and topic in the database
    option = input("Do you want to save the quiz (name, creator, topic)?\n\
                  Press (Y) to save, (N) to redo or (B) to exit: ")

    if option == 'Y' or option == 'y':
        loadname = "SELECT * FROM quiz WHERE quiz_name = '%s'"
        cursor.execute(loadname % (quiz_name))
        # cursor.execute(query)
        checkdata = cursor.fetchall()
        if len(checkdata) > 0:
            loadname = "SELECT quiz_creator FROM quiz WHERE quiz_name = '%s'"
            cursor.execute(loadname % (quiz_name))
            # cursor.execute(query)
            checkdata = cursor.fetchall()
            if checkdata[0][0] == quiz_creator:
                print("==============================")
                print("The quiz is already existed!")
                print("==============================")
                return createQuiz()

            else:
                query = "INSERT INTO quiz(User_ID,quiz_name,quiz_topic,quiz_creator) VALUES (%s, %s, %s, %s )"

                ## storing values in a variable
                values = (userID, quiz_name, quiz_topic, quiz_creator)
                ## executing the query with values
                cursor.execute(query, values)

                ## to make final output we have to run
                ## the 'commit()' method of the database object
                db.commit()
                db.autocommit = True

                print("==============================")
                print(cursor.rowcount, "Quiz Sucessfully Created!")

                ### Quiz ID
                query2 = "SELECT * FROM quiz WHERE quiz_name = '%s' AND quiz_topic = '%s' AND quiz_creator = '%s'"
                cursor.execute(query2 % (quiz_name, quiz_topic, quiz_creator))
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    quizID = checkdata[0][0]
                ###
                return createquizQuestion()

        else:
            query = "INSERT INTO quiz(User_ID,quiz_name,quiz_topic,quiz_creator) VALUES (%s, %s, %s, %s )"

            ## storing values in a variable
            values = (userID, quiz_name, quiz_topic, quiz_creator)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Quiz Sucessfully Created!")

            ## Quiz ID
            query2 = "SELECT * FROM quiz WHERE quiz_name = '%s' AND quiz_topic = '%s' AND quiz_creator = '%s'"
            cursor.execute(query2 % (quiz_name, quiz_topic, quiz_creator))
            checkdata = cursor.fetchall()
            if len(checkdata) > 0:
                quizID = checkdata[0][0]
            ##
            return createquizQuestion(quizID)

    elif option == 'N' or option == 'n':
        return createQuiz()
    elif option == 'B' or option == 'b':
        return website2()
    else:
        while option != 'Y' or option != 'y' or option != 'N' or option != 'n' or option != 'B' or option != 'b':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            option = input("Do you want to save the quiz (name, creator, topic)?\n\
                           Press (Y) to save, (N) to redo or (B) to exit: ")

            if option == 'Y' or option == 'y':
                loadname = "SELECT * FROM quiz WHERE quiz_name = '%s'"
                cursor.execute(loadname % (quiz_name))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    loadname = "SELECT quiz_creator FROM quiz WHERE quiz_name = '%s'"
                    cursor.execute(loadname % (quiz_name))
                    # cursor.execute(query)
                    checkdata = cursor.fetchall()
                    if checkdata[0][0] == quiz_creator:
                        print("==============================")
                        print("The quiz is already existed!")
                        print("==============================")
                        return createQuiz()

                    else:
                        query = "INSERT INTO quiz(User_ID,quiz_name,quiz_topic,quiz_creator) VALUES (%s, %s, %s, %s )"

                        ## storing values in a variable
                        values = (userID, quiz_name, quiz_topic, quiz_creator)
                        ## executing the query with values
                        cursor.execute(query, values)

                        ## to make final output we have to run
                        ## the 'commit()' method of the database object
                        db.commit()
                        db.autocommit = True

                        print("==============================")
                        print(cursor.rowcount, "Quiz Sucessfully Created!")

                        ### Quiz ID
                        query2 = "SELECT * FROM quiz WHERE quiz_name = '%s' AND quiz_topic = '%s' AND quiz_creator = '%s'"
                        cursor.execute(query2 % (quiz_name, quiz_topic, quiz_creator))
                        checkdata = cursor.fetchall()
                        if len(checkdata) > 0:
                            quizID = checkdata[0][0]
                        ###
                        return createquizQuestion(quizID)

                else:
                    query = "INSERT INTO quiz(User_ID,quiz_name,quiz_topic,quiz_creator) VALUES (%s, %s, %s, %s )"

                    ## storing values in a variable
                    values = (userID, quiz_name, quiz_topic, quiz_creator)
                    ## executing the query with values
                    cursor.execute(query, values)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Quiz Sucessfully Created!")

                    ## Quiz ID
                    query2 = "SELECT * FROM quiz WHERE quiz_name = '%s' AND quiz_topic = '%s' AND quiz_creator = '%s'"
                    cursor.execute(query2 % (quiz_name, quiz_topic, quiz_creator))
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        quizID = checkdata[0][0]
                    ##
                    return createquizQuestion(quizID)

            elif option == 'N' or option == 'n':
                return createQuiz()
            elif option == 'B' or option == 'b':
                return website2()


def createquizQuestion(quizID):
    global userID
    global Uname
    condition = ""

    done = "No"
    while done == "No":
        questionNumber = str(input("Please enter the question number: "))
        while len(questionNumber) < 0:
            print("------------------------------")
            print("The length of your question number is less than 1 character,\n"
                  "or you're pressing the incorrect input!")
            print("------------------------------")
            questionNumber = input("Please enter the question number: ")
            if len(questionNumber) >= 1:
                break

        choice = input("Are you sure you want to save the question number?\n\tPress (Y) to save, (N) to redo or (B) to exit.")

        if choice == 'Y' or choice == 'y':
            print(quizID)
            loadquiz = "SELECT number FROM question WHERE quiz_id = '%s' AND number = '%s'"
            cursor.execute(loadquiz % (quizID, questionNumber))
            # cursor.execute(query)
            checkdata = cursor.fetchall()
            if len(checkdata) > 0:
                print("==============================")
                print("The question number already existed! anjenk")

            else:
                query = "INSERT INTO question(User_ID,quiz_id,number) values (%s, %s, %s)"
                # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                ## storing values in a variable
                values = (userID, quizID, questionNumber)
                ## executing the query with values
                cursor.execute(query, values)

                ## to make final output we have to run
                ## the 'commit()' method of the database object
                db.commit()
                db.autocommit = True

                print("==============================")
                print("Question Number = ", questionNumber)
                print("==============================")

                # Quiz Structure
                print("------------------------------")
                print("        MATHEMATICSXDDDDDDDDD")
                print("------------------------------")
                print("Trigonometry")
                print("Question (1): What is 2 multiply with 4? ")
                print("A. 6")
                print("B. 2")
                print("C. 8")
                print("D. 16")
                print("------------------------------")
                print("==============================")
                print("Note: Above are examples of the structure in the quiz, you can design it differently too if you want ;).")
                print("==============================")
                print("Reminder: DO NOT! press 'ENTER' button if you want to go to the next rows, ")
                print("          Please finish what you are typing in the current row first, ")
                print("          Because once you press the 'ENTER' button, you can't edit back the previous rows!")
                print("Reminder 2: Only create one question at a time for example make a structure of 'Question 1' ")
                print("            Save it, and then continue with 'Question 2' save it and so on.")
                print("            Do not write 'Question 1' and 'Question 2' together and the save it. ")
                print("SAVE QUIZ: Press 'ENTER' button twice at the bottom of your quiz structure to save the quiz.")
                print("==============================")

                contents = []

                while True:
                    if condition == "1":
                        break
                    try:
                        line = input()
                    except EOFError:
                        break

                    if line == '':
                        save = str(input("Type 'save' to save quiz: "))
                        if save == "save":
                            break
                        else:
                            while save != "save":
                                print("Incorrect input, press enter again to save!")
                                save = str(input("Type 'save' to save quiz: "))
                                if save == "save":
                                    condition = "1"
                                    break

                    contents.append(line)

                choice = input("Are you sure you want to save the quiz question?\n\
                                         Press (Y) to save, (N) to redo or (B) to exit: ")

                if choice == 'Y' or choice == 'y':

                    quizquestion = (' \n '.join(map(str, contents)))
                    loadquiz = "SELECT Question FROM question WHERE Question = '%s'"
                    cursor.execute(loadquiz % (quizquestion))
                    # cursor.execute(query)
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        print("==============================")
                        print("The question is already existed!")

                    else:
                        query = "UPDATE question SET Question = '" + str(quizquestion) + "' WHERE number = '" + str(questionNumber) + "'"

                        ## executing the query with values
                        cursor.execute(query)

                        ## to make final output we have to run
                        ## the 'commit()' method of the database object
                        db.commit()
                        db.autocommit = True

                        print("==============================")
                        print(cursor.rowcount, "Quiz Content Sucessfully Created!")


                        done = input("are you done?: ")
                        if done == "yes":
                            print("setel beb")
                            break

        elif choice == 'N' or choice == 'n':
            return createquizQuestion(quizID)

        elif choice == 'B' or choice == 'b':
            return website2()

        else:
            while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n' or choice != 'B' or choice != 'b':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                choice = input("Are you sure you want to save the question number?\n\
                                     Press (Y) to save, (N) to redo or (B) to exit: ")
                if choice == 'Y' or choice == 'y':

                    loadquiz = "SELECT * FROM question WHERE number = '%s'"
                    cursor.execute(loadquiz % (questionNumber))
                    # cursor.execute(query)
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        print("==============================")
                        print("The question number already existed!")

                    else:
                        query = "INSERT INTO question(User_ID,quiz_id,number) values (%s, %s, %s)"
                        # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                        ## storing values in a variable
                        values = (userID, quizID, questionNumber)
                        ## executing the query with values
                        cursor.execute(query, values)

                        ## to make final output we have to run
                        ## the 'commit()' method of the database object
                        db.commit()
                        db.autocommit = True

                        print("==============================")
                        print("Question Number = ", questionNumber)
                        print("==============================")
                        response = input("\nPress any key to continue to the question...\n")

                elif choice == 'N' or choice == 'n':
                    return createquizQuestion(quizID)

                elif choice == 'B' or choice == 'b':
                    return website2()

    # Quiz Structure
    print("------------------------------")
    print("        MATHEMATICS")
    print("------------------------------")
    print("Trigonometry")
    print("Question (1): What is 2 multiply with 4? ")
    print("A. 6")
    print("B. 2")
    print("C. 8")
    print("D. 16")
    print("------------------------------")
    print("==============================")
    print("Note: Above are examples of the structure in the quiz, you can design it differently too if you want ;).")
    print("==============================")
    print("Reminder: DO NOT! press 'ENTER' button if you want to go to the next rows, ")
    print("          Please finish what you are typing in the current row first, ")
    print("          Because once you press the 'ENTER' button, you can't edit back the previous rows!")
    print("Reminder 2: Only create one question at a time for example make a structure of 'Question 1' ")
    print("            Save it, and then continue with 'Question 2' save it and so on.")
    print("            Do not write 'Question 1' and 'Question 2' together and the save it. ")
    print("SAVE QUIZ: Press 'ENTER' button twice at the bottom of your quiz structure to save the quiz.")
    print("==============================")

    contents = []

    while True:
        if condition == "1":
            break
        try:
            line = input()
        except EOFError:
            break

        if line == '':
            save = str(input("Type 'save' to save quiz: "))
            if save == "save":
                break
            else:
                while save != "save":
                    print("Incorrect input, press enter again to save!")
                    save = str(input("Type 'save' to save quiz: "))
                    if save == "save":
                        condition = "1"
                        break

        contents.append(line)

    choice = input("Are you sure you want to save the quiz question?\n\
                     Press (Y) to save, (N) to redo or (B) to exit: ")

    if choice == 'Y' or choice == 'y':

        quizquestion = (' \n '.join(map(str, contents)))
        loadquiz = "SELECT Question FROM question WHERE number = '%s'"
        cursor.execute(loadquiz % (quizquestion))
        # cursor.execute(query)
        checkdata = cursor.fetchall()
        if len(checkdata) > 0:
            print("==============================")
            print("The question is already existed!")

        else:
            query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
            # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

            ## storing values in a variable
            values = (userID, quizID, quizquestion, questionNumber)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Quiz Content Sucessfully Created!")

    elif choice == 'N' or choice == 'n':
        return createquizQuestion(quizID)

    elif choice == 'B' or choice == 'b':
        return website2()

    else:
        while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n' or choice != 'B' or choice != 'b':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            choice = input("Are you sure you want to save the question?\n\
                           Press (Y) to save, (N) to redo or (B) to exit: ")
            if choice == 'Y' or choice == 'y':

                quizquestion = (' \n '.join(map(str, contents)))
                loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                cursor.execute(loadquiz % (quizquestion))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    print("==============================")
                    print("The question is already existed!")

                else:
                    query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                    # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                    ## storing values in a variable
                    values = (userID, quizID, quizquestion, questionNumber)
                    ## executing the query with values
                    cursor.execute(query, values)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Quiz Content Sucessfully Created!")

            elif choice == 'N' or choice == 'n':
                return createquizQuestion(quizID)

            elif choice == 'B' or choice == 'b':
                return website2()

    # Question Answer (Instruction)
    print("==============================")
    print("QUIZ QUESTION ANSWER INSTRUCTION")
    print("==============================")
    print("Examples: ")
    print("Note: Choose from your answer option, no need to write down everything for examples: ")
    print("      Question 1: 4 + 1 = ?")
    print("      A. 1 ")
    print("      B. 2 ")
    print("      C. 3 ")
    print("      D. 5 ")
    print("==============================")
    print("Please enter the question answer: D")
    print("==============================")
    response = input("\nPress any key if you've read the instruction and wish to proceed...\n")

    # Question Answer
    print("==============================")
    print("  PICK QUIZ QUESTION ANSWER")
    print("==============================")
    loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
    cursor.execute(loadquizname % (quizID))
    checkdata2 = cursor.fetchall()
    print(checkdata2[0][0])
    print("==============================")

    questionAnswer = str(input("Please enter the question answer: "))
    while len(questionAnswer) < 0:
        print("------------------------------")
        print("The length of your question answer is less than 1 character,\n"
              "or you're pressing the incorrect input!")
        print("------------------------------")
        questionAnswer = input("Please enter the question answer: ")
        if len(questionAnswer) >= 1:
            break

    choice = input("Are you sure you want to save the question answer?\n\
                                       Press (Y) to save, (N) to redo or (B) to exit: ")

    if choice == 'Y' or choice == 'y':
        query = "UPDATE question SET Answer = '" + str(questionAnswer) + "' WHERE quiz_id = '" + str(quizID) + "'"
        # query = "UPDATE question(User_ID,quiz_id,Question,number,Answer) values (%s, %s, %s, %s,%s)"
        # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

        ## executing the query
        cursor.execute(query)

        ## to make final output we have to run
        ## the 'commit()' method of the database object
        db.commit()
        db.autocommit = True

        print("==============================")
        print("Question Answer = ", questionAnswer)
        print("==============================")
        response = input("\nPress any key to continue...\n")
        return website2()

    elif choice == 'N' or choice == 'n':
        return createquizQuestion(quizID)

    elif choice == 'B' or choice == 'b':
        return website2()

    else:
        while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n' or choice != 'B' or choice != 'b':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            choice = input("Are you sure you want to save the question answer?\n\
                                          Press (Y) to save, (N) to redo or (B) to exit: ")
            if choice == 'Y' or choice == 'y':
                query = "UPDATE question SET Answer = '" + str(questionAnswer) + "' WHERE quiz_id = '" + str(
                    quizID) + "'"
                # query = "UPDATE question(User_ID,quiz_id,Question,number,Answer) values (%s, %s, %s, %s, %s)"
                # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                ## executing the query
                cursor.execute(query)

                ## to make final output we have to run
                ## the 'commit()' method of the database object
                db.commit()
                db.autocommit = True

                print("==============================")
                print("Question Answer = ", questionAnswer)
                print("==============================")
                response = input("\nPress any key to continue...\n")

            elif choice == 'N' or choice == 'n':
                return createquizQuestion(quizID)

            elif choice == 'B' or choice == 'b':
                return website2()


def deleteQuiz():
    global userID
    global quizID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("       DELETE QUIZZES")
    print("==============================")

    query = "SELECT quiz_name FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    if len(checkdata) > 0:
        query2 = "SELECT quiz_id FROM quiz WHERE User_ID = '" + str(userID) + "'"
        cursor.execute(query2)
        checkdata1 = cursor.fetchall()
        print("List of the quiz you created: ")
        print("Quiz ID/ Number: ", checkdata1)
        print("Quiz Name: ", checkdata)
        print("==============================")

    else:
        print("List of the quiz you created: ")
        print("None!")
        print("==============================")
        leave = input("Press any key to continue...")
        return website2()

    quiz_id = input("Type the (Quiz ID/ Number) from above if you wish to delete the quiz: ")
    quiz_name = input("Type your (Quiz Name) from above for confirmation: ")
    confirm = input("Are you sure you want to delete quiz ( " + quiz_name + " ) ? \n\
         Press (Y) to confirm (N) to cancel:")

    if confirm == 'Y' or confirm == 'y':
        loadquizname = "SELECT quiz_name FROM quiz WHERE quiz_name = '%s'"
        cursor.execute(loadquizname % (quiz_name))
        checkdata = cursor.fetchall()
        loadquizname1 = "SELECT quiz_id FROM question WHERE quiz_id = '%s'"
        cursor.execute(loadquizname1 % (quiz_id))
        checkdata2 = cursor.fetchall()
        if checkdata[0][0] == quiz_name and str(checkdata2[0][0]) == str(quiz_id):
            query = "DELETE FROM quiz WHERE quiz_name = '%s' AND User_ID = '%s'"
            query2 = "DELETE FROM question WHERE quiz_id = '%s'"
            ## storing values in a variable
            # values = (quiz_name, userID)
            ## executing the query with values
            # cursor.execute(query, values)
            cursor.execute(query % (quiz_name, userID))
            cursor.execute(query2 % (quiz_id))
            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Quiz Sucessfully Deleted!")
            return website2()

    elif confirm == 'N' or confirm == 'n':
        return website2()

    else:
        while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            confirm = input("Are you sure you want to delete quiz ( " + quiz_name + " ) ? \n\
            Press (Y) to confirm (N) to cancel:")
            if confirm == 'Y' or confirm == 'y':
                loadquizname = "SELECT quiz_name FROM quiz WHERE quiz_name = '%s'"
                cursor.execute(loadquizname % (quiz_name))
                checkdata = cursor.fetchall()

                loadquizname1 = "SELECT Question FROM question WHERE quiz_id = '%s'"
                cursor.execute(loadquizname1 % (quiz_id))
                checkdata2 = cursor.fetchall()

                if checkdata[0][0] == quiz_name and str(checkdata2[0][0]) == str(quiz_id):
                    query = "DELETE FROM quiz WHERE quiz_name = '%s' AND User_ID = '%s'"
                    query2 = "DELETE FROM question WHERE quiz_id = '%s' AND User_ID = '%s'"
                    ## storing values in a variable
                    # values = (quiz_name, userID)
                    ## executing the query with values
                    # cursor.execute(query, values)
                    cursor.execute(query % (quiz_name, userID))
                    cursor.execute(query2 % (quiz_id, userID))
                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Quiz Sucessfully Deleted!")
                    return website2()
            elif confirm == 'N' or confirm == 'n':
                return website2()


def editquizMenu():
    global userID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("         EDIT QUIZZES")
    print("==============================")
    print("0. Edit Quiz Name")
    print("1. Edit Quiz Topic")
    print("2. Add New Question")
    print("3. Edit Question")
    print("4. Delete Question")
    print("X. Exit")
    print("==============================")

    choice = str(input("Please input your choice: "))
    if choice == '0':
        return editquizName()
    elif choice == '1':
        return editquizTopic()
    elif choice == '2':
        return addQuestion()
    elif choice == '3':
        return editQuestion()
    elif choice == '4':
        return deleteQuestion()

    elif choice == 'X' or choice == 'x':
        exit = input("Are you sure you want to exit?\n\
          (Y) for Yes, (N) for No: ")
        if exit == 'Y' or exit == 'y':
            return website2()
        elif exit == 'N' or exit == 'n':
            return editquizMenu()
        else:
            print("Please enter the correct key...")
            return editquizMenu()
    else:
        print("Please enter the correct key...")
        return editquizMenu()


def addQuestion():
    global userID
    global Uname
    global quizID

    condition = ""

    print("Username: ", Uname)
    print("==============================")
    print("         ADD QUESTION")
    print("==============================")


    # Confirmation
    query = "SELECT quiz_name FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    print("Total numbers of quiz created: ")
    print(len(checkdata))
    print("------------------------------")
    if len(checkdata) > 0:
        query2 = "SELECT quiz_id FROM quiz WHERE User_ID = '" + str(userID) + "'"
        cursor.execute(query2)
        checkdata1 = cursor.fetchall()
        print("List of the quiz you created: ")
        print("Quiz ID/ Number: ", checkdata1)
        print("Quiz Name: ", checkdata)
        print("==============================")
        quizID = input("Type the (Quiz ID/ Number) from above if you wish to add new question: ")
        quiz_name = input("Type your (Quiz Name) as well for confirmation : ")
        confirm = input("Are you sure you want to add new question in quiz ( " + quiz_name + " )? \n\
            Press (Y) to confirm, (N) to cancel: ")

        if confirm == 'Y' or confirm == 'y':
            loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
            cursor.execute(loadquizname % (quizID))
            checkdata2 = cursor.fetchall()
            print("List of question in the quiz: ")
            print("==============================")
            print(checkdata2[0][0])
            print("==============================")

            done = "No"

            while done == "No":
                # Add question function
                questionNumber = str(input("Please enter the new question number: "))
                while len(questionNumber) < 0:
                    print("------------------------------")
                    print("The length of your question number is less than 1 character,\n"
                          "or you're pressing the incorrect input!")
                    print("------------------------------")
                    questionNumber = input("Please enter the new question number: ")
                    if len(questionNumber) >= 1:
                        break

                loadquiz = "SELECT * FROM question WHERE number = '%s'"
                cursor.execute(loadquiz % (questionNumber))
                # cursor.execute(query)
                checkdata = cursor.fetchall()
                if len(checkdata) > 0:
                    print("==============================")
                    print("The question number already existed!")
                    return addQuestion()

                else:
                    query = "INSERT INTO question(User_ID,quiz_id,number) values (%s, %s, %s)"
                    # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                    ## storing values in a variable
                    values = (userID, quizID, questionNumber)
                    ## executing the query with values
                    cursor.execute(query, values)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print("Question Number = ", questionNumber)
                    print("==============================")
                    print("==============================")
                    print("Enter the new question structure down below hahahaxdd.")
                    print("==============================")
                    contents = []

                    while True:
                        if condition == "1":
                            break
                        try:
                            line = input()
                        except EOFError:
                            break

                        if line == '':
                            save = str(input("Type 'save' to save quiz: "))
                            if save == "save":
                                break
                            else:
                                while save != "save":
                                    print("Incorrect input, press enter again to save!")
                                    save = str(input("Type 'save' to save quiz: "))
                                    if save == "save":
                                        condition = "1"
                                        break

                        contents.append(line)

                    choice = input("Are you sure you want to save the quiz question?\n\Press (Y) to save, (N) to cancel: ")

                    if choice == 'Y' or choice == 'y':

                        quizquestion = (' \n '.join(map(str, contents)))
                        loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                        cursor.execute(loadquiz % (quizquestion))
                        # cursor.execute(query)
                        checkdata = cursor.fetchall()
                        if len(checkdata) > 0:
                            print("==============================")
                            print("The question is already existed!")

                        else:
                            query = "UPDATE question SET Question = '" + str(quizquestion) + "' WHERE number = '" + str(
                                questionNumber) + "'"

                            ## executing the query with values
                            cursor.execute(query)

                            ## to make final output we have to run
                            ## the 'commit()' method of the database object
                            db.commit()
                            db.autocommit = True

                            print("==============================")
                            print(cursor.rowcount, "Quiz Content Sucessfully Created!")

                            # Question Answer
                            print("==============================")
                            print("  PICK QUIZ QUESTION ANSWER")
                            print("==============================")
                            loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
                            cursor.execute(loadquizname % (quizID))
                            checkdata2 = cursor.fetchall()
                            print(checkdata2[0][0])
                            print("==============================")

                            questionAnswer = str(input("Please enter the new question answer: "))
                            while len(questionAnswer) < 0:
                                print("------------------------------")
                                print("The length of your question answer is less than 1 character,\n"
                                      "or you're pressing the incorrect input!")
                                print("------------------------------")
                                questionAnswer = input("Please enter new the question answer: ")
                                if len(questionAnswer) >= 1:
                                    break

                            choice = input("Are you sure you want to save the new question answer?\n\Press (Y) to save, (N) to cancel: ")

                            if choice == 'Y' or choice == 'y':
                                query = "UPDATE question SET Answer = '" + str(questionAnswer) + "' WHERE number = '" + str(questionNumber) + "'"
                                # query = "UPDATE question(User_ID,quiz_id,Question,number,Answer) values (%s, %s, %s, %s,%s)"
                                # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                                ## executing the query
                                cursor.execute(query)

                                ## to make final output we have to run
                                ## the 'commit()' method of the database object
                                db.commit()
                                db.autocommit = True

                                print("==============================")
                                print("Question Answer = ", questionAnswer)
                                print("==============================")
                                print("New question successfully added!")
                                print("==============================")

                            done = input("are you done?: ")
                            if done == "Yes":
                                print("siap")
                                break

        elif confirm == 'N' or confirm == 'n':
            return editquizMenu()

        else:
            while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                confirm = input("Are you sure you want to add new question in quiz ( " + quiz_name + " )? \n\
               Press (Y) to confirm, (N) to cancel:")
                if confirm == 'Y' or confirm == 'y':
                    loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
                    cursor.execute(loadquizname % (quizID))
                    checkdata2 = cursor.fetchall()
                    print("List of question in the quiz: ")
                    print("==============================")
                    print(checkdata2[0][0])
                    print("==============================")

                    # Add question function
                    questionNumber = str(input("Please enter the new question number: "))
                    while len(questionNumber) < 0:
                        print("------------------------------")
                        print("The length of your question number is less than 1 character,\n"
                              "or you're pressing the incorrect input!")
                        print("------------------------------")
                        questionNumber = input("Please enter the new question number: ")
                        if len(questionNumber) >= 1:
                            break

                    loadquiz = "SELECT * FROM question WHERE number = '%s'"
                    cursor.execute(loadquiz % (questionNumber))
                    # cursor.execute(query)
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        print("==============================")
                        print("The question number already existed!")
                        return addQuestion()

                    else:
                        query = "INSERT INTO question(User_ID,quiz_id,number) values (%s, %s, %s)"
                        # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                        ## storing values in a variable
                        values = (userID, quizID, questionNumber)
                        ## executing the query with values
                        cursor.execute(query, values)

                        ## to make final output we have to run
                        ## the 'commit()' method of the database object
                        db.commit()
                        db.autocommit = True

                        print("==============================")
                        print("Question Number = ", questionNumber)
                        print("==============================")
                        response = input("\nPress any key to continue to the question...\n")

                elif confirm == 'N' or confirm == 'n':
                    return editquizMenu()

        # Question Structure
        print("==============================")
        print("Enter the new question structure down below.")
        print("==============================")
        contents = []

        while True:
            if condition == "1":
                break
            try:
                line = input()
            except EOFError:
                break

            if line == '':
                save = str(input("Type 'save' to save quiz: "))
                if save == "save":
                    break
                else:
                    while save != "save":
                        print("Incorrect input, press enter again to save!")
                        save = str(input("Type 'save' to save quiz: "))
                        if save == "save":
                            condition = "1"
                            break

            contents.append(line)

        choice = input("Are you sure you want to save the quiz question?\n\
                                       Press (Y) to save, (N) to cancel: ")

        if choice == 'Y' or choice == 'y':

            quizquestion = (' \n '.join(map(str, contents)))
            loadquiz = "SELECT Question FROM question WHERE number = '%s'"
            cursor.execute(loadquiz % (quizquestion))
            # cursor.execute(query)
            checkdata = cursor.fetchall()
            if len(checkdata) > 0:
                print("==============================")
                print("The question is already existed!")

            else:
                query = "UPDATE question SET Question = '" + str(quizquestion) + "' WHERE number = '" + str(
                    questionNumber) + "'"
                # query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                ## executing the query with values
                cursor.execute(query)

                ## to make final output we have to run
                ## the 'commit()' method of the database object
                db.commit()
                db.autocommit = True

                print("==============================")
                print(cursor.rowcount, "Quiz Content Sucessfully Created!")

        elif choice == 'N' or choice == 'n':
            return editquizMenu()

        else:
            while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                choice = input("Are you sure you want to save the question?\n\
                                             Press (Y) to save, (N) to redo or (B) to exit: ")
                if choice == 'Y' or choice == 'y':

                    quizquestion = (' \n '.join(map(str, contents)))
                    loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                    cursor.execute(loadquiz % (quizquestion))
                    # cursor.execute(query)
                    checkdata = cursor.fetchall()
                    if len(checkdata) > 0:
                        print("==============================")
                        print("The question is already existed!")

                    else:
                        query = "UPDATE question SET Question = '" + str(quizquestion) + "' WHERE number = '" + str(
                            questionNumber) + "'"
                        # query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                        # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                        ## executing the query with values
                        cursor.execute(query)

                        ## to make final output we have to run
                        ## the 'commit()' method of the database object
                        db.commit()
                        db.autocommit = True

                        print("==============================")
                        print(cursor.rowcount, "Quiz Content Sucessfully Created!")

                elif choice == 'N' or choice == 'n':
                    return editquizMenu()

        # Question Answer
        print("==============================")
        print("  PICK QUIZ QUESTION ANSWER")
        print("==============================")
        loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
        cursor.execute(loadquizname % (quizID))
        checkdata2 = cursor.fetchall()
        print(checkdata2[0][0])
        print("==============================")

        questionAnswer = str(input("Please enter the new question answer: "))
        while len(questionAnswer) < 0:
            print("------------------------------")
            print("The length of your question answer is less than 1 character,\n"
                  "or you're pressing the incorrect input!")
            print("------------------------------")
            questionAnswer = input("Please enter new the question answer: ")
            if len(questionAnswer) >= 1:
                break

        choice = input("Are you sure you want to save the new question answer?\n\
                                          Press (Y) to save, (N) to cancel: ")

        if choice == 'Y' or choice == 'y':
            query = "UPDATE question SET Answer = '" + str(questionAnswer) + "' WHERE number = '" + str(
                questionNumber) + "'"
            # query = "UPDATE question(User_ID,quiz_id,Question,number,Answer) values (%s, %s, %s, %s,%s)"
            # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

            ## executing the query
            cursor.execute(query)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print("Question Answer = ", questionAnswer)
            print("==============================")
            print("New question successfully added!")
            print("==============================")
            response = input("\nPress any key to continue...\n")
            return editquizMenu()

        elif choice == 'N' or choice == 'n':
            return editquizMenu()

        else:
            while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                choice = input("Are you sure you want to save the new question answer?\n\
                                             Press (Y) to save, (N) to cancel: ")
                if choice == 'Y' or choice == 'y':
                    query = "UPDATE question SET Answer = '" + str(questionAnswer) + "' WHERE number = '" + str(
                        questionNumber) + "'"
                    # query = "UPDATE question(User_ID,quiz_id,Question,number,Answer) values (%s, %s, %s, %s, %s)"
                    # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                    ## executing the query
                    cursor.execute(query)

                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print("Question Answer = ", questionAnswer)
                    print("==============================")
                    print("New question successfully added!")
                    print("==============================")
                    response = input("\nPress any key to continue...\n")
                    return editquizMenu()

                elif choice == 'N' or choice == 'n':
                    return editquizMenu()

    else:
        print("List of the quiz you created: ")
        print("None!")
        print("==============================")
        response = input("\nPress any key to continue...\n")
        return editquizMenu()


def editQuestion():
    global userID
    global quizID
    global Uname
    condition = ""
    print("Username: ", Uname)
    print("==============================")
    print("         EDIT QUESTIONS")
    print("==============================")

    query = "SELECT quiz_name FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    if len(checkdata) > 0:
        query2 = "SELECT quiz_id FROM quiz WHERE User_ID = '" + str(userID) + "'"
        cursor.execute(query2)
        checkdata1 = cursor.fetchall()
        print("List of the quiz you created: ")
        print("Quiz ID/ Number: ", checkdata1)
        print("Quiz Name: ", checkdata)
        print("==============================")
        quizID = input("Type the (Quiz ID/ Number) from above if you wish view the question: ")
        choosequizname = input("Please type the quiz name to view the question:  ")
        confirm = input("Are you sure you want to view your quiz ( " + str(choosequizname) + " ) question?\n\
                           Press (Y) to confirm (N) to cancel:")

        if confirm == 'Y' or confirm == 'y':
            loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
            cursor.execute(loadquizname % (quizID))
            checkdata2 = cursor.fetchall()
            print("==============================")
            apani = (' \n '.join(map(str, checkdata2)))
            print(apani)
            print("==============================")

            number = input("Please type in the question number to be edit: ")
            confirmation = input("Are you sure you want to edit question" + "(" + number + ") ?\n\
                                   Press (Y) to confirm (N) to cancel:")
            if confirmation == 'Y' or confirmation == 'y':
                loadquizname = "SELECT number FROM question WHERE number = '%s'"
                cursor.execute(loadquizname % (number))
                checkdata = cursor.fetchall()

                if checkdata[0][0] == int(number):
                    print("==============================")
                    print(checkdata2[0][0])
                    print("==============================")
                    print("Enter the new question structure down below.")
                    print("==============================")
                    contents = []

                    while True:
                        if condition == "1":
                            break
                        try:
                            line = input()
                        except EOFError:
                            break

                        if line == '':
                            save = str(input("Type 'save' to save quiz: "))
                            if save == "save":
                                break
                            else:
                                while save != "save":
                                    print("Incorrect input, press enter again to save!")
                                    save = str(input("Type 'save' to save quiz: "))
                                    if save == "save":
                                        condition = "1"
                                        break

                        contents.append(line)

                    choice = input("Are you sure you want to save the edited question?\n\
                                                      Press (Y) to save, (N) to cancel: ")

                    if choice == 'Y' or choice == 'y':

                        quizquestion = (' \n '.join(map(str, contents)))
                        loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                        cursor.execute(loadquiz % (quizquestion))
                        # cursor.execute(query)
                        checkdata = cursor.fetchall()
                        if len(checkdata) > 0:
                            print("==============================")
                            print("The question is already existed!")

                        else:
                            query = "UPDATE question SET Question = '" + str(quizquestion) + "' WHERE number = '" + str(
                                number) + "'"
                            # query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                            # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                            ## executing the query with values
                            cursor.execute(query)

                            ## to make final output we have to run
                            ## the 'commit()' method of the database object
                            db.commit()
                            db.autocommit = True

                            print("==============================")
                            print("Question (" + number + ") Sucessfully Edited!")
                            response = input("\nPress any key to continue...\n")
                            return editquizMenu()

            elif confirm == 'N' or confirm == 'n':
                return editquizMenu()

            else:
                while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
                    print("==============================")
                    print("Incorrect input! Please try again..")
                    print("==============================")
                    confirmation = input("Are you sure you want to edit question" + "(" + number + ") ?\n\
                                                        Press (Y) to confirm (N) to cancel:")
                    if confirmation == 'Y' or confirmation == 'y':
                        loadquizname = "SELECT Question FROM question WHERE number = '%s'"
                        cursor.execute(loadquizname % (number))
                        checkdata = cursor.fetchall()

                        if checkdata[0][0] == number:
                            print("==============================")
                            print(checkdata2[0][0])
                            print("==============================")
                            print("Enter the new question structure down below.")
                            print("==============================")
                            contents = []

                            while True:
                                if condition == "1":
                                    break
                                try:
                                    line = input()
                                except EOFError:
                                    break

                                if line == '':
                                    save = str(input("Type 'save' to save quiz: "))
                                    if save == "save":
                                        break
                                    else:
                                        while save != "save":
                                            print("Incorrect input, press enter again to save!")
                                            save = str(input("Type 'save' to save quiz: "))
                                            if save == "save":
                                                condition = "1"
                                                break

                                contents.append(line)

                            choice = input("Are you sure you want to save the edited question?\n\
                                                                           Press (Y) to save, (N) to cancel: ")

                            if choice == 'Y' or choice == 'y':

                                quizquestion = (' \n '.join(map(str, contents)))
                                loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                                cursor.execute(loadquiz % (quizquestion))
                                # cursor.execute(query)
                                checkdata = cursor.fetchall()
                                if len(checkdata) > 0:
                                    print("==============================")
                                    print("The question is already existed!")

                                else:
                                    query = "UPDATE question SET Question = '" + str(
                                        quizquestion) + "' WHERE number = '" + str(
                                        number) + "'"
                                    # query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                                    # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                                    ## executing the query with values
                                    cursor.execute(query)

                                    ## to make final output we have to run
                                    ## the 'commit()' method of the database object
                                    db.commit()
                                    db.autocommit = True

                                    print("==============================")
                                    print("Question (" + number + ") Sucessfully Edited!")
                                    response = input("\nPress any key to continue...\n")
                                    return editquizMenu()

                    elif confirm == 'N' or confirm == 'n':
                        return editquizMenu()

        elif confirm == 'N' or confirm == 'n':
            return editquizMenu()

        else:
            while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
                print("==============================")
                print("Incorrect input! Please try again..")
                print("==============================")
                confirm = input("Are you sure you want to view your quiz ( " + str(choosequizname) + " ) question?\n\
                                       Press (Y) to confirm (N) to cancel:")

                if confirm == 'Y' or confirm == 'y':
                    loadquizname = "SELECT Question FROM question WHERE quiz_id = '%s'"
                    cursor.execute(loadquizname % (quizID))
                    checkdata2 = cursor.fetchall()
                    print("==============================")
                    print(checkdata2[0][0])
                    print("==============================")

                    number = input("Please type in the question number to be edit: ")
                    confirmation = input("Are you sure you want to edit question" + "(" + number + ") ?\n\
                                         Press (Y) to confirm (N) to cancel:")
                    if confirmation == 'Y' or confirmation == 'y':
                        loadquizname = "SELECT Question FROM question WHERE number = '%s'"
                        cursor.execute(loadquizname % (number))
                        checkdata = cursor.fetchall()
                        print(str(checkdata))

                        if checkdata[0][0] == number:
                            print("==============================")
                            print(checkdata2[0][0])
                            print("==============================")
                            print("Enter the new question structure down below.")
                            print("==============================")
                            contents = []

                            while True:
                                if condition == "1":
                                    break
                                try:
                                    line = input()
                                except EOFError:
                                    break

                                if line == '':
                                    save = str(input("Type 'save' to save quiz: "))
                                    if save == "save":
                                        break
                                    else:
                                        while save != "save":
                                            print("Incorrect input, press enter again to save!")
                                            save = str(input("Type 'save' to save quiz: "))
                                            if save == "save":
                                                condition = "1"
                                                break

                                contents.append(line)

                            choice = input("Are you sure you want to save the edited question?\n\
                                                            Press (Y) to save, (N) to cancel: ")

                            if choice == 'Y' or choice == 'y':

                                quizquestion = (' \n '.join(map(str, contents)))
                                loadquiz = "SELECT Question FROM question WHERE number = '%s'"
                                cursor.execute(loadquiz % (quizquestion))
                                # cursor.execute(query)
                                checkdata = cursor.fetchall()
                                if len(checkdata) > 0:
                                    print("==============================")
                                    print("The question is already existed!")

                                else:
                                    query = "UPDATE question SET Question = '" + str(
                                        quizquestion) + "' WHERE number = '" + str(
                                        number) + "'"
                                    # query = "INSERT INTO question(User_ID,quiz_id,Question, number) values (%s, %s, %s, %s)"
                                    # query = "INSERT INTO question SET Question = '" + quizquestion + "' WHERE quiz_id = '" + loadquiz + "'"

                                    ## executing the query with values
                                    cursor.execute(query)

                                    ## to make final output we have to run
                                    ## the 'commit()' method of the database object
                                    db.commit()
                                    db.autocommit = True

                                    print("==============================")
                                    print("Question (" + number + ") Sucessfully Edited!")
                                    response = input("\nPress any key to continue...\n")
                                    return editquizMenu()

                elif confirm == 'N' or confirm == 'n':
                    return editquizMenu()


def deleteQuestion():
    global userID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("         DELETE QUESTIONS")
    print("==============================")
    print("Question Deleted!")

    response = input("\nPress any key to continue...\n")
    return editquizMenu()


def editquizName():
    global userID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("         EDIT QUIZ NAME")
    print("==============================")

    query = "SELECT quiz_name FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    if len(checkdata) > 0:
        print("List of the quiz you created: ")
        print(str(checkdata))
        print("==============================")

    choosequizname = input("Please type the quiz name to be change:  ")
    newquizname = input("Please type your new quiz name: ")
    confirm = input("Are you sure you want to change your quiz name ( " + str(choosequizname) + " ) ? \n\
                  Press (Y) to confirm (N) to cancel:")

    if confirm == 'Y' or confirm == 'y':
        loadquizname = "SELECT quiz_name FROM quiz WHERE quiz_name = '%s'"
        cursor.execute(loadquizname % (choosequizname))
        checkdata = cursor.fetchall()

        if checkdata[0][0] == choosequizname:
            query = "UPDATE quiz SET quiz_name = '" + str(newquizname) + "' WHERE User_ID = '" + str(userID) + "'"

            ## storing values in a variable
            # values = (quiz_name, userID)
            ## executing the query with values
            # cursor.execute(query, values)
            cursor.execute(query)
            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Quiz Name Sucessfully Edited!")
            print("==============================")
            return editquizMenu()

    elif confirm == 'N' or confirm == 'n':
        return editquizMenu()

    else:
        while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            confirm = input("Are you sure you want to change your quiz name ( " + str(choosequizname) + " ) ? \n\
                           Press (Y) to confirm (N) to cancel:")

            if confirm == 'Y' or confirm == 'y':
                loadquizname = "SELECT quiz_name FROM quiz WHERE quiz_name = '%s'"
                cursor.execute(loadquizname % (choosequizname))
                checkdata = cursor.fetchall()

                if checkdata[0][0] == choosequizname:
                    query = "UPDATE quiz SET quiz_name = '" + str(newquizname) + "' WHERE User_ID = '" + str(
                        userID) + "'"

                    ## storing values in a variable
                    # values = (quiz_name, userID)
                    ## executing the query with values
                    # cursor.execute(query, values)
                    cursor.execute(query)
                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Quiz Name Sucessfully Edited!")
                    print("==============================")
                    return editquizMenu()

            elif confirm == 'N' or confirm == 'n':
                return editquizMenu()


def editquizTopic():
    global userID
    global Uname
    print("Username: ", Uname)
    print("==============================")
    print("         EDIT QUIZ TOPIC")
    print("==============================")

    query = "SELECT quiz_topic FROM quiz WHERE User_ID = '" + str(userID) + "'"
    cursor.execute(query)
    checkdata = cursor.fetchall()
    if len(checkdata) > 0:
        print("List of the quiz you created: ")
        print(str(checkdata))
        print("==============================")

    choosequiztopic = input("Please type the quiz topic to be change:  ")
    newquiztopic = input("Please type your new quiz topic: ")
    confirm = input("Are you sure you want to change your quiz topic ( " + str(choosequiztopic) + " ) ? \n\
                     Press (Y) to confirm (N) to cancel:")

    if confirm == 'Y' or confirm == 'y':
        loadquizname = "SELECT quiz_topic FROM quiz WHERE quiz_topic = '%s'"
        cursor.execute(loadquizname % (choosequiztopic))
        checkdata = cursor.fetchall()

        if checkdata[0][0] == choosequiztopic:
            query = "UPDATE quiz SET quiz_topic = '" + str(newquiztopic) + "' WHERE User_ID = '" + str(userID) + "'"

            ## storing values in a variable
            # values = (quiz_name, userID)
            ## executing the query with values
            # cursor.execute(query, values)
            cursor.execute(query)
            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print(cursor.rowcount, "Quiz Topic Sucessfully Edited!")
            print("==============================")
            return editquizMenu()

    elif confirm == 'N' or confirm == 'n':
        return editquizMenu()

    else:
        while confirm != 'Y' or confirm != 'y' or confirm != 'N' or confirm != 'n':
            print("==============================")
            print("Incorrect input! Please try again..")
            print("==============================")
            confirm = input("Are you sure you want to change your quiz topic ( " + str(choosequiztopic) + " ) ? \n\
                              Press (Y) to confirm (N) to cancel:")

            if confirm == 'Y' or confirm == 'y':
                loadquizname = "SELECT quiz_topic FROM quiz WHERE quiz_topic = '%s'"
                cursor.execute(loadquizname % (choosequiztopic))
                checkdata = cursor.fetchall()

                if checkdata[0][0] == choosequiztopic:
                    query = "UPDATE quiz SET quiz_topic = '" + str(newquiztopic) + "' WHERE User_ID = '" + str(
                        userID) + "'"

                    ## storing values in a variable
                    # values = (quiz_name, userID)
                    ## executing the query with values
                    # cursor.execute(query, values)
                    cursor.execute(query)
                    ## to make final output we have to run
                    ## the 'commit()' method of the database object
                    db.commit()
                    db.autocommit = True

                    print("==============================")
                    print(cursor.rowcount, "Quiz Topic Sucessfully Edited!")
                    print("==============================")
                    return editquizMenu()

            elif confirm == 'N' or confirm == 'n':
                return editquizMenu()

def answerQuiz():

    print("1. attempted quiz")
    print("2. not attempted quiz")
    pilih = input("which ne?? : ")
    print("=============================")

    if pilih == "1":
        query = "SELECT quiz_id, quiz_name FROM quiz"
        cursor.execute(query)
        checkdata = cursor.fetchall()
        i=1
        if len(checkdata) > 0:
            print("List of the quiz for you: ")
            for row in checkdata:
                query4 = "SELECT quiz_id, User_ID  FROM attempt"
                cursor.execute(query4)
                checkattempt = cursor.fetchall()

                if len(checkattempt) > 0:
                    for row2 in checkattempt:
                        if row2[0] == row[0]:
                            print(row[1])

            print("==============================")
        else:
            print("we dont have any quiz for you yet")

        name = input("enter quiz name to answer: ")

        query2 = "SELECT quiz_id, quiz_name FROM quiz where quiz_name = '%s'"
        cursor.execute(query2 % (name))
        checkname= cursor.fetchall()
        #print(checkname[0][0])
        #print(checkname[0][1])
        XD = checkname[0][0]
        if name == checkname[0][1]:
            print("jawab laa quiz kamu bingai")

            queryquestion = "SELECT Question, number FROM question where quiz_id = '%s' "
            cursor.execute(queryquestion % (XD))
            checkquestion = cursor.fetchall()

            number = 0
            number = (checkquestion[1][1])
            #print(number)

            x=0
            for row in checkquestion:
                print(row[0])
                answer = input("Your answer: ")
                print("\n")

            query = "INSERT INTO attempt(quiz_id,User_ID) VALUES (%s, %s)"

            ## storing values in a variable
            values = (XD, userID)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print("Quiz Sucessfully attempted!")

    elif pilih == "2":
        query = "SELECT quiz_id, quiz_name FROM quiz"
        cursor.execute(query)
        checkdata = cursor.fetchall()

        query = "SELECT quiz_id FROM attempt WHERE user_id = '%s'"
        cursor.execute(query%(userID))
        checkdata2 = cursor.fetchall()
        i = 1
        if len(checkdata) > 0:
            print("List of the quiz for you: ")
            quiz = []
            attempts = []
            for row in checkdata:
                quiz.append(row[0])
            for row in checkdata2:
                attempts.append(row[0])

            print(quiz)
            print(attempts)

            epic = set(quiz) ^ set(attempts)

            print(list(epic))

            for row in list(epic):
                query45 = "SELECT quiz_name FROM quiz WHERE quiz_id = '%s'"
                cursor.execute(query45 % (row))
                checkdata3 = cursor.fetchall()
                print(checkdata3[0][0])
                print("salam")

        else:
            print("we dont have any quiz for you yet")

        name = input("enter quiz name to answer: ")

        query2 = "SELECT quiz_id, quiz_name FROM quiz where quiz_name = '%s'"
        cursor.execute(query2 % (name))
        checkname = cursor.fetchall()
        # print(checkname[0][0])
        # print(checkname[0][1])
        XD = checkname[0][0]
        if name == checkname[0][1]:
            print("jawab laa quiz kamu bingai")

            queryquestion = "SELECT Question, number FROM question where quiz_id = '%s' "
            cursor.execute(queryquestion % (XD))
            checkquestion = cursor.fetchall()

            number = 0
            number = (checkquestion[1][1])
            # print(number)

            x = 0
            for row in checkquestion:
                print(row[0])
                answer = input("Your answer: ")
                print("\n")

            query = "INSERT INTO attempt(quiz_id,User_ID) VALUES (%s, %s)"

            ## storing values in a variable
            values = (XD, userID)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.autocommit = True

            print("==============================")
            print("Quiz Sucessfully attempted!")


mainMenu()
