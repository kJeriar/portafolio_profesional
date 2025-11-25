# Portafolio Profesional | Karla Dev
> Proyecto desarrollado con Django para la presentación de trabajos y aptitudes de forma dinámica y profesional.

## Descripción
Este proyecto es un portafolio web de tipo **One Page** (página única), diseñado para ser elegante y funcional. Permite la administración total de contenido (proyectos, habilidades, y mensajes de contacto) a través del panel de Django Admin. El diseño utiliza una estética moderna con paleta de grises (Slate) y componentes modulares.

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