class student:
    name = "" 
    family = ""
    id = ""
    age = ""
    def show_data(self):
        print(f"Name = {self.name}, Family = {self.family}")

student2 = student()
student2.name = "AmirAli"
student2.family = "Rahimian"
student2.age = "20"
student2.id = "2"


student1 = student()
student1.name = "Hanieh"
student1.family = "Rezaei"
student1.age = "Amir age - 1"
student1.id = "1"




student1.show_data()
student2.show_data()