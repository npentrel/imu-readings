import app
import imu

from events.input import Buttons, BUTTON_TYPES


class ExampleApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.acc_read = None

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()
        else:
            self.acc_read = imu.acc_read()

    def draw(self, ctx):
        ctx.save()
        ctx.rgb(0.2,0,0).rectangle(-120,-120,240,240).fill()
        if self.acc_read:
            ctx.rgb(1,0,0).move_to(-80,-40).text("accel x,y,z:\n{},\n{},\n{}".format(self.acc_read[0], self.acc_read[1], self.acc_read[2]))
        else:
            ctx.rgb(1,0,0).move_to(-80,0).text("no readings yet")
        ctx.restore()

__app_export__ = ExampleApp
