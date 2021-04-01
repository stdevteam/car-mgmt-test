from django.utils.translation import gettext_lazy as _

TRANSMISSION = (
    ("automatic", _("Automatic")),
    ("manual", _("Manual"))
)

SEATS = (
    # The material of seats.
    ("leather", _("Leather")),
    ("textile", _("Textile"))
)

CATEGORIES = (
    ("small", _("Small Cars")),  # suitable for carrying up to 4 people
    ("family", _("Family Cars")),  # suitable for carrying up to 7 adults
    ("van", ("Van"))  # Bigger cars
)
