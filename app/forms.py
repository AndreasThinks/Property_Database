from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, IntegerField
from wtforms.validators import Required, length


class LoginForm(Form):
    username = TextField('Username', validators = [Required()])
    password = PasswordField('password', validators = [Required()])

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)


class LostReport(Form):
    description = TextField('Description')
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    finderTel = TextField('Telephone Number')
    finderAddress = TextField('Loser Address')
    finderEmail = TextField('Loser Email')
    finderPostcode = TextField('Loser Postcode')
    itemType = TextField('Item Type')
    itemColour = TextField('Item Colour')
    streetFound = TextField('Street Found')
    postcode = TextField('Postcode')
    borough = TextField('Borough')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LostReport, self).__init__(*args, **kwargs)


class FoundReport(Form):
    description = TextField('Description')
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    finderTel = TextField('Telephone Number')
    finderAddress = TextField('Loser Address')
    finderEmail = TextField('Loser Email')
    finderPostcode = TextField('Loser Postcode')
    finderPolice = BooleanField('Police Staff')
    itemType = TextField('Item Type')
    itemColour = TextField('Item Colour')
    streetFound = TextField('Street Found')
    postcode = TextField('Postcode')
    borough = TextField('Borough')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LostReport, self).__init__(*args, **kwargs)

