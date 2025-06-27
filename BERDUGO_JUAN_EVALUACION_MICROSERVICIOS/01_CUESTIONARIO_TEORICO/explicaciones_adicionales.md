# Explicaciones Adicionales

Este documento explica el porqué de cada principio y patrón aplicado en el proyecto, y cómo su correcta implementación impacta en la calidad, escalabilidad y mantenibilidad de toda la solución multistack basada en microservicios.

SECCION A:

1. Explique los 4 layers principales de Clean Architecture y su responsabilidad
Clean Architecture promueve la separación de responsabilidades en capas concéntricas, lo que permite que los cambios en la infraestructura o frameworks no afecten el núcleo del negocio. Esto facilita la evolución tecnológica, la testabilidad y la independencia de la lógica de negocio. En el proyecto, cada microservicio implementa estas capas, asegurando que las reglas de negocio (Entities y Use Cases) estén protegidas de cambios externos, mientras que los adaptadores y frameworks pueden evolucionar sin riesgo para el dominio.

2. ¿Qué es la Regla de Dependencia en Clean Architecture?
La Regla de Dependencia garantiza que las capas internas (dominio y aplicación) nunca dependan de detalles externos (infraestructura, frameworks, UI). Esto permite que el código crítico del negocio sea reutilizable, portable y fácil de probar. En el proyecto, esta regla se respeta estrictamente, permitiendo que los microservicios sean robustos y adaptables a nuevas tecnologías o requerimientos.

3. Diferencias entre Entities y Value Objects con ejemplos del proyecto
La distinción entre entidades y objetos de valor es clave para un modelo de dominio claro y expresivo. Las entidades permiten rastrear y modificar objetos únicos a lo largo del tiempo, mientras que los value objects simplifican la lógica y evitan errores de identidad. En el proyecto, esto se traduce en código más seguro, menos propenso a bugs y más fácil de mantener.

4. Explique el patrón Repository y su implementación en el proyecto
El patrón Repository desacopla la lógica de negocio del acceso a datos, permitiendo cambiar la tecnología de persistencia sin afectar el dominio. Esto facilita pruebas unitarias, migraciones tecnológicas y mantenimiento. En el proyecto, cada microservicio define interfaces de repositorio en el dominio y las implementaciones en infraestructura, siguiendo las mejores prácticas.

5. ¿Qué son los Use Cases y cuál es su función?
Los Use Cases encapsulan la lógica de aplicación, coordinando entidades, servicios y repositorios para cumplir tareas específicas del negocio. Esto centraliza las reglas de negocio, facilita la evolución de requerimientos y permite pruebas aisladas. En el proyecto, cada acción relevante del sistema está representada por un caso de uso, asegurando claridad y robustez.

SECCION B:

6. Principios fundamentales de la arquitectura de microservicios
La adopción de microservicios permite que cada dominio de negocio evolucione de forma independiente, con equipos autónomos y despliegues desacoplados. Esto mejora la escalabilidad, la resiliencia y la velocidad de entrega. En el proyecto, cada microservicio es autónomo, con su propia base de datos y lógica, lo que facilita la innovación y la respuesta rápida a cambios.

7. Ventajas y desventajas de microservicios vs monolitos
La comparación entre microservicios y monolitos es fundamental para tomar decisiones arquitectónicas informadas. Los microservicios aportan escalabilidad y flexibilidad, pero requieren mayor disciplina operativa y automatización. En el proyecto, se optó por microservicios para maximizar la escalabilidad y la mantenibilidad, asumiendo la complejidad adicional con herramientas modernas de CI/CD y orquestación.

8. ¿Cómo se comunican los microservicios en este proyecto?
La comunicación mediante APIs HTTP REST, gestionada por un API Gateway, permite desacoplar servicios, versionar APIs y aplicar políticas de seguridad centralizadas. Esto facilita la integración, el monitoreo y la evolución de la solución. En el proyecto, esta estrategia asegura que los servicios puedan evolucionar y escalar sin afectar a los demás.

9. ¿Qué es el API Gateway y cuál es su función?
El API Gateway centraliza el acceso a los microservicios, simplificando la arquitectura para los clientes y permitiendo aplicar políticas de seguridad, autenticación y monitoreo de forma uniforme. Esto reduce la complejidad en los servicios individuales y mejora la experiencia de desarrollo y operación. En el proyecto, el API Gateway es clave para la seguridad, el enrutamiento y la agregación de datos, contribuyendo a una arquitectura robusta y escalable.
