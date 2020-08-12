import time
from datetime import date
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from rasa_sdk import Action, Tracker
from typing import Text, Any, Dict, List
import logging
logger = logging.getLogger(__name__)
from pytz import timezone
from datetime import date,datetime

class GetDateValue(Action):

    def name(self):
        return "action_get_date"

    def run(self, dispatcher, tracker, domain):
        if (tracker.get_slot('bot_location') != "br"):
            #print("     !!! not br")
            today = date.today()
            return [SlotSet("bot_date", today.strftime("%d/%m/%Y")),
                    FollowupAction("utter_features_date")]
        else:
            #print("     !!! br")
            date_output = "%d/%m/%Y"
            brazil_acre = datetime.now(timezone('Brazil/Acre'))
            brazil_fnoronha = datetime.now(timezone('Brazil/DeNoronha'))
            brazil_brasilia = datetime.now(timezone('Brazil/East'))
            brazil_amazonas = datetime.now(timezone('Brazil/West'))

            return [SlotSet("bot_date_acre", brazil_acre.strftime(date_output)),
                    SlotSet("bot_date_fnoronha",
                            brazil_fnoronha.strftime(date_output)),
                    SlotSet("bot_date_brasilia",
                            brazil_brasilia.strftime(date_output)),
                    SlotSet("bot_date_amazonas",
                            brazil_amazonas.strftime(date_output)),
                    FollowupAction("utter_features_date")]
