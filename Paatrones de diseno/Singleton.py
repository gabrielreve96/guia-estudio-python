class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Uso del Singleton
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True, ambas variables apuntan a la misma instancia
