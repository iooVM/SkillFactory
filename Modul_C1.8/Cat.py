class Cat:
    def __init__(self, name='x3',sex = 'Devochka',age = '0'):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age




if __name__ == '__main__':
    cat1 = Cat()
    cat1.set_name('tom')
    cat1.set_sex('malchik')
    cat1.set_age(15)
    print(cat1.get_name())
    print(cat1.get_sex())
    print(cat1.get_age())



