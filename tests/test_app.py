# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
import unittest

# import the app's classes and objects
from application import app, db
from application.models import ToDo

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test2.db",
                SECRET_KEY='mister11',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        sample1 = ToDo(id=1, task="sleeping", completed=False)
        # save users to database
        db.session.add(sample1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('thome'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sleeping', response.data)

    def test_delete(self):
        response = self.client.get(url_for('deleting', id=1))
        follow_redirects=True
        self.assertNotIn(b'sleeping', response.data)

    def test_edit(self):
        response = self.client.post('edit/1', 
        data=dict(
            task='ntask',
            completed=False
        ), 
        follow_redirects=True)
        self.assertIn(b'ntask', response.data)

    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertIn(b'sleeping', response.data)