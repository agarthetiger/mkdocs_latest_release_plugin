from mkdocs.plugins import BasePlugin
from git import Git, Repo
from jinja2 import Template, DebugUndefined

import re

class GitLatestTagPlugin(BasePlugin):

    def __init__(self):
        self.g = Git()


    def on_page_markdown(self, markdown, page, config, files):
        latest_git_tag = self.get_latest_version(page.file.abs_src_path)
        t = Template(markdown, undefined=DebugUndefined)
        return t.render({'git_latest_version': latest_git_tag})

    def get_latest_version(self, page_path):
        """
        Function to get the latest tag from the git repository which matches
        the configured regex for the version tag format.
        :param page_path:
        :return: String with the highest semver tag, returns "unknown" if not found.
        """
        default_version = "v0.1.0"

        self.r = Repo(page_path,search_parent_directories=True)
        assert not self.r.bare

        self.tags = self.r.tags
        self.matching_tags = {}

        for tag in self.tags:
            if isinstance(re.search("v\d+\.\d+\.\d+", tag), MatchObject):
                self.matching_tags.add(tag)

        if len(self.matching_tags) > 0:
            return self.matching_tags[0]
        else:
            return "unknown"
