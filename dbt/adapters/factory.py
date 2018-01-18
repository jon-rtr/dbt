from dbt.logger import GLOBAL_LOGGER as logger  # noqa

from dbt.lazy_import import lazy_import

import dbt.exceptions


lazy_import(globals(), """
from dbt.adapters.postgres import PostgresAdapter
from dbt.adapters.redshift import RedshiftAdapter
from dbt.adapters.snowflake import SnowflakeAdapter
from dbt.adapters.bigquery import BigQueryAdapter
""")


adapters = {
    'postgres': 'PostgresAdapter',
    'redshift': 'RedshiftAdapter',
    'snowflake': 'SnowflakeAdapter',
    'bigquery': 'BigQueryAdapter'
}


def get_adapter_by_name(adapter_name):
    adapter = adapters.get(adapter_name, None)

    if adapter is None:
        message = "Invalid adapter type {}! Must be one of {}"
        adapter_names = ", ".join(adapters.keys())
        formatted_message = message.format(adapter_name, adapter_names)
        raise dbt.exceptions.RuntimeException(formatted_message)

    else:
        return globals()[adapter]


def get_adapter(profile):
    adapter_type = profile.get('type', None)
    return get_adapter_by_name(adapter_type)
