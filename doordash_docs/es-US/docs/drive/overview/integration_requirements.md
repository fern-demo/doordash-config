En esta página

# Requisitos de integración

API: Drive

Este documento cubre la API de Drive. Si utilizas la API de Drive (Classic), consulta los [requisitos de integración de Drive (Classic)](/es-US/docs/drive_classic/overview/integration_requirements).

Nuestra misión es simple: queremos ser el servicio de entrega local más sencillo y confiable disponible, mientras protegemos a las tiendas, los clientes y Dashers que lo hacen posible. Esto se logra a través de un portal de autoservicio que permite a los desarrolladores aprovechar la amplia red de Dashers de DoorDash en tu propio negocio, donde cada integración es revisada por nuestro equipo para asegurar que se cumplan nuestros estándares tecnológicos y legales.

## Antes de solicitar el acceso a la producción[​](#antes-de-solicitar-el-acceso-a-la-producción "Enlace directo al encabezado")

Para poder acceder a nuestro entorno de producción y comenzar a realizar entregas en vivo, el equipo de DoorDash revisará y aprobará tu producto terminado. Para garantizar que este proceso se desarrolle sin problemas, consulta la siguiente lista de verificación antes de solicitar el acceso a la producción. Toma en cuenta que la autorización no está garantizada si revisas todos los artículos a continuación, pero es un buen comienzo.

Verifica lo siguiente:

* Tienes suficientes protecciones para evitar el retiro o la entrega de artículos restringidos. Entre ellos, se encuentran el tabaco, el cannabis u otras drogas ilícitas, armas y explosivos. Consulta la lista completa de artículos restringidos a continuación para obtener más información sobre los artículos que DoorDash no puede entregar.
* Has leído y aceptado nuestra Licencia Tecnológica y las Condiciones de Uso.
* Has utilizado el simulador de entregas para crear entregas de prueba y familiarizarte con el funcionamiento de DoorDash.
* Estás listo para realizar una demostración en vivo con el equipo de DoorDash. Podrás compartir la pantalla y guiarnos a través de una entrega de prueba de principio a fin, demostrando la experiencia completa del usuario.
* Los campos obligatorios se pasan en todas las llamadas a la API. Todos están anotados en nuestra referencia de la API.
* Los detalles clave de la entrega, como el ID de entrega y asistencia suministrada por DoorDash, se muestran a los usuarios correspondientes en tu interfaz de usuario. Puedes obtener más información sobre nuestros requisitos mínimos de interfaz de usuario a continuación, así como en nuestra página Cómo > Obtener acceso a la producción.

## Temas legales y seguridad[​](#temas-legales-y-seguridad "Enlace directo al encabezado")

DoorDash tiene un compromiso con la seguridad de todos los usuarios que utilizan su plataforma y servicios, incluyendo a los Dashers, las Tiendas y los Clientes. Nuestra prioridad es garantizar que cualquier persona que solicite o facilite la entrega a través de DoorDash pueda hacerlo con seguridad y confianza. Enumeramos los puntos principales a continuación, pero toma en cuenta que esta lista no es exhaustiva. Si tu negocio o producto no cumple con estos requisitos, el equipo de DoorDash puede rechazar tu solicitud de acceso a la producción; si te autorizaron para la producción, nos reservamos el derecho de desactivar tus credenciales de producción.

### Artículos restringidos[​](#artículos-restringidos "Enlace directo al encabezado")

DoorDash restringe la venta de ciertos artículos (incluyendo, entre otros, los que se mencionan a continuación) para mantener una experiencia de usuario de alta calidad, además de cumplir con los requisitos legales. Eres responsable de tener suficientes protecciones para evitar el retiro o la entrega de artículos restringidos.

La siguiente lista ofrece ejemplos de artículos restringidos, pero no de forma exhaustiva. DoorDash podría modificar esta lista a su exclusivo criterio y se reserva el derecho de eliminar o rechazar a anunciar, transportar, enviar, entregar o poner a disposición a través de su servicio cualquiera de los artículos anteriores o cualquier otro artículo que DoorDash considere inseguro o inapropiado.

* Personas, vida silvestre, animales o restos humanos/partes de animales
* Artículos ilegales; mercaderías robadas
* Fuegos artificiales, explosivos, armas de fuego, armamento, municiones y sus componentes; información sobre cómo fabricar dichos dispositivos
* Artículos que fomenten una actividad violenta o ilegal
* Artículos o materiales sexualmente explícitos u obscenos para adultos
* Cualquiera de los siguientes artículos sin un anexo firmado con DoorDash:
  + Alcohol
  + Productos con tabaco/para vapeo
  + Medicamentos para el resfrío, productos farmacéuticos, medicamentos de venta libre, vitaminas, dispositivos médicos o suplementos
* Drogas para uso recreativo o parafernalia relacionada con drogas, que incluyen, entre otros, cannabis o productos con CBD, Kratom o inhalantes, incluido el óxido nitroso
* Sustancias tóxicas y veneno
* Cualquier artículo que pese más de 50 libras
* Cualquier otro artículo cuya entrega esté prohibida sin un permiso o licencia según las leyes locales aplicables
* Materiales peligrosos, incluidos desechos médicos, o artículos venenosos o inflamables, excepto los materiales que:
  + (i) Se consideren ORM-D o (ii) se envíen en cantidades limitadas Y sean un producto de consumo
  + Se envíen en cantidades que no requieran rotulación
* Dinero, tarjetas de regalo, billetes de lotería o valores transferibles
* Productos falsificados
* Carnes o mariscos crudos
* Productos animales o provenientes de la vida silvestre en peligro de extinción; artículos elaborados con productos animales o de la vida silvestre en peligro de extinción (incluyendo, de manera enunciativa mas no limitativa, marfil, cuerno de rinoceronte, caviar euroasiático, carne de animales silvestres)
* Artículos que promuevan el odio o los grupos terroristas
* Productos que afirman o promueven resultados médicos específicos
* Cualquier artículo que pueda ser percibido como amenazante, obsceno, acosador, inapropiado o que de alguna otra manera infrinja los términos y condiciones aplicables que rigen tu relación con DoorDash

### Cumplimiento de leyes y reglamentos[​](#cumplimiento-de-leyes-y-reglamentos "Enlace directo al encabezado")

Tu empresa, incluyendo empleados, agentes, representantes, subcontratistas y el propio producto, debe cumplir con todas las leyes y reglamentos aplicables en todos los mercados en los que opera.

## Lineamientos técnicos e interfaz de usuario[​](#lineamientos-técnicos-e-interfaz-de-usuario "Enlace directo al encabezado")

Nuestro objetivo es ofrecer un servicio de entrega que sea fluido, sencillo y confiable para todas las partes involucradas. El diseño y la creación de un gran producto depende de ti, pero los lineamientos técnicos y de la interfaz de usuario que se presentan a continuación tienen el propósito de garantizar que tus clientes tengan la mejor experiencia posible de recolección y entrega. Visita nuestra página Cómo > Obtener acceso a la producción para obtener más información sobre el proceso de demostración y cómo el equipo de DoorDash evaluará tus propuestas.

### Requisitos[​](#requisitos "Enlace directo al encabezado")

* **El ID de entrega de DoorDash (`support_reference`) debe comunicarse a las tiendas, a los operadores de tiendas o a los usuarios que facilitan los retiros dentro de tu interfaz de usuario.** Este número de identificación, que se incluye en las respuestas de nuestra API, es necesario para todas las actividades de asistencia, incluyendo el servicio de asistencia a las tiendas de Drive (para cuestiones no técnicas relacionadas con las entregas, como los reembolsos) y el servicio de asistencia para desarrolladores (para cuestiones técnicas y de API relacionadas con las entregas).
* La hora del retiro debe comunicarse al usuario o usuarios que facilitan la recolección. Esto es más frecuente para la tienda o el operador de la tienda.
* El nombre del negocio de retiro debe pasarse en las solicitudes de entrega para todos los casos en que la dirección de retiro sea un lugar de negocios.
* Existe un claro bucle de retroalimentación para el usuario final si DoorDash rechaza el presupuesto o la solicitud de entrega. Por ejemplo, si DoorDash devuelve un error en la API debido a una dirección de entrega no válida, el usuario final debe recibir la indicación de corregir su dirección antes de completar el pago.

### Recomendaciones[​](#recomendaciones "Enlace directo al encabezado")

Estos elementos no son obligatorios, pero se recomiendan encarecidamente para garantizar una experiencia de retiro y entrega de alta calidad.

* Proporciona instrucciones claras de retiro y entrega cuando se creen las órdenes.
* Muestra el enlace de seguimiento de la entrega suministrado por DoorDash a las tiendas y clientes.
* Desarrolla una funcionalidad que permita a los administradores internos o a tus clientes comerciantes ver y gestionar las entregas. Por ejemplo, si tu negocio es una plataforma que permite a los clientes pedir flores a las floristerías locales, te recomendamos que desarrolles un panel de control que estas puedan utilizar para ver los detalles de las entregas actuales y anteriores

[Anterior

Precios y pago](/es-US/docs/drive/overview/pricing_payment)[Siguiente

How to Build for Restaurants](/es-US/docs/drive/how_to/build_for_restaurants)

* [Antes de solicitar el acceso a la producción](#antes-de-solicitar-el-acceso-a-la-producción)
* [Temas legales y seguridad](#temas-legales-y-seguridad)
  + [Artículos restringidos](#artículos-restringidos)
  + [Cumplimiento de leyes y reglamentos](#cumplimiento-de-leyes-y-reglamentos)
* [Lineamientos técnicos e interfaz de usuario](#lineamientos-técnicos-e-interfaz-de-usuario)
  + [Requisitos](#requisitos)
  + [Recomendaciones](#recomendaciones)