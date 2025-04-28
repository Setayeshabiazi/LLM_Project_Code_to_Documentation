                                              
                                  

from __future__ import annotations

import pytest
from pikepdf import Array, Dictionary, Name, NameTree, Pdf

from ocrmypdf._annots import remove_broken_goto_annotations


def test_remove_broken_goto_annotations(resources):
    with Pdf.open(resources / 'link.pdf') as pdf:
        assert not remove_broken_goto_annotations(pdf), "File should not be modified"

                                  
        nt = NameTree.new(pdf)
        names = pdf.Root[Name.Names] = pdf.make_indirect(Dictionary())
        names[Name.Dests] = nt.obj
                                           
        nt['Invalid'] = pdf.make_indirect(Dictionary())
                                          
        nt['Valid'] = Array([pdf.pages[0].obj, Name.XYZ, 0, 0, 0])

        pdf.pages[0].Annots[0].A.D = 'Missing'
        pdf.pages[1].Annots[0].A.D = 'Valid'

        assert remove_broken_goto_annotations(pdf), "File should be modified"

        assert Name.D not in pdf.pages[0].Annots[0].A
        assert Name.D in pdf.pages[1].Annots[0].A
