#! /bin/bash

cd /home/codeformiami/Dropbox/mia-councilmatic
/home/codeformiami/Dropbox/mia-councilmatic/venv/lib/python3.4/python manage.py loaddata >> /tmp/miamidade-loaddata.log 2>&1
/home/codeformiami/Dropbox/mia-councilmatic/venv/lib/python3.4/python manage.py fixdata >> /tmp/miamidade-loaddata.log 2>&1
/home/codeformiami/Dropbox/mia-councilmatic/venv/lib/python3.4/python manage.py update_index --age=24
