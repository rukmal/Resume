# Script to build the RDF file from my personal data JSON

from context import precis
from resume_config import config


def buildPersonalDataRDF():
    # Opening json file
    f = open(config.data_json, 'r')

    # Instantiating loader
    loader = precis.Loader(ingest_file=f, namespace=config.data_namespace)

    # Saving completed ontology to file
    loader.saveToFile(save_location=config.data_rdf)

if __name__ == '__main__':
    buildPersonalDataRDF()
