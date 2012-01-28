from registration.backends.default import DefaultBackend
from registration.forms import ReCaptchaRegistrationForm

class RecaptchaRegistrationBackend(DefaultBackend):
    def get_form_class(self, request):
        return ReCaptchaRegistrationForm
