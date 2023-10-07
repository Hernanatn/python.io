from googleapiclient.discovery import build, Resource
from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials as SA_Credentials
from overloading import overload

class Singleton(type):
    __instancias : dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instancias:
            cls.__instancias[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instancias[cls]

class Recurso(metaclass=Singleton):
    __nombreApi : str = None
    __recursoSubyacente : Resource = None

    @property
    def recurso(self):
        return type(self).__recursoSubyacente

class AdministradorAPI(metaclass=Singleton):
    
    GOOGLE_APIS : dict  = \
    {
        'drive'     :
        {
            'version'   :   'v3',
            'alcances'  :
            [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/documents',
                'https://www.googleapis.com/auth/drive'
            ]
        },
        'docs'      :
        {
            'version'   :   'v1',
            'alcances'  :
            [
                'https://www.googleapis.com/auth/documents',
                'https://www.googleapis.com/auth/drive'
            ]
        },
        'sheets'    :
        {
            'version'   :   'v4',
            'alcances'  :
            [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        },
        'gmail'     :       
        {
            'version'   :   'v1',
            'alcances'  :
            [
                'https://www.googleapis.com/auth/gmail.send',
                'https://mail.google.com'
            ]
        },        
        'calendar'  :
        {
            'version'   :   'v3',
            'alcances'  :
            [
                'https://www.googleapis.com/auth/calendar'
            ]
        },
    }

    Drive           : str   = 'drive'
    Documentos      : str   = 'docs'
    HojasCalculo    : str   = 'sheets'
    Correo          : str   = 'gmail'
    Calendario      : str   = 'calendar'

    def __init__(self, rutaCredenciales : str):
        self.__rutaCredenciales = rutaCredenciales

    @classmethod
    def __montarCredenciales(cls, nombreApi : str) -> Credentials:
        return SA_Credentials.from_service_account_file(filename = self.__rutaCredenciales, scopes = AdministradorAPI.GOOGLE_APIS[nombreApi]['alcances'])

    @classmethod
    def __crearTipoRecurso(cls,nombreApi,**nominales):
        return type\
        (
            name    = nombreApi,
            bases   = (Recurso,),
            dict    = \
            {
                '__init__' : lambda self, nombreApi, **nominales : setattr\
                (
                    type( self ),
                    "__recursoSubyacente",
                    build\
                    (
                        serviceName = nombreApi,
                        version     = cls.GOOGLE_APIS[nombreApi]['version'],
                        credentials = cls.__montarCredenciales(nombreApi),
                        **nominales
                    )
                ),
            }
        )


    @classmethod
    def crearRecurso(cls,nombreApi : str,**nominales) -> Recurso:
        tipo : Recurso = cls.__crearTipoRecurso(nombreApi)(nombreApi)
        match nombreApi:
            case AdministradorAPI.Drive:
                return tipo
            case AdministradorAPI.HojasCalculo:
                return tipo.spreadsheets()
            case AdministradorAPI.Documentos:
                return tipo.documents()
            case AdministradorAPI.Correo:
                return tipo
            case AdministradorAPI.Calendario:
                return tipo
            case _:
                raise TypeError(f"Ud. trató de crear un recurso para una API no soportada {nombreApi}. \n Las APIs soportadas son: 'drive','docs','sheets','gmail' y 'calendar'. Para más información revise la documentación.")