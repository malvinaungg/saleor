from django.conf import settings

from .public_log_drain import LogDrainAttributes, PublicLogDrain
from .transporters import LogDrainTransporter
from .transporters.public_log_drain_http_transporter import LogDrainHTTPTransporter
from .transporters.public_log_drain_otel_transporter import LogDrainOtelTransporter


def emit_public_log(
    logger_name: str, trace_id: int, span_id: int, attributes: LogDrainAttributes
):
    transports: list[LogDrainTransporter] = []
    if otl_endpoint := settings.OTEL_TRANSPORTED_ENDPOINT:
        transports.append(LogDrainOtelTransporter(endpoint=otl_endpoint))
    if otl_endpoint := settings.HTTP_TRANSPORTED_ENDPOINT:
        transports.append(LogDrainHTTPTransporter(endpoint=otl_endpoint))
    if not transports:
        return
    PublicLogDrain(transports).emit_log(logger_name, trace_id, span_id, attributes)