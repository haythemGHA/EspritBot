# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from email.message import EmailMessage
import imghdr
import logging
import json
from datetime import datetime
import smtplib
import googletrans
from googletrans import *
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)
from rasa_sdk.events import (SlotSet,AllSlotsReset)
import pandas as pd
import numpy as np
import folium
from folium import Marker
import warnings 
from geopy.geocoders import Nominatim
from shapely.geometry import Point
warnings.filterwarnings('ignore')
import webbrowser



logger = logging.getLogger(__name__)

class EspritInternal_pic_en(Action):
     def name(self) -> Text:
        return "action_EspritInternal_pic-en"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_EspritInternal_pic-en")
        dispatcher.utter_message(image= "https://imgur.com/a/4FfmJPN")
        dispatcher.utter_message(image= "https://imgur.com/a/elndNnJ")
        dispatcher.utter_message(image= "https://imgur.com/a/saGgzH1")
        dispatcher.utter_message(image= "https://imgur.com/a/CrYx1Pq")
        return []

class Alamen_pic_en(Action):
     def name(self) -> Text:
        return "action_Alamen_pic-en"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_Alamen_pic-en")
        dispatcher.utter_message(image= "https://imgur.com/a/v0vbyoI")
        dispatcher.utter_message(image= "https://imgur.com/a/mmq55tv")
        dispatcher.utter_message(image= "https://imgur.com/a/ZmHXbLC")
        return []

class Alamen_pic_fr(Action):
     def name(self) -> Text:
        return "action_Alamen_pic-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_Alamen_pic-fr")
        dispatcher.utter_message(image= "https://imgur.com/a/v0vbyoI")
        dispatcher.utter_message(image= "https://imgur.com/a/mmq55tv")
        dispatcher.utter_message(image= "https://imgur.com/a/ZmHXbLC")
        return []

class EspritInternal_pic_fr(Action):
     def name(self) -> Text:
        return "action_EspritInternal_pic-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_EspritInternal_pic-fr")
        dispatcher.utter_message(image= "https://imgur.com/a/4FfmJPN")
        dispatcher.utter_message(image= "https://imgur.com/a/elndNnJ")
        dispatcher.utter_message(image= "https://imgur.com/a/saGgzH1")
        dispatcher.utter_message(image= "https://imgur.com/a/CrYx1Pq")
        return []

class restaurant_en(Action):
     def name(self) -> Text:
        return "action_restaurant-en"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-en")
        dispatcher.utter_message(image= "https://imgur.com/a/sRBi5yI")
        dispatcher.utter_message(image= "https://imgur.com/a/QO6Ngfc")
        dispatcher.utter_message(image= "https://imgur.com/a/lqKfKP5")
        return []

class restaurant_fr(Action):
     def name(self) -> Text:
        return "action_restaurant-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-fr")
        dispatcher.utter_message(image= "https://imgur.com/a/sRBi5yI")
        dispatcher.utter_message(image= "https://imgur.com/a/QO6Ngfc")
        dispatcher.utter_message(image= "https://imgur.com/a/lqKfKP5")
        return []

class restaurant_tn_en(Action):
     def name(self) -> Text:
        return "action_restaurant-tn-en"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-tn-en")
        dispatcher.utter_message(image= "https://imgur.com/a/sQwJ5Nm")
        dispatcher.utter_message(image= "https://imgur.com/a/jCDWLWY")
        return []

class restaurant_tn_fr(Action):
     def name(self) -> Text:
        return "action_restaurant-tn-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-tn-fr")
        dispatcher.utter_message(image= "https://imgur.com/a/sQwJ5Nm")
        dispatcher.utter_message(image= "https://imgur.com/a/jCDWLWY")
        return []

class restaurant_int_en(Action):
     def name(self) -> Text:
        return "action_restaurant-int-en"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-int-en")
        dispatcher.utter_message(image= "https://imgur.com/a/EpGHJU9")
        dispatcher.utter_message(image= "https://imgur.com/a/1Ahew7Y")
        return []

class restaurant_int_fr(Action):
     def name(self) -> Text:
        return "action_restaurant-int-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_restaurant-int-fr")
        dispatcher.utter_message(image= "https://imgur.com/a/EpGHJU9")
        dispatcher.utter_message(image= "https://imgur.com/a/1Ahew7Y")
        return []

class ActionAskEmail(Action):
    def name(self) -> Text:
        return "action_ask_email"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
            dispatcher.utter_message(response="utter_ask_email")
            return []

class ActionAskEmail_fr(Action):
    def name(self) -> Text:
        return "action_ask_email-fr"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
            dispatcher.utter_message(response="utter_ask_email-fr")
            return []

class Esprit_link(Action):
     def name(self) -> Text:
        return "action_Esprit_link"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_Esprit-en")
        dispatcher.utter_message(text = "please connect via this link https://esprit.tn/ to see more information ")
        return []

class Esprit_link_fr(Action):
     def name(self) -> Text:
        return "action_Esprit_link-fr"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_Esprit-fr")
        dispatcher.utter_message(text = "merci de vous connecter via ce lien https://esprit.tn/ pour voir plus d'informations ")
        return []

        

class languageAction(Action):
    def name(self) -> Text:
        return "action_language"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Francais", "payload":'/Francais{"language":"Francais"}'})
        buttons.append({"title": "English", "payload":'/English{"language":"English"}'})
        dispatcher.utter_message(text="Please select the button to choose the language", buttons = buttons)
        return[]

class classeAction(Action):
    def name(self) -> Text:
        return "action_classe"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Normal Classes", "payload":'/Normal Classes{"classe":"Normal Classes"}'})
        buttons.append({"title": "Evening Classes", "payload":'/Evening Classes{"classe":"Evening Classes"}'})
        buttons.append({"title": "Preparatory Cycles", "payload":'/Preparatory Cycles{"classe":"Preparatory Cycles"}'})
        dispatcher.utter_message(text="Please select the button to choose the class ", buttons = buttons)
        return[]

class SpecialiteAction(Action):
    def name(self) -> Text:
        return "action_specialite"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Electromecanique", "payload":'/Electromecanique{"specialite":"Electromecanique"}'})
        buttons.append({"title": "Génie civil", "payload":'/Génie civil{"specialite":"Génie civil"}'})
        buttons.append({"title": "Informatique", "payload":'/Informatique{"specialite":"Informatique"}'})
        buttons.append({"title": "Telecommunication", "payload":'/Telecommunication{"specialite":"Telecommunication"}'})
        dispatcher.utter_message(text="Please select the button to choose the specialite ", buttons = buttons)
        return[]

class TunisianInternationalAction(Action):
    def name(self) -> Text:
        return "action_tunisian_international"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Tunisian", "payload":'/tunisian{"nationalite":"tunisian"}'})
        buttons.append({"title": "International", "payload":'/international{"nationalite":"international"}'})
        dispatcher.utter_message(text="Please select the button that describes your status", buttons = buttons)
        return[]

class hostelAction(Action):
    def name(self) -> Text:
        return "action_hostel"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "ESPRIT Internal Residence", "payload":'/ESPRIT Internal Residence{"hostel":"ESPRIT Internal Residence"}'})
        buttons.append({"title": "Al Amen Residence", "payload":'/Al Amen Residence{"hostel":"Al Amen Residence"}'})
        dispatcher.utter_message(text="Please select the button to choose the hostel type", buttons = buttons)
        return[]

class Reglement_concours_esprit(Action):
     def name(self) -> Text:
        return "action_Reglement_concours_esprit"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
            rep="file:///C:/Users/admin/RasaPi/rasa_env/pdf_docs/Règlement_du_concours_d'admission_22-23.pdf"
            dispatcher.utter_message(rep)
            email = tracker.get_slot("email")
            msg = EmailMessage()
            msg['Subject'] = 'Règlement du concours d admission 22-23'
            msg['From'] = 'EspritBot@gmail.com'
            msg['To'] = str(email)
            

            msg.set_content('This is the Rules of admission competition')

            file ="C:/Users/admin/RasaPi/rasa_env/pdf_docs/Règlement_du_concours_d'admission_22-23.pdf"
            with open(file,'rb') as f :
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stram',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("espritbot@gmail.com", "espritbot2003")
                smtp.send_message(msg)
            dispatcher.utter_message(text="Please check your mail. I have sent you an email there.")
        
            return []

class Reglement_scolarite_esprit(Action):
     def name(self) -> Text:
        return "action_Reglement_scolarite_esprit"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
            rep="file:///C:/Users/admin/RasaPi/rasa_env/pdf_docs/RegSCO_coursdujour_22-23.pdf"
            dispatcher.utter_message(rep)
            email = tracker.get_slot("email")
            msg = EmailMessage()
            msg['Subject'] = 'Règlement de scolarité 22-23'
            msg['From'] = 'EspritBot@gmail.com'
            msg['To'] = str(email)
            

            msg.set_content('This is the School rules of our University')

            file ="C:/Users/admin/RasaPi/rasa_env/pdf_docs/RegSCO_coursdujour_22-23.pdf"
            with open(file,'rb') as f :
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stram',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("espritbot@gmail.com", "espritbot2003")
                smtp.send_message(msg)
            dispatcher.utter_message(text="Please check your mail. I have sent you an email there.")
        
            return []

class catalogue_electromecanique_esprit(Action):
     def name(self) -> Text:
        return "action_electromecanique_pdf"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
            rep="file:///C:/Users/admin/RasaPi/rasa_env/pdf_docs/Présentation-site-EM.698ecfa4.pdf"
            dispatcher.utter_message(rep)
            email = tracker.get_slot("email")
            msg = EmailMessage()
            msg['Subject'] = 'Presentation site Electromecanique'
            msg['From'] = 'EspritBot@gmail.com'
            msg['To'] = str(email)
            

            msg.set_content('To know more about Electromecanique Specialitie')

            file ="C:/Users/admin/RasaPi/rasa_env/pdf_docs/Présentation-site-EM.698ecfa4.pdf"
            with open(file,'rb') as f :
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stram',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("espritbot@gmail.com", "espritbot2003")
                smtp.send_message(msg)
            dispatcher.utter_message(text="Please check your mail. I have sent you an email there.")
        
            return []

class catalogue_tic_esprit(Action):
     def name(self) -> Text:
        return "action_tic_pdf"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
            rep="file:///C:/Users/admin/RasaPi/rasa_env/pdf_docs/présentation-TIC.d4a7662a.pdf"
            dispatcher.utter_message(rep)
            email = tracker.get_slot("email")
            msg = EmailMessage()
            msg['Subject'] = 'Presentation site TIC'
            msg['From'] = 'EspritBot@gmail.com'
            msg['To'] = str(email)
            

            msg.set_content('To know more about TIC Specialitie')

            file ="C:/Users/admin/RasaPi/rasa_env/pdf_docs/présentation-TIC.d4a7662a.pdf"
            with open(file,'rb') as f :
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stram',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("espritbot@gmail.com", "espritbot2003")
                smtp.send_message(msg)
            dispatcher.utter_message(text="Please check your mail. I have sent you an email there.")
        
            return []

class catalogue_GenieCivil_esprit(Action):
     def name(self) -> Text:
        return "action_geniecivil_pdf"

     def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
            rep="file:///C:/Users/admin/RasaPi/rasa_env/pdf_docs/présentation-génie-civil.6b641af4.pdf"
            dispatcher.utter_message(rep)
            email = tracker.get_slot("email")
            msg = EmailMessage()
            msg['Subject'] = 'Presentation site Genie Civil'
            msg['From'] = 'EspritBot@gmail.com'
            msg['To'] = str(email)
            

            msg.set_content('To know more about Genie Civil Specialitie')

            file ="C:/Users/admin/RasaPi/rasa_env/pdf_docs/présentation-génie-civil.6b641af4.pdf"
            with open(file,'rb') as f :
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stram',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("espritbot@gmail.com", "espritbot2003")
                smtp.send_message(msg)
            dispatcher.utter_message(text="Please check your mail. I have sent you an email there.")
        
            return []

class ActionPause(Action):
    """Pause the conversation"""

    def name(self) -> Text:
        return "action_pause"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        return [ConversationPaused()]

class ActionStoreBotLanguage(Action):
    """Takes the bot language and checks what pipelines can be used"""

    def name(self) -> Text:
        return "action_store_bot_language"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        spacy_languages = [
            "english",
            "french",
        ]
        language = tracker.get_slot("language")
        if not language:
            return [
                SlotSet("language", "that language"),
                SlotSet("can_use_spacy", False),
            ]

        if language.lower() in spacy_languages:
            return [SlotSet("can_use_spacy", True)]
        else:
            return [SlotSet("can_use_spacy", False)]

class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        if intent == "greet-en" or (intent == "enter_data" and name_entity):
            if name_entity and name_entity.lower() != "sara":
                dispatcher.utter_message(response="utter_greet_name", name=name_entity)
                return []
            else:
                dispatcher.utter_message(response="utter_greet_noname")
                return []
            
        dispatcher.utter_message(response="utter_greet-en")
        return []

class ActionGreetUser_fr(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user-fr"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        if intent == "greet-fr" or (intent == "enter_data-fr" and name_entity):
            if name_entity and name_entity.lower() != "sara":
                dispatcher.utter_message(response="utter_greet_name-fr", name=name_entity)
                return []
            else:
                dispatcher.utter_message(response="utter_greet_noname-fr")
                return []
            
        dispatcher.utter_message(response="utter_greet-fr")
        return []


class LocationMapAction(Action):
    def name(self) -> Text:
        return "action_location_map"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        df = pd.read_csv(r"C:\Users\admin\RasaPi\rasa_env\departments_locations.csv")
        m = folium.Map(location=[36, 10], tiles='openstreetmap', zoom_start=7)
        for idx, row in df.iterrows():
            Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)
        m.save("map.html")
        webbrowser.open("map.html")
        return []

class ActionRestartWithButton(Action):
    def name(self) -> Text:
        return "action_restart_with_button"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> None:

        dispatcher.utter_message(response="utter_restart_with_button")

class ActionRestartWithButton(Action):
    def name(self) -> Text:
        return "action_restart_with_button-fr"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> None:

        dispatcher.utter_message(response="utter_restart_with_button-fr")

class ActionTagFeedback(Action):

    def name(self):
        return "action_tag_feedback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:

        feedback = tracker.get_slot("feedback_value")

        if feedback == "positive":
            label = '[{"value":"postive feedback","color":"76af3d"}]'
        elif feedback == "negative":
            label = '[{"value":"negative feedback","color":"ff0000"}]'
        else:
            return []


        return []

class AcceptmailingAction(Action):
    def name(self) -> Text:
        return "action_accept_mailing"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Accept", "payload":'/track_status{"track_status":"Yes"}'})
        buttons.append({"title": "Deny", "payload":'/track_status{"track_status":"No"}'})
    
        dispatcher.utter_message(text="Do you want to recive an email for more details ?", buttons = buttons)
    
        return []

class AcceptmailingAction_fr(Action):
    def name(self) -> Text:
        return "action_accept_mailing-fr"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
        buttons = []
        buttons.append({"title": "Accept", "payload":'/track_status-fr{"track_status":"Oui"}'})
        buttons.append({"title": "Deny", "payload":'/track_status-fr{"track_status":"Non"}'})
    
        dispatcher.utter_message(text="Vous souhaitez recevoir un email pour plus de détails ?", buttons = buttons)
    
        return []