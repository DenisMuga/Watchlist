# from distutils.debug import DEBUG




class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_KEY = '2c046c049b4d576ef5dbf27cfbd26cf4'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
        Args: The parent configuration class with general configuration settings
    '''
    
    DEBUG = True
    
    
    