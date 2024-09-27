# Bienvenido al Módulo: Sistemas Dinámicos

En este proyecto se abordo la evolución temporal de sistemas cuánticos utilizando el método numérico de Runge-Kutta de orden cuatro (RK4). El objetivo es resolver ecuaciones diferenciales que describen la dinámicoa temporal de un sitema de matrices, en particular para problemas en los que la función de evolución no tiene una dependencia explícita del tiempo.

El problema a resolver sigue la ecuación diferencial:

$$
\frac{dy}{dt} = f(t,y)
$$

Con la condición inicial \(y(t_0) = y_o\). Para este caso, la función de evolución es de la forma:

$$
f(t, y) = -i[0, y(t)]
$$

donde (O) es el operador cuántico y y(t) es el estado cuántico en el tiempo (t). El objetivo es resolver esta ecuación diferencial numéricamente utilizando el método RK4, un método preciso y estable para la integración numérica de ecuaciones diferenciales.
