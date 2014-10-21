import logging
import logging.config
import sys

from jsonlogging.formatters import JsonFormatter
from jsonlogging.tests import unittest


class TestJsonFormatterDictconfigFactory(unittest.TestCase):

    def get_dictconfig(self):
        """
        Get a dictConfig implementation. On Python 2.6 we use the
        implementation from the logutils library.
        """
        if not hasattr(logging.config, "dictConfig"):
            from logutils.dictconfig import dictConfig
            return dictConfig
        return logging.config.dictConfig

    def test_dictconfig_factory(self):

        conf = {
            "version": 1,
            "handlers": {
                "test-json-handler": {
                    "class": "logging.StreamHandler",
                    "formatter": "test-json-formatter",
                }
            },
            "formatters": {
                "test-json-formatter": {
                    "()": "jsonlogging.json_formatter_factory",
                    "format": "test: {json}",
                    "json_encoder": {
                        "indent": 2,
                        "separators": [" , ", " : "]
                    }
                }
            },
            "loggers": {
                __name__: {
                    "handlers": ["test-json-handler"]
                }
            }
        }

        dictConfig = self.get_dictconfig()
        dictConfig(conf)

        logger = logging.getLogger(__name__)
        handler = logger.handlers[0]
        self.assertEqual("test-json-handler", handler.name)

        formatter = handler.formatter
        self.assertIsInstance(formatter, JsonFormatter)

        self.assertEqual("test: {json}", formatter.get_format())

        self.assertEqual(2, formatter.get_encoder().indent)
        self.assertEqual(" , ", formatter.get_encoder().item_separator)
        self.assertEqual(" : ", formatter.get_encoder().key_separator)

