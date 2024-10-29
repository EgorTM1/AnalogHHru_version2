class Settings:
    @property
    def DB_URL(self):
        return f"sqlite+aiosqlite:///FastAPIHHru2.db"
    

settings = Settings()
