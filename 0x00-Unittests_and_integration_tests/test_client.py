#!/usr/bin/env python3
"""Unittests for github org client
"""

from http import client
import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import *


class TestGithubOrgClient(unittest.TestCase):
    """ GitHubOrgClient tests """

    @parameterized.expand(
        [('google'), ('abc')]
    )
    @mock.patch('client.get_json', return_value={'test': 'one'})
    def test_org(self, name, json_result):
        """ tests org """
        client = GithubOrgClient(name)
        self.assertEqual(client.org, {'test': 'one'})
        json_result.assert_called_once()

    def test_public_repos_url(self):
        """ test _public_repos_irl """
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=mock.PropertyMock,
                        return_value={
                            'repos_url': [{'test': 'one'},
                                          {'test': 'two'}]}) as mock_test:
            test = GithubOrgClient('test')
            self.assertEqual(test._public_repos_url,
                             [{'test': 'one'}, {'test': 'two'}])
            mock_test.assert_called_once()

    @patch("client.get_json", return_value={'test': 'one'})
    def test_public_repos(self, get_json):
        """Test public repos function"""
        with mock.patch('client.GithubOrgClient.public_repos',
                        new_callable=mock.PropertyMock) as mock_test:
            mock_test.return_value = {"repos_url": "url"}
            testClass = GithubOrgClient("org_name")
            test = get_json()
            self.assertEqual(testClass.public_repos, {'repos_url': 'url'})
            mock_test.assert_called_once_with()
            get_json.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ tests has_license """
        test = GithubOrgClient('test')
        self.assertEqual(test.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Tests public_repos in an integration test """
    @classmethod
    def setUpClass(cls):
        """ sets up tests """
        from urllib.error import HTTPError
        cls.get_patcher = mock.patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ tears down tests """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
