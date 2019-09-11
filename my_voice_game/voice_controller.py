#!/usr/bin/env python
# -*- coding; utf-8 -*-

import speech_recognition as sr
import sys
import pyaudio
import pyttsx3
import threading

class Voice_Controller:
    def talk(self, words):
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()

    def zadanie(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Говори")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)

        try:
            self.command = r.recognize_google(audio, language = 'ru-RU').lower()
            print("Вы сказали: " + self.command)

        except sr.UnknownValueError:
            self.talk("Повтори")
            self.command = self.zadanie()

        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))
            self.command = self.zadanie()

        return self.command
