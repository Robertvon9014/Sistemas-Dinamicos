# Explicación

Esta parte de la documentación del proyecto se enfoca en una comprensión más profunda de los **sistemas dinámicos** y cómo los resolvemos numéricamente utilizando el método **Runge-Kutta de cuarto orden (RK4)**.

## Sistemas dinámicos

Los sistemas dinámicos son modelos de gran importancia en diversas ciencias. Un modelo dinámico busca resolver la trayectoria temporal de alguna cantidad física como función de un generador dinámico, que suele representarse de forma funcional.

Podemos modelar la dinámica de un estado genérico \( y \) mediante la siguiente **ecuación dinámica**:

$$
\frac{dy}{dt} = f(t, y),
$$

la cual está sujeta a la condición inicial:

$$
y(t_0) = y_0.
$$

En esta notación:
- \( y \) representa el estado del sistema. Este estado puede ser un escalar o incluso una matriz que represente algún operador lineal.
- \( t \) es la variable temporal.

Este tipo de problema es conocido como un **problema de condición inicial** en el campo de las matemáticas aplicadas, ya que se busca encontrar la trayectoria de \( y \) en función del tiempo, dado un estado inicial en \( t_0 \).

## Soluciones a sistemas dinámicos

Resolver ecuaciones diferenciales para sistemas dinámicos es un tema fundamental que se abordará más a fondo en el curso. Sin embargo, en este contexto, el objetivo es familiarizarnos con las herramientas y métodos de programación científica que nos permiten resolver estos problemas numéricamente.

### Método Runge-Kutta de orden 4 (RK4)

Para resolver numéricamente sistemas dinámicos, utilizamos el **método de Runge-Kutta de cuarto orden (RK4)**, un método explícito que proporciona un buen equilibrio entre precisión y costo computacional.

El método RK4 estima la solución en un tiempo \( t_{n+1} \) basado en la solución anterior \( t_n \) de la siguiente forma:

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4),
$$

donde los términos \( k_1, k_2, k_3 \) y \( k_4 \) se calculan como sigue:

$$
\begin{aligned}
k_1 &= h f(t_n, y_n), \\
k_2 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right), \\
k_3 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right), \\
k_4 &= h f(t_n + h, y_n + k_3).
\end{aligned}
$$

### Contexto de uso en este proyecto

El método RK4 es una herramienta poderosa cuando se trata de resolver ecuaciones diferenciales en sistemas dinámicos. Este proyecto implementa el método para simular la evolución temporal de sistemas en los que el estado \( y \) puede representar una cantidad física, como la posición de un cuerpo, o una matriz cuántica que representa el estado de un sistema.

Al usar este método, los usuarios pueden experimentar con la simulación de diferentes sistemas dinámicos, proporcionando una comprensión más profunda de cómo estos sistemas evolucionan en el tiempo y cómo se pueden aproximar soluciones a problemas complejos mediante métodos numéricos.

## Reflexiones

Este enfoque no solo introduce a los usuarios a la implementación práctica de métodos numéricos como RK4, sino que también proporciona una base sólida para explorar y aplicar estos métodos en otras áreas de las ciencias aplicadas y la ingeniería. Las simulaciones numéricas son esenciales para resolver problemas que no tienen soluciones analíticas, y este proyecto proporciona las herramientas para llevar a cabo estas simulaciones de manera eficiente.

