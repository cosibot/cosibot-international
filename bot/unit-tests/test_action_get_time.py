import pytest
import time
from datetime import datetime
from pytz import timezone

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_get_time import GetTimeValue


@pytest.fixture
def get_time_value():
    return GetTimeValue()


@pytest.fixture
def default_domain():
    return Domain(
        intents={},
        entities=[],
        slots=[],
        templates={},
        action_names=["utter_welcome", ],
        form_names=[],
    )


@pytest.fixture
def default_dispatcher():
    return CollectingDispatcher()


def test_name(get_time_value):
    name = get_time_value.name()

    assert name == "action_get_time"


def test_run_en(get_time_value, default_dispatcher, default_domain):

    en_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={"bot_location": "en"},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = get_time_value.run(default_dispatcher, en_tracker, default_domain)

    bot_time = result[0]['value']
    followup_action = result[1]['name']
    assert bot_time == time.strftime("%H:%M:%S", time.localtime())
    assert followup_action == "utter_features_time"


def test_run_br(get_time_value, default_dispatcher, default_domain):

    br_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={"bot_location": "br"},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = get_time_value.run(default_dispatcher, br_tracker, default_domain)

    bot_time_acre = result[0]['value']
    bot_time_fnoronha = result[1]['value']
    bot_time_brasilia = result[2]['value']
    bot_time_amazonas = result[3]['value']
    followup_action = result[4]['name']
    assert bot_time_acre == datetime.now(timezone('Brazil/Acre')).strftime("%H:%M:%S")
    assert bot_time_fnoronha == datetime.now(timezone('Brazil/DeNoronha')).strftime("%H:%M:%S")
    assert bot_time_brasilia == datetime.now(timezone('Brazil/East')).strftime("%H:%M:%S")
    assert bot_time_amazonas == datetime.now(timezone('Brazil/West')).strftime("%H:%M:%S")
    assert followup_action == "utter_features_time"
