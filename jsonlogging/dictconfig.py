import json

from .formatters import WrapedJsonFormatter
from .recordadapter import default_record_adapter


def json_formatter_factory(json_encoder={}, format="{json}"):
    """
    A factory to create JsonFormatter instances from dictconfig logging
    configurations.

    formatters:
      json:
        (): jsonlogging.json_formatter_factory
        format: my-app: {json}
        json_encoder:
          indent: 0
          separators: [", ", ": "]

    Customising the record template is not yet supported through this
    dictconfig factory.
    """
    encoder = json.JSONEncoder(**json_encoder)

    return WrapedJsonFormatter(format, encoder, default_record_adapter())
