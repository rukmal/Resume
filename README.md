# Resume

My personal Resume and CV.

Built with [Precis](https://precis.rukmal.me).


<p align="center">

|[Click here to view my Resume](https://github.com/rukmal/Resume/blob/gh-pages/resume/Rukmal%20Weerawarana%20-%20Resume.pdf)|
|:--:|

|[Click here to view my CV](https://github.com/rukmal/Resume/blob/gh-pages/curriculum_vitae/Rukmal%20Weerawarana%20-%20Curriculum%20Vitae.pdf)|
|:--:|

</p>


## Artifact Builds

All builds (RDF, LaTeX, PDF) are handled by GitHub Actions [automations](.github/workflows/), and are not to be done manually. Local copies of these files are ignored in `.gitignore`, and are force added by the [`commit-artifacts`](.github/workflows/commit-artifacts.yml) workflow job.

## Local Development

Recipes for building locally are in [`scripts/Makefile`](scripts/Makefile).

```bash
$ make -C scripts

build_cv_from_json             Build CV LaTeX and PDF from the personal data JSON file
build_data_rdf                 Build personal data RDF from the personal data JSON file
build_resume_from_json         Build resume LaTeX and PDF from the personal data JSON file
```

## Contact

This is an open source project released under the [MIT License](LICENSE). Contact me if you want to suggest an improvement, or fork and send a pull request!

https://rukmal.me
