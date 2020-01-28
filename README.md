WIP

The project uses `pipenv` and its dependencies are in Pipfile. Pipenv's official page is unsecure at the moment, please refer to this page for more info:
`https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used`

How it works:

`./manage.py getthedocs` -- writes all hosted projects info from `https://readthedocs.org/api/v2/project/` to database.


`./manage.py scrapethedocs.py` -- crawls the saved projects pages
