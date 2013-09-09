# Settings for running tests: test runners, in-memory database definitions, log settings

from .settings import *

# TEST SETTINGS
TEST_RUNNER = "discover_runner.DiscoverRunner"
TEST_DISCOVER_TOP_LEVEL = BASE_DIR
TEST_DISCOVER_ROOT = BASE_DIR
TEST_DISCOVER_PATTERN = "test*.py"

# IN-MEMORY TEST DATABASE

DATABASES = {
    "default":
    {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
