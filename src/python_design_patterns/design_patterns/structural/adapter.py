"""
Adapter Design Pattern | https://wikipedia.org/wiki/Adapter_pattern

The Adapter pattern allows incompatible interfaces to work together.
It acts as a bridge between two incompatible interfaces.
"""
import json

from abc import ABC, abstractmethod

""" Adapter pattern example integrating a legacy payment processor with a new system that uses JSON data."""
class LegacyPaymentProcessor:
    """ A legacy payment processor that only accepts XML data. """
    def process_xml_payment(self, xml_data: str) -> str:
        # Simulate processing XML payment
        return f"Processed XML payment: {xml_data}"

""" The new system expects to work with JSON data, so we create an adapter to convert JSON to XML. """
class PaymentProcessor(ABC):
    """ Target interface expected by the new system. """
    @abstractmethod
    def process_payment(self, json_data: dict) -> str:
        pass

""" The Adapter class that allows the new system to use the legacy payment processor. """
class PaymentAdapter(PaymentProcessor):
    """ Adapter that converts JSON data to XML and uses the legacy processor. """

    def __init__(self, legacy_processor: LegacyPaymentProcessor):
        self.legacy_processor = legacy_processor

    def process_payment(self, json_data: dict) -> str:
        xml_data = self._convert_json_to_xml(json_data)
        return self.legacy_processor.process_xml_payment(xml_data)

    def _convert_json_to_xml(self, json_data: dict) -> str:
        # Simulate conversion (in real code, use a proper library)
        return f"<payment>{json.dumps(json_data)}</payment>"

# Client code
def process_user_payment(processor: PaymentProcessor, payment_data: dict) -> str:
    return processor.process_payment(payment_data)
