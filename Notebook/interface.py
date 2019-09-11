from main import Notes


def interface():
    a = Notes()
    choose = 0
    while choose != 7:
        print(" ##############################\n",
              "#  1. New note               #\n",
              "#----------------------------#\n",
              "#  2. Open note              #\n",
              "#----------------------------#\n",
              "#  3. Delete note(Input '*'  #\n",
              "#     to delete all notes)   #\n",
              "#----------------------------#\n",
              "#  4. Display all notes      #\n",
              "#----------------------------#\n",
              "#  5. Edit note              #\n",
              "#----------------------------#\n",
              "#  7. Exit                   #\n",
              "#----------------------------#\n",
              "#  For aborting              #\n",
              "#  operation use '!q'        #\n",
              "##############################\n",
              )

        choose = int(input("What you like to do?\n" + ">>> "))
        if choose == 1:
            header = str(input("Input header name: "))
            if header.replace('.txt', '') == '!q':
                continue
            body = str(input("Input your note text: "))
            if body.replace('.txt', '') == '!q':
                continue
            a.newNote(header, body)

        if choose == 2:
            name = str(input("Input your note name: ")) + ".txt"
            if name.replace('.txt', '') == '!q':
                continue
            a.display(name)

        if choose == 3:
            header = str(input("Input your note name: ")) + ".txt"
            if header.replace('.txt', '') == '!q':
                continue
            a.delNote(header)

        if choose == 4:
            a.display(None, True)

        if choose == 5:
            option = 0
            header = str(input("Input your note name: ")) + ".txt"
            if header.replace('.txt', '') == '!q':
                continue
            else:
                while option != 4:
                    print(" ##############################\n",
                          "#  1. Do you want to         #\n",
                          "#     complement your note?  #\n",
                          "#----------------------------#\n",
                          "#  2. Do you want to         #\n",
                          "#     completely change      #\n",
                          "#     your note?             #\n",
                          "#----------------------------#\n",
                          "#  3. Do you want to change  #\n",
                          "#     name of your note?     #\n",
                          "#----------------------------#\n",
                          "#  4. Exit                   #\n",
                          "#----------------------------#\n",
                          "#  For aborting              #\n",
                          "#  operation use '!q'        #\n",
                          "##############################\n",)
                    option = str(input("What you like to do?\n" + ">>> "))
                    if option == '!q':
                        continue
                    if option == '3':
                        new_name = str(input("Input new name of note\n" + ">>> "))
                        a.editNote(header, option, new_name)
                    elif option == '4':
                        break
                    else:
                        a.editNote(header, option)

if __name__ == "__main__":
    interface()
