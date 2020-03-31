from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS=dict(
        real_world_currency_per_point=1.00, 
        participation_fee=0.00, doc="", 
        mturk_hit_settings = dict(
            keywords='bonus, study',
            title='Title for your experiment',
            description='Description for your experiment',
            frame_height=500,
            template='global/mturk_template.html',
            minutes_allotted_per_assignment=60,
            expiration_hours=7 * 24,
            qualification_requirements=[]
            # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
        )
    )

OTREE_ADMIN_PASSWORD="markusprior"
OTREE_AUTH_LEVEL="DEMO"

SESSION_CONFIGS = [
    dict(
        name='econ',
        display_name='Econ CTB',
        num_demo_participants=3, 
        app_sequence=['otime']
    ),
    dict(
        name='politics',
        display_name='Political CTB',
        num_demo_participants=3,
        app_sequence=['opolitics']
    ),
    dict(
        name='public_goods',
        display_name='Trust',
        num_demo_participants=3,
        app_sequence=['trust'] 
    ),
    dict(
        name='cournot',
        display_name='Cournot',
        num_demo_participants=3,
        app_sequence=['cournot']
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='markusroom',
        display_name="Professor Prior's Room",
        participant_label_file='_rooms/prior.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'xb_4%4j75ymz+gb468yyjn^3rumxo7ap3363wc4u87-vtcwd@a'

INSTALLED_APPS = ['otree']

