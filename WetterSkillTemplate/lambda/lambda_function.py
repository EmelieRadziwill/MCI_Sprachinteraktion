# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import csv_utils
import json
import urllib.request
import csv

city = "dresden" #input location
KEY = "" #openweathermap api key

filepath = "config.csv" #place created configs in same directory as this file

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
            
        speak_output = '<speak>Bitte geben Sie Ihre ID an.</speak>'
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class AbfrageHandler(AbstractRequestHandler):
    """Handler for Abfrage Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Abfrage")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        file = open(filepath, "r")
        csvdata = list(csv.reader(file, delimiter=";"))
        file.close()
        csvdata = csvdata[1:]
        
        slot = ask_utils.request_util.get_slot(handler_input, "ID") #asks for slot input
        
        flag = csv_utils.IdPresent(csvdata, slot.value)
        
        if(flag):
            volume, voice, language, speed, breaks, expression = csv_utils.getConfigs(csvdata, slot.value)
            
            if language == "de-DE":
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&lang=de&units=metric"
            else:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&lang=en&units=metric"
            with urllib.request.urlopen(url) as url:
                data = json.loads(url.read().decode())
                temp = int(data['main']['temp'])
                desc = data['weather'][0]['description']
                
                
            if expression:
                if language == "de-DE": 
                    speak_output = f'<speak><voice name="{voice}"><lang xml:lang="{language}"><prosody volume="{volume}"><prosody rate="{speed}">Es ist gerade {desc}, bei {temp} Grad Celsius.</prosody></prosody></lang></voice></speak>'
                else:
                    speak_output = f'<speak><voice name="{voice}"><lang xml:lang="{language}"><prosody volume="{volume}"><prosody rate="{speed}">It is {desc}. The temperature is {temp} degrees celsius.</prosody></prosody></lang></voice></speak>'
            else:
                if language == "de-DE":
                    speak_output = f'<speak><voice name="{voice}"><lang xml:lang="{language}"><prosody volume="{volume}"><prosody rate="{speed}">Lass mich kurz nachgucken. <break strength="{breaks}"/> Das Wetter ist im Moment {desc}. <break strength="{breaks}"/>Die Temperatur beträgt {temp} Grad Celsius.</prosody></prosody></lang></voice></speak>'
                else:
                    speak_output = f'<speak><voice name="{voice}"><lang xml:lang="{language}"><prosody volume="{volume}"><prosody rate="{speed}">Let me see. <break strength="{breaks}"/> The weather is currently {desc} and the temperature is {temp} degrees celsius.</prosody></prosody></lang></voice></speak>'
              
            ''' formatted for better readability        
            <speak>
            	<voice="{voice}">
            		<lang xml:lang="{language}">
            			<prosody volume="{volume}", rate="{speed}">
            			    <prosody rate="{speed}">
                				First sentence <break strength="{breaks}">
                				Second sentence
                			</prosody>
            			</prosody>
            		</lang>
            	</voice>
            </speak>   
            '''
            
        else:
            speak_output = "Keine Konfiguration mit dieser ID gefunden"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AbfrageHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()