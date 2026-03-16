import pytest

from python_design_patterns.design_patterns.structural.adapter import PaymentAdapter, process_user_payment
from unittest.mock import MagicMock

class TestPaymentAdapter:

    @pytest.fixture
    def legacy_processor(self):
        return MagicMock()

    @pytest.fixture
    def adapter(self, legacy_processor):
        return PaymentAdapter(legacy_processor)

    def test_process_payment(self, adapter, legacy_processor):
        # Setup
        payment_data = {"amount": 100}
        expected_xml = "<payment>{\"amount\": 100}</payment>"
        legacy_processor.process_xml_payment.return_value = f"Processed XML payment: {expected_xml}"

        # Action
        result = adapter.process_payment(payment_data)

        # Assert
        assert result == f"Processed XML payment: {expected_xml}"
        legacy_processor.process_xml_payment.assert_called_once_with(expected_xml)

    def test_process_user_payment(self, adapter, legacy_processor):
        # Setup
        payment_data = {"amount": 200}
        expected_xml = "<payment>{\"amount\": 200}</payment>"
        legacy_processor.process_xml_payment.return_value = f"Processed XML payment: {expected_xml}"

        # Action
        result = process_user_payment(adapter, payment_data)

        # Assert
        assert result == f"Processed XML payment: {expected_xml}"
