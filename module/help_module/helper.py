
class Helper:
    def url_extration(self, str):
        return str.split("/url?q=", 1)[1].split("&sa", 1)[0]
