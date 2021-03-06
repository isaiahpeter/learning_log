#!/usr/bin/env python

# test_errcodes.py - unit test for psycopg2.errcodes module
#
# Copyright (C) 2015-2019 Daniele Varrazzo  <daniele.varrazzo@gmail.com>
# Copyright (C) 2020-2021 The Psycopg Team
#
# psycopg2 is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In addition, as a special exception, the copyright holders give
# permission to link this program with the OpenSSL library (or with
# modified versions of OpenSSL that use the same license as OpenSSL),
# and distribute linked combinations including the two.
#
# You must obey the GNU Lesser General Public License in all respects for
# all of the code used other than OpenSSL.
#
# psycopg2 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

import unittest
from .testutils import ConnectingTestCase, slow, reload

from threading import Thread
from psycopg2 import errorcodes


class ErrocodeTests(ConnectingTestCase):
    @slow
    def test_lookup_threadsafe(self):

        # Increase if it does not fail with KeyError
        MAX_CYCLES = 2000

        errs = []

        def f(pg_code='40001'):
            try:
                errorcodes.lookup(pg_code)
            except Exception as e:
                errs.append(e)

        for __ in range(MAX_CYCLES):
            reload(errorcodes)
            (t1, t2) = (Thread(target=f), Thread(target=f))
            (t1.start(), t2.start())
            (t1.join(), t2.join())

            if errs:
                self.fail(
                    "raised {} errors in {} cycles (first is {} {})".format(
                        len(errs), MAX_CYCLES,
                        errs[0].__class__.__name__, errs[0]))

    def test_ambiguous_names(self):
        self.assertEqual(
            errorcodes.lookup('2F004'), "READING_SQL_DATA_NOT_PERMITTED")
        self.assertEqual(
            errorcodes.lookup('38004'), "READING_SQL_DATA_NOT_PERMITTED")
        self.assertEqual(errorcodes.READING_SQL_DATA_NOT_PERMITTED, '38004')
        self.assertEqual(errorcodes.READING_SQL_DATA_NOT_PERMITTED_, '2F004')


def test_suite():
    return unittest.TestLoader().loadTestsFromName(__name__)


if __name__ == "__main__":
    unittest.main()
