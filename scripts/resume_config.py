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
