from typing import Text, Any, Dict, List

import logging

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ChangePreferredLanguage(Action):

    def name(self):
        return "action_change_preferred_language"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        preferred_lang = next(tracker.get_latest_entity_values("preferred_lang"), None)

        lang_code = preferred_lang.split('_')[0]
        print("lang_code: {}".format(lang_code))

        return [SlotSet('preferred_lang', lang_code), FollowupAction("utter_command_change_bot")]
