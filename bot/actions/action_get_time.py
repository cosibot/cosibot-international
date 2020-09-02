
from typing import Text, Any, Dict, List
import time
from pytz import timezone
from datetime import datetime

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk import Action, Tracker

import logging


logger = logging.getLogger(__name__)


class GetTimeValue(Action):

    def name(self):
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if (tracker.get_slot('bot_location') != "br"):
            # print("     !!! not br")
            t = time.localtime()
            return [SlotSet("bot_time", time.strftime("%H:%M:%S", t)),
                    FollowupAction("utter_features_time")]
        else:
            # print("     !!! br")
            time_output = "%H:%M:%S"
            # t = time.localtime()
            brazil_acre = datetime.now(timezone('Brazil/Acre'))
            brazil_fnoronha = datetime.now(timezone('Brazil/DeNoronha'))
            brazil_brasilia = datetime.now(timezone('Brazil/East'))
            brazil_amazonas = datetime.now(timezone('Brazil/West'))

            # return [SlotSet("bot_time", time.strftime("%H:%M:%S", t)),
            # FollowupAction("utter_features_time")]

            return [SlotSet("bot_time_acre", brazil_acre.strftime(time_output)),
                    SlotSet("bot_time_fnoronha",
                            brazil_fnoronha.strftime(time_output)),
                    SlotSet("bot_time_brasilia",
                            brazil_brasilia.strftime(time_output)),
                    SlotSet("bot_time_amazonas",
                            brazil_amazonas.strftime(time_output)),
                    FollowupAction("utter_features_time")]
