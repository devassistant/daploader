# -*- coding: utf-8 -*-
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from daploader import *


class TestDap(object):
    '''Tests for the Dap class'''
    def test_no_gz(self):
        '''Not-gzip archive should raise DapFileError'''
        with pytest.raises(DapFileError):
            Dap('test/bz2.dap')

    def test_no_exist(self):
        '''Nonexisting file should raise DapFileError'''
        with pytest.raises(DapFileError):
            Dap('foo')

    def test_no_meta(self):
        '''Dap without meta.yaml should raise DapMetaError'''
        with pytest.raises(DapMetaError):
            Dap('test/no_meta.dap')

    def test_dap_data(self):
        '''Dap should have correct content in meta, basename and files'''
        name = 'meta_only'
        basename = name + '.dap'
        dap = Dap('test/'+basename)
        assert dap.meta['package_name'] == 'foo'
        assert dap.meta['version'] == '1.0.0'
        assert u'Hrončok' in dap.meta['authors'][0]
        assert dap.basename == basename
        assert dap.files == [name, name + '/meta.yaml']
