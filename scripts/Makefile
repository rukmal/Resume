.DEFAULT_GOAL := help


# Build recipes
###############

.PHONY: build_cv_from_json
build_cv_from_json: ## Build CV LaTeX and PDF from the personal data JSON file
	python build_data_rdf.py && \
		python build_cv.py && \
		pdflatex -output-directory ../curriculum_vitae ../curriculum_vitae/Rukmal\ Weerawarana\ -\ Curriculum\ Vitae.tex

.PHONY: build_resume_from_json
build_resume_from_json: ## Build resume LaTeX and PDF from the personal data JSON file
	python build_data_rdf.py && \
		python build_resume.py && \
		pdflatex -output-directory ../resume ../resume/Rukmal\ Weerawarana\ -\ Resume.tex

.PHONY: build_data_rdf
build_data_rdf: ## Build personal data RDF from the personal data JSON file
	python build_data_rdf.py


# Util
#######

.PHONY: help
help: # See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
