                     
                                              
                                            

"""Run the OCRmyPDF web service."""

import os
import sys

try:
    import streamlit              
except ImportError:
    raise ImportError(
        'You need to install streamlit in the Python environment '
        'to run the web service.\n'
    )

if __name__ == '__main__':
    os.execvp(
        sys.executable,
        [
            sys.executable,
            '-m',
            'streamlit',
            'run',
            'misc/_webservice.py',
            *sys.argv[1:],
        ],
    )
