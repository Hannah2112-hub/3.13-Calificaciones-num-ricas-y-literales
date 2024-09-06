class alumno:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def evaluar_calificacion(self):
        if self.calificacion > 9.0:
            return "La calificación es A."
        elif self.calificacion > 8.0:
            return "La calificación es B."
        elif self.calificacion >= 7.5:
            return "La calificación es C."
        else:
            return "La calificación es R."

calificacion = float(input("Ingrese la calificación: "))
Alumno = alumno(calificacion)

print(Alumno.evaluar_calificacion())


