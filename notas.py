# dado una nota y un porcentaje de asistencia, devuelve aprobadi True or False
# condiciones: nota de esmane >= 70 y asistencia >= 80
# TODO: recoger las notas de un csv

# recoger: nota y asistencia
#   - usamos input para recoger los datos 
score = input("introduce la nota del examen (de 0 a 100): ")
assistance = input("Introduce la asistencia de 0 a 100 sin %: ")
#   - convertir nota y asistencia a int
score = int(score)
assistance = int(assistance)

# asigno True o False a aprobado en base a las condiciones

if score >= 70 and assistance >= 80:
    print("Has aprobado")
else:
    print("Ponte a estudiar para Julio")