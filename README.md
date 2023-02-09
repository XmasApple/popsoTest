# Installation

```bash
pip -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd popsoTestAdmin
python manage.py collectstatic
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

##### Don't forget to change `popsoTestAdmin/popsoTestAdmin/main/tg_parser/config.py` to your own settings

# DEMO
![DEMO](demo.gif)