#-*-coding: utf-8 -*-
#/usr/bin/python3

import subprocess as sub
import os

class Buffer:
    def __init__(self):
        self.username = os.getlogin()
        self.allLocation = "/home/{0}/Documents/".format(self.username)
        self.bufferLocation = "/home/{0}/Desktop/".format(self.username)

    def clearMem(self):
        pass

    def save(self, header, body):
        sub.call(["touch " + self.bufferLocation + "buffer.txt"], shell=True)
        sub.call(["touch {0}".format(self.allLocation + header + ".txt")], shell=True)
        with open(self.allLocation + header + ".txt", "w", encoding="utf-8") as note:
            note.write(body + "\n")

        with open(self.bufferLocation + "buffer.txt", "w", encoding="utf-8") as buffer:
            buffer.write(header + "\n")
            buffer.write(body + "\n")

    def display(self, name=None, all=False):

        if all:
            sub.call(["cd {} && ls *.txt".format(self.allLocation)], shell=True)

        else:
            try:
                with open(self.allLocation + name, "r", encoding="utf-8") as note:
                    txt = note.read()
                    print(txt)
                return True
            except:
                print("Can`t find note with this name;(")
                return False


class Notes(Buffer):
    def newNote(self, header, body):
        self.save(header, body)

    def editNote(self, header, option, new_name=None):
        self.display(header)
        if option == '1':
            with open(self.allLocation + header, "a", encoding="utf-8") as note:
                edit_txt = str(input("Input your text:\n"))
                note.write(edit_txt)

        elif option == '2':
            with open(self.allLocation + header, "w", encoding="utf-8") as note:
                edit_txt = str(input("Copy and edit your note text:\n"))
                note.write(edit_txt)

        else:
            sub.call(["mv {0} {1}".format(self.allLocation + header,
                                          self.allLocation + new_name + ".txt")], shell=True)

    def delNote(self, header):
        code = sub.call(["rm " + self.allLocation + header], shell=True)
        if code == 0:
            return True

        else:
            return False
