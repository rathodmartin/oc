# encoding: utf-8
# Copyright (C) 2002-2011, Stefan Schwarzer <sschwarzer@sschwarzer.net>
# See the file LICENSE for licensing terms.

import ftplib
import unittest

from ftputil import ftp_error


class TestFTPErrorArguments(unittest.TestCase):

    def test_bytestring_argument(self):
        # An umlaut as latin-1 character
        os_error = ftp_error.FTPOSError("\xe4")

    def test_unicode_argument(self):
        # An umlaut as unicode character
        io_error = ftp_error.FTPIOError(u"\xe4")


class TestTryWithFTPError(unittest.TestCase):

    def callee(self):
        raise ftplib.error_perm()

    def test_try_with_oserror(self):
        "Ensure the `ftplib` exception isn't used as `FTPOSError` argument."
        try:
            ftp_error._try_with_oserror(self.callee)
        except ftp_error.FTPOSError, exc:
            self.assertFalse(exc.args and
                             isinstance(exc.args[0], ftplib.error_perm))
        else:
            # We shouldn't come here.
            self.assertTrue(False)

    def test_try_with_ioerror(self):
        "Ensure the `ftplib` exception isn't used as `FTPIOError` argument."
        try:
            ftp_error._try_with_ioerror(self.callee)
        except ftp_error.FTPIOError, exc:
            self.assertFalse(exc.args and
                             isinstance(exc.args[0], ftplib.error_perm))
        else:
            # We shouldn't come here.
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
