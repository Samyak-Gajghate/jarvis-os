from backend.config.settings import settings


def validate_configuration() -> None:
    """Validate startup configuration."""

    assert settings.app_name
    assert settings.app_version