# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests


class ActionResponseLed(Action):

    def name(self) -> Text:
        return "action_response_led"

    def run(self, dispatcher, tracker, domain):

        status = tracker.get_slot('led_status')
        if status == False :
            status = "desligado"
        else:
            status = "ligado"

        dispatcher.utter_message("O quarto está {}".format(status))
        return[]


class ActionLedOn(Action):

    def name(self) -> Text:
        return "action_resolve_led_on"

    def run(self, dispatcher, tracker, domain):

        status = tracker.get_slot('led_status')
        if status == False:        
            dispatcher.utter_message("luz do quarto acesa!")
            status_led = True
        else:
            dispatcher.utter_message("A luz do quarto já está aceso!")
            status_led = True
        # return[SlotSet("led_status", status_led)]
        return[]
    
class ActionLedOff(Action):

    def name(self) -> Text:
        return "action_resolve_led_off"

    def run(self, dispatcher, tracker, domain):

        status = tracker.get_slot('led')
        if status == False:        
            dispatcher.utter_message("a luz do quarto já está apagada!")
            status_led = False
        else:
            dispatcher.utter_message("Luz do quarto apagada")
            status_led = False
        # return[SlotSet("led_status", status_led)]
        return[]


class ActionResponsePwm(Action):

    def name(self) -> Text:
        return "action_response_pwm"

    def run(self, dispatcher, tracker, domain):

        pwm = tracker.get_slot('pwm')
        if pwm == False :
            pwm = "desligado"
        else:
            pwm = "ligado"

        dispatcher.utter_message(" A sala está {}".format(pwm))
        return[]

class ActionPwmOn(Action):

    def name(self) -> Text:
        return "action_resolve_pwm_on"

    def run(self, dispatcher, tracker, domain):

        status = tracker.get_slot('pwm')
        if status == False:             
            dispatcher.utter_message("Luz da sala acesa!")
            status_pwm = True
        else:
            dispatcher.utter_message("A luz da sala já está acesa!")
            status_pwm = True
        # return[SlotSet("pwm_status", status_pwm)]
        return[]

class ActionPwmOff(Action):

    def name(self) -> Text:
        return "action_resolve_pwm_off"

    def run(self, dispatcher, tracker, domain):

        status = tracker.get_slot('pwm')
        if status == False:        
            dispatcher.utter_message("A sala já está apagado!")
            status_pwm = False
        else:
            dispatcher.utter_message("Luz da sala apagada!")
            status_pwm = False
        # return[SlotSet("pwm_status", status_pwm)]
        return[]