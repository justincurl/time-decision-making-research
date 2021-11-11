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
        name="Slider_Full",
        display_name="Slider Full",
        num_demo_participants=3,
        app_sequence=["consent", "PastSlider", "demographics"],
        t_earliers="Today, Today, Today, Today, Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today",
        t_laters="8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today",
        payment_earliers="1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000",
        payment_laters="1000, 1250, 1500, 2000, 2500, 1000, 1250, 1500, 2000, 2500",
        num_sliders=10,
        randomize_sliders=False, 
        
    ), 
    dict(
        name="Slider_Only",
        display_name="Slider Only",
        num_demo_participants=3,
        app_sequence=["consent", "PastSlider"],
        t_earliers="Today, Today, Today, Today, Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today",
        t_laters="8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today",
        payment_earliers="1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000",
        payment_laters="1000, 1250, 1500, 2000, 2500, 1000, 1250, 1500, 2000, 2500",
        num_sliders=10,
        randomize_sliders=False
    ),
    dict(
        name="CTB_only",
        display_name="CTB Only", 
        num_demo_participants=3,
        app_sequence=["consent", "PastCTB"],
        CTB_left_values = "1, 2, 3, 4.5, 9, 1.5, 2.9, 4.4, 6.7, 12.9, 1.5, 2.5, 4.5, 8.1, 13.5", 
        CTB_right_values = "3, 3, 3, 3, 3, 4.4, 4.4, 4.4, 4.4, 4.4, 4.5, 4.5, 4.5, 4.5, 4.5",
        CTB_t_earliers="This Year, 1 Year from Now, 1 Year Ago",
        CTB_t_laters="1 Year from Now, 2 Years from Now, This Year",
        num_blocks=3,
        block_size=5,
        randomize_blocks=False
    ),
    dict(
        name="Slider_CTB",
        display_name="Slider then CTB",
        num_demo_participants=3,
        app_sequence=["consent", "PastSlider", "PastCTB", "demographics"],
        t_earliers="Today, Today, Today, Today, Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today",
        t_laters="8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 8 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today, 16 Weeks from Today",
        payment_earliers="1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000",
        payment_laters="1000, 1250, 1500, 2000, 2500, 1000, 1250, 1500, 2000, 2500",
        num_sliders=10,
        randomize_sliders=False,
        CTB_left_values = "1, 2, 3, 4.5, 9, 1.5, 2.9, 4.4, 6.7, 12.9, 1.5, 2.5, 4.5, 8.1, 13.5", 
        CTB_right_values = "3, 3, 3, 3, 3, 4.4, 4.4, 4.4, 4.4, 4.4, 4.5, 4.5, 4.5, 4.5, 4.5",
        CTB_t_earliers="This Year, 1 Year from Now, 1 Year Ago",
        CTB_t_laters="1 Year from Now, 2 Years from Now, This Year",
        num_blocks=3,
        block_size=5,
        randomize_blocks=False
    ),
    dict(
        name="Slider_CTB_Demo",
        display_name="Sliders and CTB 11.04 Demo",
        num_demo_participants=20,
        app_sequence=["consent", "PastCTB","FutureCTB", "FutureSlider", "PastSlider", "demographics"],
        past_t_earliers="1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago | 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago | 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago",
        past_t_laters="now, now, now, now, now, now | now, now, now, now, now, now | 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago",
        past_payment_laters="1000000, 1000000, 1000000, 1000000, 1000000, 1000000 | 1000000, 1000000, 1000000, 1000000, 1000000, 1000000 | 1000000, 1000000, 1000000, 1000000, 1000000, 1000000",
        past_payment_earliers="500000, 750000, 1000000, 1250000, 1500000, 1850000 | 500000, 750000, 1000000, 1250000, 1500000, 1850000 | 500000, 750000, 1000000, 1250000, 1500000, 1850000",
        past_t_options="5 years ago, 1 year ago, now",
        past_num_sliders=18,
        past_randomize_sliders=True,
        future_t_earliers="now, now, now, now, now, now | now, now, now, now, now, now | 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now",
        future_t_laters="1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now | 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now | 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now",
        future_payment_earliers="1000000, 1000000, 1000000, 1000000, 1000000, 1000000 | 1000000, 1000000, 1000000, 1000000, 1000000, 1000000 | 1000000, 1000000, 1000000, 1000000, 1000000, 1000000",
        future_payment_laters="500000, 750000, 1000000, 1250000, 1500000, 1850000 | 500000, 750000, 1000000, 1250000, 1500000, 1850000 | 500000, 750000, 1000000, 1250000, 1500000, 1850000",
        future_t_options="now, 1 year from now, 5 years from now",
        future_num_sliders=18,
        future_randomize_sliders=True,
        past_CTB_left_values = "1000000, 1000000, 1000000, 1500000, 1000000, 1000000, 1000000, 1000000, 1000000, 1500000, 1000000, 1000000, 1000000, 1000000, 1000000, 1500000, 1000000, 1000000",
        past_CTB_right_values = "500000, 750000, 1000000, 1250000, 1500000, 1850000, 500000, 750000, 1000000, 1250000, 1500000, 1850000, 500000, 750000, 1000000, 1250000, 1500000, 1850000",
        past_CTB_t_earliers="1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago, 5 years ago",
        past_CTB_t_laters="now, now, now, now, now, now, now, now, now, now, now, now, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago, 1 year ago",
        past_num_blocks=18,
        past_block_size=1,
        past_randomize_blocks=True,
        future_CTB_left_values = "1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000", 
        future_CTB_right_values = "1350000, 1500000, 1650000, 1800000, 1950000, 2100000, 1350000, 1500000, 1650000, 1800000, 1950000, 2100000, 1350000, 1500000, 1650000, 1800000, 1950000, 2100000",
        future_CTB_t_earliers="now, now, now, now, now, now, now, now, now, now, now, now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now",
        future_CTB_t_laters="1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 1 year from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now, 5 years from now",
        future_num_blocks=18,
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
