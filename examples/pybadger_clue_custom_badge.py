""""""

from adafruit_pybadger import pybadger

pybadger.badge_background(background_color=pybadger.WHITE, rectangle_color=pybadger.PURPLE,
                          rectangle_drop=0.2, rectangle_height=0.6)

pybadger.badge_line(text="@blinka", color=pybadger.BLINKA_PURPLE, scale=4, padding_above=1)
pybadger.badge_line(text="Blinka", color=pybadger.WHITE, scale=5, padding_above=2)
pybadger.badge_line(text="CircuitPython", color=pybadger.WHITE, scale=3, padding_above=1)
pybadger.badge_line(text="she/her", color=pybadger.BLINKA_PINK, scale=4, padding_above=4)

pybadger.show()

while True:
    if pybadger.button.a:
        pybadger.show()

    if pybadger.button.b:
        pybadger.show_qr_code()
