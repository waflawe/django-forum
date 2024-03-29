from services.schemora.settings import include_setting
from services.schemora.src.datastructures import ValidationClasses
from services.user_settings_handlers import TimezoneHandler, AvatarHandler, SignatureHandler
from error_messages.home_error_messages import Settings

# Переменная со всеми настройками пользователя.
settings = (
    include_setting(field="timezone", error_code=3, error_message=Settings.INVALID_TIMEZONE, handler=TimezoneHandler),
    include_setting(field="avatar", error_code=1, error_message=Settings.INVALID_AVATAR, handler=AvatarHandler,
                    validation_classes=ValidationClasses("UploadAvatarForm", "UserAvatarSerializer")),
    include_setting(field="signature", error_code=2, error_message=Settings.INVALID_SIGNATURE, handler=SignatureHandler,
                    validation_classes=ValidationClasses("ChangeSignatureForm", "SignatureSerializer"))
)
