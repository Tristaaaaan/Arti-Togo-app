from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from database import Database
from pwd_generator import Password
from kivy.properties import StringProperty
from generateid import UserID

generateid = UserID()
password_generate = Password()
db = Database()


class RectangularElevationButton(
    ButtonBehavior,
    RectangularRippleBehavior,
    CommonElevationBehavior,
    BackgroundColorBehavior,
):
    '''
    This class implements custom button with shadow
    '''
    pass


class LoginPage(Screen):

    def on_kv_post(self, base_widget):
        if len(db.allAcc()) == 0:
            self.user_id.text = generateid.generate_id()
        else:
            self.user_password.passw.disabled = True
            self.user_id.text = db.get_acc()[0]
            self.user_password.passw.text = db.get_acc()[1]

            Clock.schedule_once(lambda dt: self.login_delayed(), 5)

        return super().on_kv_post(base_widget)

    def login_delayed(self):
        self.login(self.user_id.text, self.user_password.passw.text)

    def login(self, username, password):

        if self.check_password(username, password):
            app = MDApp.get_running_app()
            app.root.current = 'Accueil'
        else:
            self.ids.error_label.text = 'Incorrect password.'
            self.ids.error_label.md_bg_color = (254/255, 219/255, 223/255, 1)
            self.ids.user_password.text = ''

            Clock.schedule_once(self.reset_error_label_bg_color, 3)

    def reset_error_label_bg_color(self, dt):
        self.ids.error_label.md_bg_color = (1, 1, 1, 1)
        self.ids.error_label.text = ''

    def check_password(self, username, password):
        if len(db.allAcc()) == 0:

            self.user_password = password_generate.generate_passw(username)

            # Status Log In
            if self.user_password == password:
                db.storeAcc(self.ids.user_id.text,
                            self.user_password)
                return True

        else:
            # Generate
            self.user_password = password_generate.generate_passw(username)
            if self.user_password == password:

                return True
