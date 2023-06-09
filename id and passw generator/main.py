from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
import pyperclip
from kivymd.uix.button import MDFlatButton
from generateid import UserID
from generatepassw import Password
from kivymd.uix.dialog import MDDialog
passw = Password()
uid = UserID()


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


class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')

    def generate(self):
        self.ids.generated.md_bg_color = [1, 1, 1, 1]

        try:
            if self.ids.user_id.text != '':

                user_id = self.ids.user_id.text

                self.ids.user_password.text = passw.generate_passw(user_id)

                self.ids.generated.text = 'Password has been generated.'
                self.ids.generated.md_bg_color = [152/255, 251/255, 152/255, 1]

                Clock.schedule_once(self.generated_label, 3)
            else:
                self.error_dialog("Kindly enter a User ID.")
        except:
            pass

    def generated_label(self, dt):
        self.ids.generated.md_bg_color = (1, 1, 1, 1)
        self.ids.generated.text = ''

    def clear(self):
        self.ids.user_id.text = ''
        self.ids.user_password.text = ''

    def copy(self):
        self.ids.generated.md_bg_color = [1, 1, 1, 1]
        if self.ids.user_password.text != '':
            userpassw = "User Password: " + self.ids.user_password.text

            pyperclip.copy(userpassw)

            self.ids.generated.text = 'Password has been copied.'

            self.ids.generated.md_bg_color = [255/255, 253/255, 156/255, 1]

            Clock.schedule_once(self.generated_label, 3)
        else:
            self.error_dialog("There is no text to be copied.")

    def error_dialog(self, message):

        close_button = MDFlatButton(
            text='CLOSE',
            text_color=[0, 0, 0, 1],
            on_release=self.close_dialog,
        )
        self.dialog = MDDialog(
            title='[color=#FF0000]Ooops![/color]',
            text=message,
            buttons=[close_button],
            auto_dismiss=False
        )
        self.dialog.open()

    # Close Dialog
    def close_dialog(self, obj):
        self.dialog.dismiss()


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
