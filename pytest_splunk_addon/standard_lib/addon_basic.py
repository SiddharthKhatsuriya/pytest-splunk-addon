import pytest
import splunklib.client as client
from splunk_appinspect import App
import logging


class Basic():
    logger = logging.getLogger()

    # This test ensures the contained samples will produce at lease one event per sourcetype
    @pytest.mark.splunk_addon_searchtime
    def test_basic_sourcetypes(self, splunk_search_util, sourcetypes):

        self.logger.debug("Testing sourcetype={}", sourcetypes)
        search = "search (index=_internal OR index=*) AND sourcetype=\"{}\"".format(sourcetypes)

        # run search
        result = splunk_search_util .checkQueryCountIsGreaterThanZero(
            search,
            interval=1, retries=20)

        if not result:
            pytest.fail(search)

    # This test ensures the contained samples will produce at lease one event per eventtype
    @pytest.mark.splunk_addon_searchtime
    def test_basic_eventtype(self, splunk_search_util, eventtypes):

        self.logger.debug("Testing eventtype={}", eventtypes)
        search = "search (index=_internal OR index=*) AND eventtype=\"{}\"".format(eventtypes)

        # run search
        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=1, retries=20)

        if not result:
            pytest.fail(search)

    @pytest.mark.splunk_addon_searchtime
    def test_fields(self, splunk_search_util, prop_elements):
        search = "search (index=_internal OR index=*) AND sourcetype=\"{}\" AND {}".format(
            prop_elements['sourcetype'],
            prop_elements['field']
        )

        # run search
        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=1, retries=10)

        if not result:
            pytest.fail(search)
