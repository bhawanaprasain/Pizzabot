from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_PIZZA_SIZES = [
    "small",
    "mini",
    "medium",
    "large",
    "extra-large",
    "extra large",
    "s",
    "m",
    "l",
    "xl",
]
ALLOWED_PIZZA_TYPES = [
    "mozzarella",
    "fungi",
    "veggie",
    "pepperoni",
    "hawaii",
    "vegiterian",
    "chicken",
]
ALLOWED_TOPPINGS = ["cheese", "olives", "bacon"]


class ValidatePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_pizza_form"

    def validate_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `size` value."""

        if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
            dispatcher.utter_message(text=f"We only accept pizza sizes: s/m/l/xl.")
            return {"size": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"size": slot_value}

    def validate_pizza_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""

        if slot_value not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(
                text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
            )
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_type": slot_value}

    def validate_topping(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `topping` value."""

        if slot_value not in ALLOWED_TOPPINGS:
            dispatcher.utter_message(
                text=f"I don't recognize that topping. We only have: {'/'.join(ALLOWED_TOPPINGS)} toppings."
            )
            return {"topping": None}
        dispatcher.utter_message(text=f"Alright! I'll add {slot_value} topping.")
        return {"topping": slot_value}
