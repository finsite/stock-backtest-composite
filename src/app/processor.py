"""Processor module for stock-backtest-composite signal generation.

Validates incoming messages and synthesizes a composite signal
based on multiple individual signals (e.g., alpha, beta, momentum).
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """Validate the incoming raw message against the expected schema.

    Args:
        message (dict[str, Any]): The raw message payload.

    Returns:
        ValidatedMessage: A validated message object.

    Raises:
        ValueError: If the message format is invalid.

    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Invalid message schema: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def compute_composite_signal(message: ValidatedMessage) -> dict[str, Any]:
    """Compute a composite signal by aggregating available signals.

    This example uses simple voting logic across multiple sub-signals.

    Args:
        message (ValidatedMessage): The validated input data.

    Returns:
        dict[str, Any]: The enriched message with a composite signal.

    """
    symbol = message.get("symbol", "UNKNOWN")
    logger.info("🧠 Computing composite signal for %s", symbol)

    signal_votes = {
        "alpha": message.get("signal_alpha"),
        "beta": message.get("beta_signal"),
        "momentum": message.get("momentum_signal"),
        "anomaly": "IGNORE" if message.get("anomaly_detected") else "INCLUDE",
    }

    vote_count = sum(
        1 for vote in signal_votes.values() if vote in ("BUY", "INCLUDE", "OVEREXPOSED")
    )

    composite_signal = "BUY" if vote_count >= 2 else "HOLD"

    result = {
        "composite_signal": composite_signal,
        "signal_votes": signal_votes,
    }

    logger.debug("🧮 Composite signal result for %s: %s", symbol, result)
    return {**message, **result}
