import configparser


config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_admin_page_url():
        return config.get("admin login info", "admin_page_url")

    @staticmethod
    def get_admin_username():
        return config.get("admin login info", "admin_username")

    @staticmethod
    def get_invalid_admin_username():
        return config.get("admin login info", "invalid_admin_username")

    @staticmethod
    def get_admin_password():
        return config.get("admin login info", "admin_password")
        