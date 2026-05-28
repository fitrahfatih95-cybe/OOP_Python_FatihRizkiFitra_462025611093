class Campus:
    name = ''
    district = ''

    def greetings(self,name):
        print(f'perkenalan {name},nama kampus kami adalah {self.name},alamatnya di {self.district}')

class Student:
    name = ''
    nim = ''
    study_program = ''


Campus1 = Campus()
Campus1.name = 'Universitas Darussalam'
Campus1.district = 'Siman, Ponorogo, Jawa Timur, Indonesia'
Campus1.greetings ('fatihrizki')