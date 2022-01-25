class PDFViews:
    def request(self) -> str:
        return "Can only view *.pdf files."


class XLSMaker:
    def specific_request(self) -> str:
        return "*.xls files"

# используется можественное наследование
class Adapter(PDFViews, XLSMaker):
    def request(self):
        return f"Remakes {self.specific_request()} on *.pdf files for PDFViews"


def client_code(views: "PDFViews"):
    print(views.request(), end="")


if __name__ == "__main__":

    view = PDFViews()
    client_code(view)
    print("\n")
    adapter = Adapter()
    client_code(adapter)
