"""As a developer, I like the idea of literate/explorative programming. This is why I decided to use `nbdev` to create the matlon website, using a simple graph structure."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/95_model.ipynb.

# %% auto 0
__all__ = ['Project', 'load_projects', 'projects_to_dot', 'project_to_markdown']

# %% ../nbs/95_model.ipynb 3
from typing import ForwardRef
from pydantic import BaseModel
import json

# %% ../nbs/95_model.ipynb 4
Project = ForwardRef('Project')

class Project(BaseModel):
    """ Model for a project and the graph of related projects """
    title: str
    year_start: int
    year_end: int | None = None
    quote: str | None = None
    description: str | None = None
    related_project_titles: list[str] | None = None
    _related_projects: list[Project] | None = None

     # create a short_title method that returns method without spaces and without special characters, all in lowercase
    def short_title(self):
        return self.title.replace(" ", "-").lower()

# %% ../nbs/95_model.ipynb 5
def load_projects():
    # Load JSON data from projects.json
    with open('projects.json', 'r') as file:
        projects_data = json.load(file)

    # Instantiate Project objects
    projects = [Project(**data) for data in projects_data]
    projects_by_title = {project.title: project for project in projects}

    # Connect graph, load markdown files
    for project in projects:
        # if a file exists with the same name as the project and suffix .md, load it as the description
        try:
            with open(f'{project.short_title()}.md', 'r', encoding='utf-8') as file:
                project.description = file.read()
        except FileNotFoundError:
            pass
        project._related_projects = [projects_by_title[title] for title in project.related_project_titles] if project.related_project_titles else []

    return projects

# %% ../nbs/95_model.ipynb 6
def projects_to_dot(projects: list[Project]) -> str:
    dot = 'graph G {\n'
    for project in projects:
        dot += f'"{project.title}" [URL="andri.html#{project.short_title()}"]\n'
        for related_project in project._related_projects:
            dot += f'"{project.title}" -- "{related_project.title}"\n'
    dot += '}'
    return dot

# %% ../nbs/95_model.ipynb 7
def project_to_markdown(project: Project) -> str:
    markdown = f'## {project.title}\n'
    year_range = f'{project.year_start} - {project.year_end}' if project.year_end else f'{project.year_start} - '
    markdown += f'{year_range}\n\n'
    if project.quote:
        markdown += f'\n> {project.quote}\n\n'
    if project.description:
        markdown += f'{project.description}\n\n'
    if project._related_projects:
        markdown += '\n### Related projects\n'
        for related_project in project._related_projects:
            markdown += f'- [{related_project.title}](#{related_project.short_title()})\n'
    return markdown