import os

from django.contrib.admin import register
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from core.services.jwt_service import JWTService, ActionToken, ActivateToken


class EmailService:
    @classmethod
    def __send_email(cls, to: str, template_name: str, context: dict, subject: str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(to=[to],
                                     subject=subject,
                                     from_email=os.environ.get("EMAIL_HOST_USER"),
                                     )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost/auth/activate/{token}'
        cls.__send_email(to=user.email,
                         template_name='register.html',
                         context={"name": user.profile.name, 'url': url},
                         subject="Register"
                         )

    @classmethod
    def report_ads(cls,ads):
        url = f'http://localhost/report_ads/{ads.id}'
        cls.__send_email(to=os.environ.get("EMAIL_HOST_USER"),
                         context={"url":url},
                         subject='report ads',
                         template_name='report_ads.html'

                         )