class Config:
    '''
    Parent configuration class that will hold universal configurations
    for the project irregadless of the environment
    '''
    
    MOVIE_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProductionConfig(Config):
    '''
    Production configuration class that holds configurations for the production environment. It inherits the configuration properties of the config class

    Args:
        1. Config: Parent class with universal configuration
    '''
    pass


class DevelopmentConfig(Config):
    '''
    Development configuration class that holds configurations for the Development environment. It inherits the configuration properties of the config class

    Args:
        1. Config: Parent class with universal configuration
    '''

    DEBUG = True
