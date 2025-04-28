                                              
                                  

from __future__ import annotations

import logging

from ocrmypdf._pipelines._common import configure_debug_logging


def test_debug_logging(tmp_path):
                                                          
                                                                                    
    prefix = 'test_debug_logging'
    log = logging.getLogger(prefix)
    _handler, remover = configure_debug_logging(tmp_path / 'test.log', prefix)
    log.info("test message")
    remover()
