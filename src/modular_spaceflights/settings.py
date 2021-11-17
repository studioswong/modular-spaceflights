"""Project settings."""
from modular_spaceflights.hooks import ProjectHooks

# Instantiate and list your project hooks here
HOOKS = (ProjectHooks(),)

# List the installed plugins for which to disable auto-registry
# DISABLE_HOOKS_FOR_PLUGINS = ("kedro-viz",)

from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore
from pathlib import Path
SESSION_STORE_CLASS = SQLiteStore

# Define keyword arguments to be passed to `SESSION_STORE_CLASS` constructor
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}

# Define custom context class. Defaults to `KedroContext`
# CONTEXT_CLASS = KedroContext

# Define the configuration folder. Defaults to `conf`
# CONF_ROOT = "conf"
