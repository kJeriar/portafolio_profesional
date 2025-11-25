# Portafolio Profesional | Karla Jeria
> Portafolio web dinámico desarrollado en Django, optimizado para exhibir proyectos y habilidades con una presentación profesional y autogestionable.

## Descripción
El proyecto está construido bajo una arquitectura de vistas híbridas. La experiencia principal se centra en un scrollable single-page view (Página Única) para la sección de proyectos y contacto, mientras que las fichas de detalle y la información estática ('Sobre Mí') utilizan vistas separadas. Esto garantiza una navegación fluida para el contenido central y una estructura óptima para la información detallada.

---

## Características Principales

* **Página Única (SPA Feel):** Navegación fluida por anclas (`#`) dentro de la misma página.
* **Manejo de Contenido Dinámico:** El carrusel, la lista de proyectos y las habilidades se cargan directamente desde la base de datos.
* **Diseño Modular:** Uso de herencia de plantillas (`base.html`) y componentes (`{% include %}`).
* **Seguridad:** Implementación de un sistema de descarga de CV con **acceso por código** y soporte para múltiples versiones de CV.
* **Funcionalidad:** Formulario de contacto funcional que guarda los mensajes en la base de datos (MySQL).
* **UX Mejorada:** Botones condicionales (Repo/Demo) que se ocultan si no hay enlaces.
* **Diseño Responsive:** Utiliza Bootstrap 5 y CSS personalizado para adaptarse a móviles.

---

## Stack Tecnológico

| Área | Tecnología | Versión / Tipo |
| :--- | :--- | :--- |
| **Backend** | Python & Django | 3.10+ & 5.2.8 |
| **Database**| MySQL (Local) | MAMP Configuration |
| **Media/Imágenes** | Pillow | Manejo de archivos subidos |
| **Frontend** | HTML5, CSS3 | Puro + Variables CSS |
| **Framework** | Bootstrap | 5.3 (CDN) |