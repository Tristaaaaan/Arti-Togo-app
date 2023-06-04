from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from formulas import Formula
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from datastore import DataStore
from generateid import UserID
from database import Database
from generatepassw import Password

passw = Password()
database = Database()
generate = UserID()
datas = DataStore()
algorithm = Formula()


class ClickableTextField(MDRelativeLayout):
    password = StringProperty()


class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')

    def login(self):
        # If input are incomplete
        if self.ids.password.passw.text:

            if database.verifyAcc(self.ids.password.passw.text) is True:
                self.clear()
                self.manager.current = "second"
                self.manager.transition.direction = "left"
            else:
                self.error_dialog(message="The password is incorrect.")
                self.ids.password.passw.text = ''
        else:
            self.error_dialog(
                message="Make sure that username and password are not empty.")

    def clear(self):
        self.ids.user_id.text = ''
        self.ids.password.passw.text = ''

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
        )
        self.dialog.open()

    # Close Dialog
    def close_dialog(self, obj):
        self.dialog.dismiss()


class SecondWindow(Screen):

    Builder.load_file('secondwindow.kv')

    def menu(self):

        self.manager.current = "third"
        self.manager.transition.direction = "left"


class ThirdWindow(Screen):

    Builder.load_file('thirdwindow.kv')


class CoordonneeWindow(Screen):

    Builder.load_file('coordinatewindow.kv')

    def validate_coordinate(self):
        # Ha is optional fields, therefore if the user does not insert any value or values different from digits are inserted, the default value 0 is set.
        if not self.ids.ha.text.isdigit():
            self.ids.ha.text = '0'

        if not self.ids.e.text.isdigit():
            self.ids.e.text = '0'

        try:
            outputs = algorithm.calculate_coordinate(
                self.ids.deg.active,
                float(self.ids.xa.text),
                float(self.ids.ya.text),
                float(self.ids.ha.text),
                float(self.ids.aab.text),
                float(self.ids.dab.text),
                float(self.ids.e.text)
            )
            self.ids.xb.text = outputs[0]
            self.ids.yb.text = outputs[1]
            self.ids.hb.text = outputs[2]
        except:
            self.invalid_input()

    def invalid_input(self):
        close_button = MDFlatButton(
            text='CLOSE',
            text_color=[0, 0, 0, 1],
            on_release=self.close_dialog,
        )
        self.dialog = MDDialog(
            title='[color=#FF0000]Ooops![/color]',
            text='[color=#000000]There was an error processing your data. Please make sure to fill in all the required information correctly before proceeding to the next step. We appreciate your cooperation in ensuring a smooth experience. Thank you![/color]',
            size_hint=(0.85, None),
            radius=[20, 7, 20, 7],
            buttons=[close_button],
            auto_dismiss=False
        )
        self.dialog.open()

    # Close operation
    def close_dialog(self, *args):
        self.dialog.dismiss()


class DistanceWindow(Screen):

    Builder.load_file('distancewindow.kv')

    def validate_distance(self):
        try:
            outputs = algorithm.calculate_distance(
                self.ids.deg.active,
                float(self.ids.dab.text),
                float(self.ids.a.text),
                float(self.ids.b.text)
            )

            self.ids.dac.text = outputs[0]
            self.ids.dbc.text = outputs[1]
            self.c = outputs[2]

        except:
            CoordonneeWindow().invalid_input()


class ChengWindow1(Screen):

    Builder.load_file('chengwindow1.kv')

    def validate_change_step1(self):
        try:
            outputs = algorithm.calculate_change1(
                float(self.ids.pd.text),
                float(self.ids.pf.text),
                float(self.ids.pg.text),
            )
            self.ids.bcrk.text = str(outputs[0])
            self.ids.frk.text = str(outputs[1])

            datas.update_data_step1(
                self.ids.bcrk.text,
                self.ids.frk.text
            )

            self.manager.current = "cheng2"
            self.manager.transition.direction = "left"

        except:
            CoordonneeWindow().invalid_input()


class ChengWindow2(Screen):

    Builder.load_file('chengwindow2.kv')

    def validate_change_step2(self):
        try:
            outputs = algorithm.calculate_change2(
                float(self.ids.pd.text),
                float(self.ids.pf.text),
                float(self.ids.pg.text),
                int(datas.get_data_step1()[0]),
                int(datas.get_data_step1()[1])
            )
            self.ids.bcx1.text = str(outputs[0])
            self.ids.fx1.text = str(outputs[1])
            self.ids.bcrc1.text = str(outputs[2])
            self.ids.frc1.text = str(outputs[3])

            datas.update_data_step2(
                self.ids.bcx1.text,
                self.ids.fx1.text,
                self.ids.bcrc1.text,
                self.ids.frc1.text
            )
        except:
            CoordonneeWindow().invalid_input()


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()

    def on_start(self):

        datas.reset()
        if len(database.allAcc()) == 0:

            # Generate ID
            self.root.ids.first.user_id.text = generate.generate_id()

            # Generate Password
            self.user_password = passw.generate_passw(
                self.root.ids.first.user_id.text)
            print(self.user_password)
            # Status Log In
            self.status = 'no'
            # 5db7e9f51db - Password
            # Store Account
            database.storeAcc(self.root.ids.first.user_id.text,
                              self.user_password, self.status)

        else:
            self.root.ids.first.user_id.text = database.select_user()
        return super().on_start()


if __name__ == '__main__':
    rawApp().run()
