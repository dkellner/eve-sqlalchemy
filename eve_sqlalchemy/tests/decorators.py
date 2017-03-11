# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from eve_sqlalchemy.tests.test_settings import SQLALCHEMY_DATABASE_URI
from eve_sqlalchemy.tests.test_sql_tables import Base, Contacts


class TestRegisterSchema(TestCase):

    def setUp(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(engine)
        self._session = sessionmaker(bind=engine)()

    def test_default_is_not_unset(self):
        contact = Contacts(ref='test_default_is_not_unset')
        self._session.add(contact)
        self._session.flush()
        self.assertIsNotNone(contact._created)
        self.assertEqual(contact.title, 'Mr.')
