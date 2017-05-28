"""Example module."""
import logging


LOGGER = logging.getLogger(__name__)


def example_function(result):
    """
    Echo the passed in value.

    Example function.
    """
    LOGGER.debug('Example: %s', result)
    return result
