# Copyright (C) 2003-2012, Stefan Schwarzer <sschwarzer@sschwarzer.net>
# See the file LICENSE for licensing terms.

import ftplib
import unittest

import ftputil
from ftputil import ftp_error

from test import mock_ftplib
from test import test_base


class FailingFTPHost(ftputil.FTPHost):
    def _dir(self, path):
        raise ftp_error.FTPOSError("simulate a failure, e. g. timeout")


# Mock session, used for testing an inaccessible login directory
class SessionWithInaccessibleLoginDirectory(mock_ftplib.MockSession):
    def cwd(self, dir):
        # Assume that `dir` is the inaccessible login directory.
        raise ftplib.error_perm("can't change into this directory")


class TestPath(unittest.TestCase):
    """Test operations in `FTPHost.path`."""

    def test_regular_isdir_isfile_islink(self):
        """Test regular `FTPHost._Path.isdir/isfile/islink`."""
        testdir = '/home/sschwarzer'
        host = test_base.ftp_host_factory()
        host.chdir(testdir)
        # Test a path which isn't there
        self.assertFalse(host.path.isdir('notthere'))
        self.assertFalse(host.path.isfile('notthere'))
        self.assertFalse(host.path.islink('notthere'))
        #  This checks additional code (see ticket #66).
        self.assertFalse(host.path.isdir('/notthere/notthere'))
        self.assertFalse(host.path.isfile('/notthere/notthere'))
        self.assertFalse(host.path.islink('/notthere/notthere'))
        # Test a directory
        self.assertTrue(host.path.isdir(testdir))
        self.assertFalse(host.path.isfile(testdir))
        self.assertFalse(host.path.islink(testdir))
        # Test a file
        testfile = '/home/sschwarzer/index.html'
        self.assertFalse(host.path.isdir(testfile))
        self.assertTrue(host.path.isfile(testfile))
        self.assertFalse(host.path.islink(testfile))
        # Test a link
        testlink = '/home/sschwarzer/osup'
        self.assertFalse(host.path.isdir(testlink))
        self.assertFalse(host.path.isfile(testlink))
        self.assertTrue(host.path.islink(testlink))

    def test_workaround_for_spaces(self):
        """Test whether the workaround for space-containing paths is used."""
        testdir = '/home/sschwarzer'
        host = test_base.ftp_host_factory()
        host.chdir(testdir)
        # Test a file name containing spaces
        testfile = '/home/dir with spaces/file with spaces'
        self.assertFalse(host.path.isdir(testfile))
        self.assertTrue(host.path.isfile(testfile))
        self.assertFalse(host.path.islink(testfile))

    def test_inaccessible_home_directory_and_whitespace_workaround(self):
        "Test combination of inaccessible home directory + whitespace in path."
        host = test_base.ftp_host_factory(
               session_factory=SessionWithInaccessibleLoginDirectory)
        self.assertRaises(ftp_error.InaccessibleLoginDirError,
                          host._dir, '/home dir')

    def test_abnormal_isdir_isfile_islink(self):
        """Test abnormal `FTPHost._Path.isdir/isfile/islink`."""
        testdir = '/home/sschwarzer'
        host = test_base.ftp_host_factory(ftp_host_class=FailingFTPHost)
        host.chdir(testdir)
        # Test a path which isn't there
        self.assertRaises(ftp_error.FTPOSError, host.path.isdir, "index.html")
        self.assertRaises(ftp_error.FTPOSError, host.path.isfile, "index.html")
        self.assertRaises(ftp_error.FTPOSError, host.path.islink, "index.html")

    def test_exists(self):
        """Test if "abnormal" FTP errors come through `path.exists`."""
        # Regular use of `exists`
        testdir = '/home/sschwarzer'
        host = test_base.ftp_host_factory()
        host.chdir(testdir)
        self.assertEqual(host.path.exists("index.html"), True)
        self.assertEqual(host.path.exists("notthere"), False)
        # "Abnormal" failure
        host = test_base.ftp_host_factory(ftp_host_class=FailingFTPHost)
        self.assertRaises(ftp_error.FTPOSError, host.path.exists, "index.html")


if __name__ == '__main__':
    unittest.main()

