# Contributing to Mopipe

## Development Environment

Ensure you have an environment with Python 3.9-3.11 installed.

This project uses [`hatch`](https://hatch.pypa.io/latest/) for development. To install `hatch`:

```console
pip install hatch
```

To create a development environment for this project:

```console
hatch env create
```

This will create the default environment specified in `pyproject.toml` under the `[tool.hatch.envs]` section. To activate the environment:

```console
hatch shell
```

## Testing

This project uses [`pytest`](https://docs.pytest.org/en/stable/) for testing. To run the tests:

```console
hatch run test
```

All the tests are located in the [`tests/`](https://github.com/au-imclab/mopipe/tree/dev/tests) directory.

## Linting

This project uses [`black`](https://black.readthedocs.io/en/stable/index.html) and [`ruff`](https://docs.astral.sh/ruff/) for linting. To run the linters:

```console
hatch -e lint run all
```

In addition, this will run [`mypy`](https://mypy.readthedocs.io/en/stable/) for type checking.

## Documentation

This project uses [`mkdocs`](https://www.mkdocs.org/) for documentation. To generate documentation from latest code:

```console
hatch -e docs run gen-docs
hatch -e docs run html-docs
```

This will generate documentation in the `docs/` directory. This will be published to [https://au-imclab.github.io/mopipe/](https://au-imclab.github.io/mopipe/).

## Continuous Integration

This project uses Github Actions and Workflows to automate:

- Tests
- Linting
- Type Checking
- Realeasing
- Publishing to PyPI

If tests or linting fail, PRs will not be accepted.

The workflows can be seen in the [`.github/workflows/`](https://github.com/au-imclab/mopipe/tree/dev/.github/workflows) directory.

## Releasing and Versioning

Each commit to `main` will trigger a release with the commit hash as a pre-release.

To release a new version, update the version number in `src/__about__.py`, and commit it with a PR to `main`. Once the PR is merged, a tag with the version number will be created, and a release will be triggered.

To create the tag, you will need to run:

```console
git tag -a v<version> -m "v<version>"
git push --tags
```

## Development Workflow

This project uses the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). It's easy to follow so please refer to the their documentation.

Essentially, the `main` branch is the stable branch, and the `dev` branch is the development branch. All development should be done on the `dev` branch, and PRs should be made to `dev`. Once the PR is merged, the `main` branch will be updated with the new changes if the feature is ready for release.

The only differnce here is that `main` will also contain pre-releases, as we make packages from the tags on `main`.
