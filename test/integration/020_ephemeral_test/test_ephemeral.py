from nose.plugins.attrib import attr
from test.integration.base import DBTIntegrationTest


class TestEphemeral(DBTIntegrationTest):

    def setUp(self):
        pass

    @property
    def schema(self):
        return "ephemeral_020"

    @property
    def models(self):
        return "test/integration/020_ephemeral_test/models"

    @attr(type='postgres')
    def test__postgres(self):
        self.use_profile('postgres')
        self.use_default_project()
        self.run_sql_file("test/integration/020_ephemeral_test/seed.sql")

        self.run_dbt()

        self.assertTablesEqual("seed", "dependent")
        self.assertTablesEqual("seed", "double_dependent")

    @attr(type='snowflake')
    def test__snowflake(self):
        self.use_profile('snowflake')
        self.use_default_project()
        self.run_sql_file("test/integration/020_ephemeral_test/seed.sql")

        self.run_dbt()

        self.assertTablesEqual("SEED", "dependent")
        self.assertTablesEqual("SEED", "double_dependent")
