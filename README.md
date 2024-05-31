# 🤖 AutoClothesline

## 📄 Descripción

AutoClothesline es un tendal de ropa colocado en el techo que funciona de manera automatica, este cuenta con multiples sensores y actuadores que facilitan su uso:

- Motores que suben y bajan el tendal de manera automatizada
- Pantalla LCD que indica la temperatura, humedad, y cantidad de luz
- Ventilador que se activa con cierto nivel de temperatura
- LED RGB que indica la temperatura para facilitar el conocimiento de la temperatura sin el uso de la pantalla LCD.

## 💡 Esquema Electronico y componentes

Se utilizaran los sensores y actuadores necesarios para que se cumpla con todas las funciones de la maqueta:

![EsquemaElectronico](https://github.com/SiploxT/AutoClothesline/assets/102182731/2975ebbe-1455-4753-9db8-1db2c21e3a8f)

## 💻 Programación

Para programar todo el código de la maqueta entera, primero debemos hacer el código de cada parte por separado, separando cada actuador según sus necesidades.

### Uso de botones

Los botones de la maqueta harán que este eleve o descienda el tendal, de manera que simulen un mando a distancia que haría lo mismo.
Código: [MaquetaBotones](https://github.com/SiploxT/AutoClothesline/blob/main/Codigos/MaquetaBotonesJoel.py)

### Uso de pantalla

La pantalla LCD mostrará los datos de la temperatura (ºC), humedad (%) y exposición de luz (%).<br/>
Código: [MaquetaPantalla](https://github.com/SiploxT/AutoClothesline/blob/main/Codigos/MaquetaPantalla.py)

### Uso de ventilador y LED RGB

Estos dos componentes van unidos en un solo código, pues ambos actuan en función de la temperatura.
El ventilador se activará cuando la temperatura sea mayor a 20ºC, en ese caso se activará el relé que enciende el ventilador.
En el caso de el LED RGB, indicará la temperatura a través de colores: Rojo (Calor), Verde (Templado), y Azul (Frio).<br/>
Código: [MaquetaTemperatura](https://github.com/SiploxT/AutoClothesline/blob/main/Codigos/MaquetaTemperatura.py)
