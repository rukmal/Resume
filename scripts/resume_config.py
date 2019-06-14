# Configuration file for Precis scripts
# See 'scripts/' folder for more

import os


class config():
    # Setting working directory to current directory
    os.chdir(os.path.abspath('.'))

    # Personal data json file
    data_json = '../personal_data.json'

    # Personal data RDF file
    data_rdf = '../personal_data.rdf'

    # Namespace for data
    data_namespace = 'http://precis.rukmal.me/ontology/weerawarana'

    # Curriculum Vitae
    #------------------
    # CV template configuration
    cv_template_config = '../curriculum_vitae/cv_prefs.yml'
    # CV LaTeX save location
    cv_tex_file = '../curriculum_vitae/Rukmal Weerawarana - Curriculum Vitae.tex'

    # Resume
    #-------
    # Resume template configuration
    resume_template_config = '../resume/resume_prefs.yml'
    # Resume LaTeX save location
    resume_tex_file = '../resume/Rukmal Weerawarana - Resume.tex'
