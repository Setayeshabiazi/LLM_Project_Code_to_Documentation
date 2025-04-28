                                              
                                  

"""OCRmyPDF PDF annotation cleanup."""

from __future__ import annotations

import logging

from pikepdf import Dictionary, Name, NameTree, Pdf

log = logging.getLogger(__name__)


def remove_broken_goto_annotations(pdf: Pdf) -> bool:
           
    modified = False

                                               
    if Name.Names not in pdf.Root:
        return modified
    if Name.Dests not in pdf.Root[Name.Names]:
        return modified

    dests = pdf.Root[Name.Names][Name.Dests]
    if not isinstance(dests, Dictionary):
        return modified
    nametree = NameTree(dests)

                                            
    names = set(k for k in nametree.keys())

    for n, page in enumerate(pdf.pages):
        if Name.Annots not in page:
            continue
        for annot in page[Name.Annots]:
            if not isinstance(annot, Dictionary):
                continue
            if Name.A not in annot or Name.D not in annot[Name.A]:
                continue
                                                                       
            named_destination = str(annot[Name.A][Name.D])
            if named_destination not in names:
                                                                            
                                                                               
                                                
                log.warning(
                    f"Disabling a hyperlink annotation on page {n + 1} to a "
                    "non-existent named destination "
                    f"{named_destination}."
                )
                del annot[Name.A][Name.D]
                modified = True

    return modified
