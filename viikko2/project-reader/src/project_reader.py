from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        dictionary = toml.loads(content)
        name = dictionary["tool"]["poetry"]["name"]
        description = dictionary["tool"]["poetry"]["description"]
        license = dictionary["tool"]["poetry"]["license"]
        authors = list(dictionary["tool"]["poetry"]["authors"])
        dependencies = list(dictionary["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(dictionary["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())


        return Project(name, description, license, authors, dependencies, dev_dependencies)
