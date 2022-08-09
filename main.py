def on_forever():
    led.plot_bar_graph(pins.analog_read_pin(AnalogPin.P0), 255)
    basic.pause(10)
basic.forever(on_forever)
