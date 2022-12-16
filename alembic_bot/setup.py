import setuptools


setuptools.setup(
    name="alembic_bot",
    version="1.1",
    author="cmflynn, paunovic",
    package_dir={"": "src"},
    packages=["alembic_bot"],
    install_requires=["typer", "requests"],
    entry_points={"console_scripts": ["alembic-bot = alembic_bot.main:main"]},
)
