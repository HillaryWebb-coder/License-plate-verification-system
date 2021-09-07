from django.apps import AppConfig


class LicensePlateRecognitionConfig(AppConfig):
    name = 'license_plate_recognition'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import license_plate_recognition.signals