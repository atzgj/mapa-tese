# Mapa TESE

Mapa interactivo del campus de la universidad visto desde arriba, hecho con
HTML, CSS y JavaScript. Cada edificio se puede tocar para ver su información.

🔗 **Ver el mapa en vivo:** https://atzgj.github.io/mapa-tese/

## Escanea para abrir el mapa

![Código QR del mapa](qr-mapa-tese.png)

## Qué puede hacer

- Edificios clicables sobre una imagen aérea del campus
- Tarjeta emergente con el nombre y la descripción de cada edificio
- Resaltado del edificio seleccionado
- Se cierra con el botón ×, con la tecla Esc o tocando una zona vacía
- Adaptado a celular: la tarjeta aparece como panel inferior

## Tecnologías

- HTML, CSS y JavaScript (SVG para dibujar los edificios sobre la imagen)
- Git y GitHub Pages para publicarlo
- Python (librería `qrcode`) para generar el código QR

## Cómo agregar un edificio

Los edificios son datos en una lista dentro de `index.html`. Para agregar uno
se añade una ficha como esta:

```javascript
{
  nombre: "Nombre del edificio",
  descripcion: "Qué hay dentro.",
  puntos: "x1,y1 x2,y2 x3,y3 x4,y4"
}
```

Las coordenadas se obtienen abriendo la página con `?trazar` al final de la
dirección y haciendo clic en las esquinas del edificio.

## Estado del proyecto

MVP en desarrollo. Pendiente: trazar todos los edificios del campus, buscador,
zoom y arrastre.

## Autora

Atzimba Godínez – Ingeniería en Sistemas Computacionales