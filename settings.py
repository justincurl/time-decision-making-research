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

OTREE_ADMIN_PASSWORD = "markusprior"
OTREE_AUTH_LEVEL = "DEMO"

SESSION_CONFIGS = [
    dict(
        name="SliderCTB",
        display_name="Slider CTB",
        num_demo_participants=3,
        app_sequence=["Slider"],
        t_earliers="Today, Today, Today, Today, Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today",
        t_laters="8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today",
        payment_earliers="1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000",
        payment_laters="1000, 1250, 1500, 2000, 2500, 1000, 1250, 1500, 2000, 2500",
        num_sliders=10
    ),
    dict(
        name="oTimeCTB",
        display_name="oTime CTB",
        num_demo_participants=3,
        app_sequence=["simple_survey", "otime"],
    ),
    dict(
        name="HLandCTB",
        display_name="H&L and CTB",
        num_demo_participants=3,
        app_sequence=["CTB"],
    ),
    dict(
        name="PastFuture",
        display_name="Past & Future",
        num_demo_participants=3,
        app_sequence=["PastFuture"],
    ),
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
