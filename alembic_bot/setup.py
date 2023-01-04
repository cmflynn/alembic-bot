import setuptools


setuptools.setup(
    name="alembic_bot",
    url="https://github.com/cmflynn/alembic-bot",
    version="1.4",
    author="cmflynn, paunovic",
    package_dir={"": "src"},
    packages=["alembic_bot"],
    install_requires=["typer", "requests"],
    entry_points={"console_scripts": ["alembic-bot = alembic_bot.main:main"]},
)
