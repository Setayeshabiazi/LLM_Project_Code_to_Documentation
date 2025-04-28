                                              
                                  

from __future__ import annotations

from ocrmypdf.helpers import check_pdf


def test_pdf_error(resources):
    assert check_pdf(resources / 'blank.pdf')
    assert not check_pdf(__file__)
