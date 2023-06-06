from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from database import Database
from pwd_generator import Password

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

    def login(self, username, password):
        if self.check_password(username, password):
            app = MDApp.get_running_app()
            app.root.current = 'Accueil'
        else:
            self.ids.error_label.text = 'Incorrect User ID or Password.'
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
            # Generate Password
            self.user_password = password_generate.generate_passw(username)
            if self.user_password == password:

                return True
