from context import precis
from owlready2 import default_world, get_ontology
from resume_config import config
import os


def buildCV():
    # Importing CV template
    cv_template = precis.templating.PrecisTemplate(
        template_folder=os.path.join(precis.config.templates_folder,
                                     'curriculum_vitae/')
    )

    # Loading user ontology
    user_ont = get_ontology(config.data_rdf).load()

    # Casting to RDFLib graph
    user_graph = default_world.as_rdflib_graph()

    # Loading user peferences (for template)
    user_prefs = open(config.cv_template_config, 'r')

    # Instantiating template driver
    driver = precis.templating.TemplateDriver(
        template=cv_template,
        user_ont=user_ont,
        user_graph=user_graph,
        user_prefs=user_prefs
    )

    with open(config.cv_tex_file, 'w') as f:
        f.write(driver.buildTemplate())


if __name__ == '__main__':
    buildCV()
