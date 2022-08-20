


class idea:
    def idea_display(Self):
        print("WELCOME TO IDEA")

class vodafone:
    def vodafone(self):
        print("WELCOME TO VODAFONE")

class VI(idea,vodafone):
    def display(self):
        self.idea_display()
        self.vodafone()
        print("welcome to VI - 2022")

vi=VI()
vi.display()