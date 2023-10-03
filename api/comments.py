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
from utils.rest_client import RestClient


class Comments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Class for comments endpoint
        """
        cls.url_comments = "https://api.todoist.com/rest/v2/comments"
        cls.session = requests.Session()
        cls.task_id = TodoBase().get_all_tasks().json()[1]["id"]

    def test_get_all_comments(self):
        """
        Test to get all comments
        :return:
        """
        task_id = self.task_id
        url_get_all_comments = f"{self.url_comments}?task_id={task_id}"
        response = RestClient().send_request("get", session=self.session,
                                             headers=HEADERS, url=url_get_all_comments)
        assert response.status_code == 200

    def test_create_comment(self):
        """
        Test to create comment
        :return:
        """
        data = {
            "id": self.task_id,
            "content": "Comment for task"
        }

        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_comments, data=data)
        assert response.status_code == 200

    def test_update_comment_on_task(self):
        data = {
            "content": ""
        }

        response = RestClient().send_request("post", session=self.session, headers=HEADERS)
        assert response.status_code == 200

    def test_delete_comment_on_task(self):

        response = RestClient().send_request("delete", session=self.session, headers=HEADERS)
        assert response.status_code == 204



