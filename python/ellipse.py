import numpy as np 

class Ellipse():

    @staticmethod
    def normTangent(theta, a, b):
        r = Ellipse.normPolar(theta, a, b)
        rp = Ellipse.normDerivative(theta, a, b)
        return np.sqrt(r**2 + rp**2)

    @staticmethod
    def chord(theta_1, theta_2, a, b):
        r_1_x = Ellipse.coordinateX(theta_1, a, b)
        r_1_y = Ellipse.coordinateY(theta_1, a, b)
        r_2_x = Ellipse.coordinateX(theta_2, a, b)
        r_2_y = Ellipse.coordinateY(theta_2, a, b)
        chord = np.sqrt((r_1_x - r_2_x)**2 + (r_1_y - r_2_y)**2)
        return chord

    @staticmethod
    def normDerivative(theta, a, b):
        aux = Ellipse._aux(theta, a, b)
        return -a*b*(a**2 - b**2)*np.sin(theta)*np.cos(theta)/np.sqrt(aux**3)

    @staticmethod
    def coordinateX(theta, a, b):
        return Ellipse.normPolar(theta, a, b)*np.cos(theta)

    @staticmethod
    def coordinateY(theta, a, b):
        return Ellipse.normPolar(theta, a, b)*np.sin(theta)

    @staticmethod
    def normPolar(theta, a, b):
        aux = Ellipse._aux(theta, a, b)
        return a*b/np.sqrt(aux)
        
    @staticmethod
    def _aux(theta, a, b):
        return  (a*np.sin(theta))**2 + (b*np.cos(theta))**2
    
    @staticmethod
    def perimeter(a, b):
        h = (a - b)**2/(a + b)**2
        p = np.pi*(a + b)*(1.0 + 3.0*h/(10.0 + np.sqrt(4.0 - 3.0*h)))
        return p
