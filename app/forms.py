from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('username', [
        validators.DataRequired()
    ])

    password = PasswordField('password', [
        validators.DataRequired()
    ])

class RegForm(Form):
    username = StringField('username', [
        validators.DataRequired(),
        validators.Length(min=3, max=25, message='Username must be between 3 and 25 characters long')
    ])

    password = PasswordField('password', [
        validators.DataRequired(),
        validators.Length(min=4, message='Minimal password length is 4 characters'),
        validators.EqualTo('confirm', message='Passwords don\'t match')
    ])

    confirm = PasswordField('repeat password')