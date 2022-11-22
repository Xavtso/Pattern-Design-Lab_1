import unittest
from Lab3 import *


class ProjectTest(unittest.TestCase):

    def test_web_creation(self):
        pr = Web()
        assert pr.team is not None

    def test_mobile_creation(self):
        pr = Mobile()
        assert pr.team is not None

    def test_embedded_creation(self):
        pr = Embedded()
        assert pr.team is not None


class AssignmentTest(unittest.TestCase):
    def test_assignment(self):
        pr = Web(limit=3)
        person = Employee(PersonalInfo("Vitaliy Havrona"))
        pr.add_employee(person)
        assert person in pr.team.member_list
        assert pr in person.projects

    def test_unassignment(self):
        pr = Web(limit=3)
        person = Employee(PersonalInfo("Vitaliy Havrona"))
        pr.add_employee(person)
        pr.remove_employee(person)
        assert person not in pr.team.member_list
        assert pr not in person.projects


class SoftwareArchitectTest(unittest.TestCase):
    def test_fill_project(self):
        pr = Web(limit=5)
        sa = WebArchitect(PersonalInfo("Vitaliy Havrona"), [pr])
        person = Employee(PersonalInfo("Vitaliy Havrona"))
        team = Team(pr.id, [person])
        sa.fill_project(team, pr)
        assert pr.team == team

    def test_create_project(self):
        sa = WebArchitect(PersonalInfo("Vitaliy Havrona"), [])
        pr = sa.create_project(title="title1", domain="google.com")
        assert pr.domain == "google.com"


if __name__ == '__main__':
    unittest.main()