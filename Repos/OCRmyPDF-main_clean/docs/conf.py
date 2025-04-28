                      
                                              
                                       

                  

                                                             
                                                
 
                                                                
                 
 
                                                                     
                     
 
                                                                        
                            

                                                                               
                                                                             
                                                                               
 
           
            
                                          

                                                                           

needs_sphinx = '8'

import datetime

                                                                     
                                                                     
       
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.imgconverter',                                                 
    'sphinx_issues',
]

myst_enable_extensions = ['colon_fence', 'attrs_block', 'attrs_inline', 'substitution']

                    
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
napoleon_use_rtype = False
issues_github_path = "ocrmypdf/OCRmyPDF"

                                                                        
templates_path = ['_templates']

                                     
source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown', '.txt': 'markdown'}

                              
master_doc = 'index'

                                        
project = 'ocrmypdf'

year = str(datetime.date.today().year)
copyright = (
    f'{year}, James R. Barlow. '
    + 'Licensed under Creative Commons Attribution-ShareAlike 4.0'
)
author = 'James R. Barlow'

                                                                              
                                                                           
                  
 
                        

import os
from importlib.metadata import version as package_version

on_rtd = os.environ.get('READTHEDOCS') == 'True'

if on_rtd:
                                                                           
    import sys
    from unittest.mock import MagicMock

    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            return MagicMock()

    MOCK_MODULES = [
        'pikepdf',
        'pikepdf.canvas',
        'pikepdf.models',
        'pikepdf.models.metadata',
    ]
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


                                                 
release = package_version('ocrmypdf')
version = '.'.join(release.split('.')[:2])


                                                                          
                                    
 
                                                                       
                                                                   
language = 'en'

                                                                            
                                   
 
            
 
                                                            
 
today_fmt = '%Y-%m-%d'

                                                                      
                                                      
                                                                   
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

                                                                     
            
 
                     

                                                                     
 
                                 

                                                                       
                                      
 
                         

                                                                         
                                      
 
                      

                                                              
pygments_style = 'sphinx'

                                                      
                             

                                                                               
                       

                                                                           
todo_include_todos = False


                                                                           

import sphinx_rtd_theme              

                                                                           
                           
 
html_theme = 'sphinx_rtd_theme'

                                                                             
                                                                   
                
 
html_theme_options = {}

                                                                            
                      

                                            
                                                  
 
                              

                                                                             
 
                         

                                                                            
                 
 
                                            

                                                                               
                                                                                
               
 
                     

                                                                             
                                                                             
                                                                         
                                

                                                                      
                                                                     
                                            
 
                      

                                                                       
                                          
                                                
 
                              

                                                                   
                                   
 
                             

                                                                  
 
                    

                                                                           
                 
 
                            

                                         
 
                            

                                  
 
                       

                                                                    
 
                          

                                                            
 
                             

                                                                               
 
                         

                                                                            
 
                            

                                                                            
                                                                             
                                                  
 
                          

                                                              
                         

                                                                     
                                          
                                                       
                                                 
 
                             

                                                                              
                              
                                                      
 
                                           

                                                                              
                                                                         
 
                                  

                                              
htmlhelp_basename = 'ocrmypdfdoc'

                                                                           

latex_elements = {                
                                                  
     
                                 
                                               
     
                          
                                              
     
                     
                                    
     
                             
}

                                                             
                                         
                                                        
latex_documents = [
    (master_doc, 'ocrmypdf.tex', 'ocrmypdf Documentation', 'James R. Barlow', 'manual')
]

                                                                               
                 
 
                   

                                                                            
               
 
                         

                                                     
 
                             

                                                   
 
                         

                                                    
 
                       

                                                                            
                                                                              
           
 
                                   

                                         
 
                             


                                                                           

                                           
                                                                  
man_pages = [(master_doc, 'ocrmypdf', 'ocrmypdf Documentation', [author], 1)]

                                                   
 
                       


                                                                           

                                                               
                                                 
                                         
texinfo_documents = [
    (
        master_doc,
        'ocrmypdf',
        'ocrmypdf Documentation',
        author,
        'ocrmypdf',
        'One line description of project.',
        'Miscellaneous',
    )
]

                                                    
 
                         

                                         
 
                               

                                                              
 
                                

                                                                  
 
                               
