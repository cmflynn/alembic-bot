use in a github action like so: 
```yaml

name: Alembic Bot

on:
  push:
    branches:
      - main

jobs:
  alembic_bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Setup Git config
        run: |
          git config user.name "Alembic Bot"
          git config user.email "alembicbot@drivewealth.tech"
          git config pull.rebase false

      - name: Fetch main
        run: git fetch --depth=1 origin +refs/heads/main

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9

      - name: Install libs
        run: pip install requests

      - name: Run script
        run: python ./tools/alembic_bot.py
        env:
          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
          REPOSITORY: DriveWealth/drivedigital
          MASTER_BRANCH: main

```