import importlib

import View.SignupScreen.signup_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SignupScreen.signup_screen)


def do_verfy_field(inst):
    if inst.text == '':
        inst.error = True
        return False, inst.text
    elif inst.error:
        print(inst.error)
        return False, inst.text
    else:
        return True, inst.text


def do_verify_pwd(inst):
    input4, pwd = do_verfy_field(inst.pwd)
    input5, pwd2 = do_verfy_field(inst.pwd2)
    if input5 and input4:
        if pwd == pwd2:
            return True, pwd
        else:
            inst.pwd.error = True
            return False, pwd
    return False, pwd


class SignupScreenController:
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.signup_screen.SignupScreenModel
        self.view = View.SignupScreen.signup_screen.SignupScreenView(controller=self, model=self.model)

    def get_view(self) -> View.SignupScreen.signup_screen:
        return self.view

    def do_signup(self):
        inst = self.view.ids

        input1, first_name = do_verfy_field(inst.first_name)
        input2, last_name = do_verfy_field(inst.last_name)
        input3, email = do_verfy_field(inst.email)
        input4, pwd = do_verify_pwd(inst)

        if input1 and input2 and input3 and input4:
            print(first_name, last_name, email, pwd)
            self.model.first_name = first_name
            self.model.last_name = last_name
            self.model.email = email
            self.model.password = pwd

            self.model.do_signup()
