#!usr/bin/env python3
"""Project tasks."""

DOIT_CONFIG = {'default_tasks': ['html']}


def task_html():
    """Build documentation-html for project."""
    return {
        'actions': ['sphinx-build -M html ./doc/ ./doc/_build']
    }

def task_gitclean():
    """Clean untracked files."""
    return {
            'actions': ['git clean -xdf'],
    }

def task_test():
    """Test application."""
    yield {
            'actions': ['pytest'], 'name': "any_tests",
            'verbosity': 2
    }
    # yield {
    #         'actions': ['pytest ...'], 'name': "specific_test_N",
    #         'verbosity': 2
    # }
    
def task_docstyle():
    """Check docstrings in src code files."""
    return {
            'actions': ['pydocstyle ./src'],
            'verbosity': 2
    }

def task_check():
    """Perform all checks."""
    return {
            'actions': [],
            'task_dep': ['docstyle', 'test']
    }