# Requisitos

## **Funcionales**

### Información de series

- [ ] Obtener información detallada de una serie de anime o manga específica.
- [ ] Buscar series por título, género, año de emisión, etc.
- [ ] Filtrar series por popularidad, calificación, duración, etc.

### Interacción con usuarios

- [ ] Permitir a los usuarios marcar series como favoritas o agregarlas a una lista de seguimiento.
- [ ] Permitir a los usuarios dejar reseñas y calificaciones para series específicas.

### Recomendaciones y descubrimiento

- [ ] Obtener recomendaciones personalizadas basadas en el historial de visualización del usuario.
- [ ] Sugerir nuevas series de anime y manga basadas en las preferencias de los usuarios.

### Listas y detalles adicionales

- [ ] Obtener la lista de episodios de una serie de anime específica.
- [ ] Obtener información sobre el manga original relacionado con una serie de anime.
- [ ] Obtener información sobre la disponibilidad de mercancía relacionada con una serie de anime o manga.
- [ ] Obtener información sobre las bandas sonoras y música de una serie de anime.
- [ ] Obtener información sobre las adaptaciones de videojuegos relacionadas con una serie de anime o manga.

### Información adicional

- [ ] Obtener información sobre el personal involucrado en la creación de una serie de anime o manga.
- [ ] Obtener información sobre la disponibilidad de una serie en diferentes plataformas de streaming.
- [ ] Obtener información sobre convenciones de anime, eventos y estrenos próximos.
- [ ] Obtener información sobre los premios y reconocimientos recibidos por una serie de anime o manga.

### Funcionalidades específicas

- [ ] Obtener información sobre el estado de producción de una serie en curso.
- [ ] Obtener información sobre el estado de producción de una serie en curso.
- [ ] Obtener información sobre el estado de producción de una serie en curso.
- [ ] Obtener información sobre el estado de producción de una serie en curso.

## **No Funcionales**

### Usabilidad y Documentación

- [ ] La API debe ser fácil de usar para los desarrolladores, con una documentación clara y completa que incluya ejemplos de uso, descripciones de los endpoints, parámetros de solicitud y respuestas esperadas.
- [ ] La documentación debe estar actualizada y ser fácilmente accesible para que los desarrolladores puedan integrarla rápidamente en sus aplicaciones.

### Escalabilidad

- [x] La arquitectura de la API debe ser altamente escalable, capaz de manejar un alto volumen de solicitudes concurrentes sin degradación del rendimiento.
- [ ] Deben implementarse prácticas de escalabilidad horizontal y vertical para garantizar que la API pueda crecer para satisfacer las demandas futuras de los usuarios.

### Seguridad y Autenticación

- [ ] Se debe implementar un sólido sistema de autenticación para proteger las operaciones sensibles de la API y prevenir el acceso no autorizado.
- [ ] Deben emplearse estándares de seguridad como OAuth 2.0 para gestionar el acceso de terceros a los datos de los usuarios y asegurar que solo los usuarios autorizados puedan acceder a ciertas funcionalidades.

### Rendimiento

- [ ] La API debe tener un rendimiento óptimo, proporcionando tiempos de respuesta rápidos y consistentes incluso bajo cargas pesadas.
- [ ] Deben optimizarse las consultas a la base de datos y la lógica de procesamiento para minimizar los tiempos de espera y maximizar la eficiencia de la API.

### Disponibilidad

- [ ] La API debe ser altamente disponible, con un tiempo de actividad cercano al 100% para garantizar que los usuarios puedan acceder a ella en todo momento.
- [ ] Deben implementarse estrategias de redundancia y tolerancia a fallos para mitigar los impactos de posibles interrupciones del servicio.

### Mantenibilidad

- [x] El código de la API debe seguir prácticas de desarrollo limpio y estar bien organizado para facilitar su mantenimiento a lo largo del tiempo.
- [x] Deben establecerse procedimientos claros para la gestión de versiones, actualizaciones y parches de seguridad para garantizar la estabilidad y la seguridad continua de la API.

## Limitaciones

- [ ] Limitaciones de solicitudes por minuto/hora
- [ ] Límites de acceso a datos detallados de ciertas series o características específicas.
- [ ] Requerimientos de autenticación para ciertas operaciones, como el uso de tokens de acceso o claves de API para realizar consultas o modificar datos en nombre de los usuarios.
- [ ] Consideraciones de rendimiento y escalabilidad, implementar almacenamiento en caché, optimización de consultas o distribución de carga para manejar picos de tráfico.
- [ ] Limitaciones compatibilidad con versiones específicas.
- [ ] Restricciones de acceso desde ciertas ubicaciones geográficas.
- [ ] Restricciones de datos, como la disponibilidad limitada de ciertos tipos de información o la necesidad de obtener permisos especiales para acceder a datos sensibles o restringidos.