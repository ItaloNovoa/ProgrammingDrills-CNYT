# ProgrammingDrills-CNYT

en este laboratorio procedemos a desarrollar algunos de los ProgrammingDrill propuestos en el capitulo 3 de libro quantum computing for computer scientists en el cual se explican la distribucion de probabilidad en el experimento de las rendijas

##### Programming Drill 3.1.1 
Write a program that performs our little marble experiment.
The program should allow the user to enter a Boolean matrix that describes the
ways that marbles move. Make sure that the matrix follows our requirement. The user
should also be permitted to enter a starting state of how many marbles are on each
vertex. Then the user enters how many time clicks she wants to proceed. The computer
should then calculate and output the state of the system after those time clicks.
We will make changes to this program later in the chapter.

##### Descripcion entrada:
- la primera entrada es un vector el cual describe el estado inicial del sistema
- la segunda entrada es una matriz que representa el flujo del sistema los 1´s tienen como significado True y los 0´s False
- la tercera entrada es un entero el cual se usa para votar el vector del sistema despues de n Click´s

~~~~
V=[6,2,1,5,3,10]
m1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
ProgamiNGDrill_3_1_1(V,m1,1)
~~~~

##### Programming Drill 3.2.1
Modify your program from Programming Drill 3.1.1 so that the entries in the matrices can be fractions as opposed to Boolean values.


##### Descripcion entrada:
- la primera entrada es un vector el cual describe el estado inicial del sistema
- la segunda entrada es una matriz que representa las probabilidades en el flujo del sistema (este ejercicio se puede desarrollar con el mismo metodo anterior debido a la representacion booleana con 1´s y 0´s)
- la tercera entrada es un entero el cual se usa para votar el vector del sistema despues de n Click´s

~~~~
V=[1/6,1/6,2/3]
m1=[[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]
ProgamiNGDrill_3_1_1(V,m1,1)
~~~~

##### Programming Drill 3.2.2
What would happen if there were more than two slits? Write a program that asks a user to design a multislit experiment. The user notes
the number of slits and the number of targets to measure the bullets. Then the user enters probabilities of the bullet´s moving from each slit to each target. An appropriate matrix is set up and then the matrix is multiplied by itself. Have the program print the
appropriate resulting matrix and vector.


##### Descripcion entrada:
- la primera entrada representa la cantidad de rendijas en el sistema
- la segunda entrada representa la cantidad de objetivos por rendija
- la tercera entrada es la cantidad de objetivos compartidos con la siguiente rendija
- la cuarta entrada es el vector incial del sistema
- la quinta entrada es un entero el cual se usa para votar el vector del sistema despues de n Click´s


#### Ejemplo del sistema mostrado en el ejemplo
![image](https://user-images.githubusercontent.com/42522754/65380439-44956e80-dca1-11e9-8610-d1eb275a1e3b.png)
##### Este sistema tiene 2 rendijas, 3 objetivos cada 1 y 1 objetivo compartido con la siguiente rendija


~~~~
#rendijas3_2_2(2,3,1,[1,0,0,0,0,0,0,0],1)
~~~~



# Pruebas
#### Al compilar el archivo automaticamente se ejecutan 15 pruebas que verifican todas las operaciones especificadas anteriormente.
#### para ejecutar el archivo matrices.py sigua las siguientes intrucciones:

1. Descargue el repositorio
~~~~
git clone https://github.com/ItaloNovoa/lab2-CNYT.git
~~~~
2. Ingrese al cmd/Terminal o simbolo del sistema
3. Ingresar a la carpeta de archivo 
4. digitar (Windows):
~~~~
python  Programming Drills.py 
~~~~ 
4.digitar (Ubuntu, Mac)
~~~~
python3 Programming Drills.py
~~~~
