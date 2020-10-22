from typing import Text

import requests
from datetime import date, datetime, timedelta

from .action_search_stats import DecsisAPI as contry_api

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted

class DecsisAPI:

    def search(self, country_region, date_filter=None):
        try:
            query_fields = "[{\"region\": \"field\"},{\"confirmed\": \"sum\"},{\"confirmed_new\": \"sum\"},{\"deaths_new\": \"sum\"},{\"deaths_accum\": \"sum\"}]"

            query_filters = "[{\"region\":\""+ str(country_region) + "\"}]"

            request_url = "https://api.data.decsis.cloud/api/v1/dataset/br_mins_covid19?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +",\"group_by\":[{\"region\":\"group\"}]}&format=json&last-data=date&limit=10"
            response = requests.get(url = request_url)

            json_response = (response.json())

            if (len(json_response) > 0):
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
            else:
                stats['code'] = response.status_code
                stats['has_data'] = False

                return stats
        except:
            print('action_search_stats_region----------', e)
            return {'code': 500, 'has_data': False}


class ActionSearchStatsRegion(Action):

    def name(self):
        return "action_search_stats_region"
    
    def run(self, dispatcher, tracker, domain):
        
        country_region = next(tracker.get_latest_entity_values("country_region"), None)
        print("country region is {}".format(country_region))

        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_region)

        if stats['code'] == 200 and not stats['has_data']:
            return [
                SlotSet('country_region_search_successful', 'empty'),
                SlotSet('country_region', country_region),
                SlotSet('country_code', 'BR'),
                FollowupAction("utter_country_region_nodata")]
        elif stats['code'] == 200 and stats['has_data']:
            return [SlotSet('country_region_search_successful', 'ok'),
                SlotSet('country_region', country_region),
                SlotSet('country_region_confirmed_accum',int(stats.get('confirmed', "N/A"))),
                SlotSet('country_region_confirmed_new',int(stats.get('confirmed_new', "N/A"))),
                SlotSet('country_region_deaths_accum',int(stats.get('deaths_accum', "N/A"))),
                SlotSet('country_region_deaths_new',int(stats.get('deaths_new', "N/A"))),
                FollowupAction("utter_country_region_hasdata")]
        else:
            return [
                SlotSet('country_regionsearch_successful', 'not-ok'),
                SlotSet('country_code', 'BR'),
                FollowupAction("utter_country_region_nodata")]