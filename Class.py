class Hero:
    name = None
    abyliti = None


class Hero_super(Hero):
    def __str__(self,):
        return

    def pr_name(self, name):
        self.name = name
        name = 'SuperMan'
        print(f' {name} it is super_hero')

