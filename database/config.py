import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/testdb"
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


class DockerDevConfig(Config):

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/testdb"
    DEBUG = True


config = {"dev": DevelopmentConfig, "prod": ProductionConfig, "docker": DockerDevConfig}
