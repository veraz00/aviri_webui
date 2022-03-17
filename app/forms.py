from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError, HiddenField, BooleanField, PasswordField, RadioField
from wtforms.validators import DataRequired, Email, Length, Optional, URL
from decimal import ROUND_HALF_UP

class LoginForm(FlaskForm):
    username = StringField('Name', validators = [DataRequired(), Length(1, 30)])
    password = PasswordField('Password', validators = [DataRequired(), Length(1, 128)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('login')

# class PredictionForm(FlaskForm):
#     result = StringField('Result', validators = [DataRequired(), Length(1)])
#     probability0 = DecimalField('Probability0', validators = [DataRequired()], places=2, rounding=ROUND_HALF_UP)
#     probability1 = DecimalField('Probability1', validators = [DataRequired()], places=2, rounding=ROUND_HALF_UP)

class PredictionForm(FlaskForm):
    image_id = StringField('Image_ID', validators = [DataRequired(), Length(20, 50)])
    model_name = RadioField('Model_name', choices=[('VI'), ('VI_Moderated')])
    submit = SubmitField('Predict')