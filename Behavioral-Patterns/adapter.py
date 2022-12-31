class Target:

    def request(self) -> str:
        return "Target: The default target's behavior"

class Adaptee:

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):

    def request(self):
        return f"Adapter: (TRANSLATE) {self.specific_request()[::-1]}"

def client_code(target: Target):

    print(target.request(), end="")


if __name__ == '__main__':
    print("Client: I can work just fine with the Target objects: ")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    adapter = Adapter()
    client_code(adapter)
