from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
    mturk_hit_settings=dict(
        keywords="bonus, study",
        title="Title for your experiment",
        description="Description for your experiment",
        frame_height=500,
        template="global/mturk_template.html",
        minutes_allotted_per_assignment=60,
        expiration_hours=7 * 24,
        qualification_requirements=[]
        # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
    ),
)

OTREE_AUTH_LEVEL = "DEMO"

SESSION_CONFIGS = [
    dict(
        name="Full_Survey",
        display_name="Full Survey",
        num_demo_participants=20,
        app_sequence=["consent", "App1", "App2", "ict", "demographics"],
        vs_on=1,
        past_t_earliers="1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago | 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago | 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago",
        past_t_laters="now, now, now, now, now | now, now, now, now, now | 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago",
        past_payment_laters="500000, 500000, 500000, 500000, 500000 | 500000, 500000, 500000, 500000, 500000 | 500000, 500000, 500000, 500000, 500000",
        past_payment_earliers="122500, 378000, 500000, 617500, 875000 | 127000, 371000, 500000, 629000, 880500 | 120000, 378000, 500000, 628000, 880500",
        past_t_options="5 years ago, 1 year ago, now",
        past_num_sliders=15,
        past_randomize_sliders=True,
        future_t_earliers="now, now, now, now, now | now, now, now, now, now | 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now",
        future_t_laters="1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now | 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now | 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now",
        future_payment_earliers="500000, 500000, 500000, 500000, 500000 | 500000, 500000, 500000, 500000, 500000 | 500000, 500000, 500000, 500000, 500000",
        future_payment_laters="122500, 378000, 500000, 617500, 875000 | 127000, 371000, 500000, 629000, 880500 | 120000, 378000, 500000, 628000, 880500",
        future_t_options="now, 1 year from now, 5 years from now",
        future_num_sliders=15,
        future_randomize_sliders=True,
        past_grid_left_values = "500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000",
        past_grid_right_values = "122500, 378000, 500000, 617500, 875000, 127000, 371000, 500000, 629000, 880500, 120000, 378000, 500000, 628000, 880500",
        past_grid_t_earliers="1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago",
        past_grid_t_laters="now, now, now, now, now, now, now, now, now, now, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago",
        past_num_blocks=15,
        past_block_size=1,
        past_randomize_blocks=True,
        future_grid_left_values = "500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000", 
        future_grid_right_values = "122500, 378000, 500000, 617500, 875000, 127000, 371000, 500000, 629000, 880500, 120000, 378000, 500000, 628000, 880500",
        future_grid_t_earliers="now, now, now, now, now, now, now, now, now, now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now",
        future_grid_t_laters="1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now",
        future_num_blocks=15,
        future_block_size=1,
        future_randomize_blocks=True,
    ),
    dict(
        name="App2",
        display_name="App 2",
        num_demo_participants=20,
        app_sequence=["App2", "demographics"]
    ),
    dict(
        name="Demographics",
        display_name="demographics",
        num_demo_participants=20,
        app_sequence=["demographics"],
        future_grid_left_values = "500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000", 
        future_grid_right_values = "122500, 378000, 500000, 617500, 875000, 127000, 371000, 500000, 629000, 880500, 120000, 378000, 500000, 628000, 880500",
        future_grid_t_earliers="now, now, now, now, now, now, now, now, now, now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now",
        future_grid_t_laters="1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now",
        future_num_blocks=15,
        future_block_size=1,
        future_randomize_blocks=True,
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = False

ROOMS = [
    dict(
        name="markusroom",
        display_name="Professor Prior's Room",
        participant_label_file="_rooms/prior.txt",
    ),
    dict(name="live_demo", display_name="Room for live demo (no participant labels)"),
]

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = "xb_4%4j75ymz+gb468yyjn^3rumxo7ap3363wc4u87-vtcwd@a"

INSTALLED_APPS = ["otree"]
