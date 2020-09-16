import pytest
from datetime import date, datetime
from pytz import timezone

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_get_date import GetDateValue


@pytest.fixture
def get_date_value():
    return GetDateValue()


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


def test_name(get_date_value):
    name = get_date_value.name()

    assert name == "action_get_date"


def test_run_en(get_date_value, default_dispatcher, default_domain):

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

    result = get_date_value.run(default_dispatcher, en_tracker, default_domain)

    bot_date = result[0]['value']
    followup_action = result[1]['name']
    assert bot_date == date.today().strftime("%d/%m/%Y")
    assert followup_action == "utter_features_date"


def test_run_br(get_date_value, default_dispatcher, default_domain):

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

    result = get_date_value.run(default_dispatcher, br_tracker, default_domain)

    bot_date_acre = result[0]['value']
    bot_date_fnoronha = result[1]['value']
    bot_date_brasilia = result[2]['value']
    bot_date_amazonas = result[3]['value']
    followup_action = result[4]['name']
    assert bot_date_acre == datetime.now(timezone('Brazil/Acre')).strftime("%d/%m/%Y")
    assert bot_date_fnoronha == datetime.now(timezone('Brazil/DeNoronha')).strftime("%d/%m/%Y")
    assert bot_date_brasilia == datetime.now(timezone('Brazil/East')).strftime("%d/%m/%Y")
    assert bot_date_amazonas == datetime.now(timezone('Brazil/West')).strftime("%d/%m/%Y")
    assert followup_action == "utter_features_date"
