from unittest.mock import patch

from django.test import override_settings

from ..public_log import emit_public_log
from ..public_log_drain import LogDrainAttributes, LogLevel, LogType


@override_settings(OTEL_TRANSPORTED_ENDPOINT=None)
@patch("saleor.public_log_drain.public_log.PublicLogDrain.emit_log")
def test_emit_public_log_no_transporters(mocked_emit_log):
    # given
    logger_name = "test_name"
    trace_id = 1
    attributes = LogDrainAttributes(
        type=LogType.WEBHOOK_SENT,
        level=LogLevel.INFO,
        api_url="test-api-url",
        message="Test message",
    )

    # when
    emit_public_log(logger_name, trace_id, attributes)

    # then
    mocked_emit_log.assert_not_called()


@override_settings(OTEL_TRANSPORTED_ENDPOINT="test-endpoint")
@patch("saleor.public_log_drain.public_log.PublicLogDrain.emit_log")
def test_emit_public_log_otel(mocked_emit_log):
    # given
    logger_name = "test_name"
    trace_id = 1
    attributes = LogDrainAttributes(
        type=LogType.WEBHOOK_SENT,
        level=LogLevel.INFO,
        api_url="test-api-url",
        message="Test message",
    )

    # when
    emit_public_log(logger_name, trace_id, attributes)

    # then
    mocked_emit_log.assert_called_once_with(logger_name, trace_id, attributes)
