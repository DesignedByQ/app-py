# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import ToDo

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
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

#class TestViews(TestBase):
    def test_delete(self):
        response = self.client.delete(url_for('deleting'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'sleeping', response.data)