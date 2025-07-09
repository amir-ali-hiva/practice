names = ["حمید","Ehsan","Omid","Henieh","Zahra","Golnosh","Milad","Mohammad","Alireza","Amir Ali","♥Alireza2♥","M.j","Amir","Ali","Erfun"]

new_names = list(map(lambda x: f"♥{x}♥\n", names))

file = open("name.txt", "w" , encoding="utf-8")

file.writelines(new_names)
file.close