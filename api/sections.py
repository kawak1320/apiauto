"""
(c) Copyright Jalasoft. 2023

projects.py
    configuration of logger file
"""
import logging
import unittest

import requests

from api.todo_base import TodoBase
from config.config import HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class Sections(unittest.TestCase):
    """
    Class for sessions endpoint
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Class only executed one time
        :return:
        """
        cls.url_section = "https://api.todoist.com/rest/v2/sections"
        cls.session = requests.Session()

        cls.project_id = TodoBase().get_all_projects().json()[1]["id"]

    def test_create_session(self):
        """
        Test to create session
        :return:
        """
        data = {
            "project_id": self.project_id,
            "name": "Section 2"
        }
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_section, data=data)
        assert response.status_code == 200

    def test_get_all_sections(self):
        """
        Test to get all sessions
        :return:
        """
        response = TodoBase().get_all_sections()
        LOGGER.info("Number of sections returned: %s", len(response.json()))
        assert response.status_code == 200

    def test_get_all_sections_by_project(self):
        """
        Test to get all sessions by project id
        :return:
        """
        if self.project_id:
            url_section = f"{self.url_section}?project_id={self.project_id}"

        response = RestClient().send_request("get", session=self.session, headers=HEADERS,
                                             url=url_section)
        LOGGER.info("Number of sections returned: %s", len(response.json()))
        assert response.status_code == 200

    def test_get_section(self):
        """
        Test to get session
        :return:
        """
        response = TodoBase().get_all_sections()
        section_id = response.json()[0]["id"]
        LOGGER.info("Section Id: %s", section_id)
        url_section = f"{self.url_section}/{section_id}"
        response = RestClient().send_request("get", session=self.session, headers=HEADERS,
                                             url=url_section)
        assert response.status_code == 200

    # ToDo: Improve this method, once i fix the issue with nose2
    def test_update_session(self):
        """
        Test to update session
        :return:
        """
        session_created = self.create_session("Session 2")
        session_id_update = session_created["body"]["id"]
        url = f"{self.url_base}/{session_id_update}"
        data = {
            "name": "Session 2 Updated",
            "color": "red"
        }
        response = RestClient().send_request("post", session=self.session, url=url,
                                             headers=HEADERS, data=data)
        assert response.status_code == 200

        # ToDo: Finish this incomplete method, once i fix the issue with nose2
        def test_delete_session(self):
            """
            Test to delete session
            :return:
            """
            response = RestClient().send_request("delete", session=self.session, url=url,
                                                 headers=HEADERS, data=data)
            assert response.status_code == 204
