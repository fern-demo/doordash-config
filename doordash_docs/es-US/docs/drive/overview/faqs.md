En esta página

# Preguntas frecuentes

### ¿Qué es el Portal para desarrolladores de DoorDash?[​](#qué-es-el-portal-para-desarrolladores-de-doordash "Enlace directo al encabezado")

El Portal para desarrolladores es una herramienta diseñada para que los desarrolladores exploren y desarrollen la API de abastecimiento de Drive de DoorDash sin problemas. En tan solo unos segundos, puedes crear una cuenta de desarrollador y comenzar a realizar pruebas en nuestro entorno de prueba. Una vez que hayas completado el desarrollo y una demostración, además de una revisión con el equipo de DoorDash, podrás generar credenciales de producción dentro del Portal y comenzar a solicitar conductores para cumplir con las entregas para tu negocio.

### ¿Qué es DoorDash Drive?[​](#qué-es-doordash-drive "Enlace directo al encabezado")

Drive es el servicio genérico de abastecimiento de órdenes de DoorDash, que permite a las tiendas acceder a una flota de entrega profesional, sin tener que ocuparse de la logística. Con DoorDash Drive, puedes solicitar un conductor en cualquier momento, dar seguimiento a tus órdenes, racionalizar tus costos de entrega e impulsar las ventas incrementales. Ya sea que necesites un abastecimiento flexible para la sobrecarga o un servicio de entrega constante y bajo demanda, la plataforma Drive está diseñada para trabajar con tu negocio.

### ¿Cuáles son las diferencias entre DoorDash Drive y DoorDash Marketplace?[​](#cuáles-son-las-diferencias-entre-doordash-drive-y-doordash-marketplace "Enlace directo al encabezado")

DoorDash Marketplace (es decir, la aplicación de DoorDash) permite a los clientes encontrar tu negocio y realizar órdenes. DoorDash Drive te permite ofrecer la entrega en tu propia plataforma, mediante tu propia aplicación o sitio web. Los detalles de la orden se comunican a DoorDash Drive a través de la API, y un Dasher se encarga del retiro y entrega por ti.

### ¿En qué países opera DoorDash Drive?[​](#en-qué-países-opera-doordash-drive "Enlace directo al encabezado")

Durante este periodo de prueba, la API estándar de DoorDash Drive solo permite realizar entregas dentro de Estados Unidos. Si tu negocio opera en Canadá o Australia, tendrás que crear la API de Drive (Classic). Toma en cuenta que Drive (Classic) solo está disponible para un grupo limitado de usuarios. Ponte en contacto a través de la página de asistencia si necesitas ayuda para entregas en estos países y no utilizas Drive (Classic).

### ¿Quién puede crear una cuenta de desarrollador?[​](#quién-puede-crear-una-cuenta-de-desarrollador "Enlace directo al encabezado")

Cualquier persona con una dirección de correo electrónico podrá registrarse como desarrollador de DoorDash. Nuestro Portal para desarrolladores está diseñado para agilizar el proceso de integración para cualquier persona que desee aprovechar el abastecimiento de DoorDash en su negocio, desde marcas minoristas individuales hasta plataformas de servicios comerciales de nivel empresarial.

### ¿Todos los integrantes de mi equipo de desarrollo tienen que crear su propia cuenta?[​](#todos-los-integrantes-de-mi-equipo-de-desarrollo-tienen-que-crear-su-propia-cuenta "Enlace directo al encabezado")

No, solo será necesaria una cuenta por empresa en el Portal para desarrolladores. Más adelante, permitiremos el inicio de sesión para varios usuarios, de modo que cada integrante de tu equipo pueda iniciar sesión en la misma cuenta de desarrollador con su propio correo electrónico y contraseña.

### ¿Qué necesito para comenzar?[​](#qué-necesito-para-comenzar "Enlace directo al encabezado")

Para registrarte y evaluar nuestro entorno de prueba, basta con que nos proporciones tu nombre, número de teléfono y dirección de correo electrónico.

### ¿Cómo sé si estoy desarrollando en Drive o en Drive Classic? ¿Cuál es la diferencia?[​](#cómo-sé-si-estoy-desarrollando-en-drive-o-en-drive-classic-cuál-es-la-diferencia "Enlace directo al encabezado")

Drive es nuestra oferta de API estándar y es la predeterminada para todos los desarrolladores. Drive Classic es nuestra API original/1.0 y tiene una referencia de API y terminales separados. Se incluyó un grupo limitado de usuarios alfa en la lista para desarrollar en Drive Classic, ya que es el más adecuado para los proveedores de middleware, como los sistemas de punto de venta, las plataformas de órdenes en línea y otras empresas de servicios comerciales que requieren soporte para el modelo de negocio y de tienda, la entrega de alcohol, etc. Si la URL de tu panel de control del Portal para desarrolladores incluye **'/Classic'**, se te agregó en la lista de candidatos permitidos para Classic. De lo contrario, estarás desarrollando para Drive.

### ¿Cuánto tiempo se tarda en desarrollar una integración con DoorDash?[​](#cuánto-tiempo-se-tarda-en-desarrollar-una-integración-con-doordash "Enlace directo al encabezado")

El Portal para desarrolladores está diseñado para brindar herramientas y recursos para crear una integración basada en la propia línea de tiempo. Dependiendo de tu hoja de ruta y necesidades de negocio, esto podría significar 1 o 2 días de desarrollo o múltiples sprints. Una vez que hayas completado el desarrollo, nuestro equipo revisará tu producto terminado y proporcionará una actualización sobre el acceso a la producción en un plazo de 5 a 10 días.

### ¿Cuánto cuestan las entregas a través de DoorDash Drive?[​](#cuánto-cuestan-las-entregas-a-través-de-doordash-drive "Enlace directo al encabezado")

La tarifa para las entregas solicitadas a través de nuestra API estándar de Drive es dinámica en función de la distancia entre el retiro y la entrega. Las entregas en un radio de 5 millas tienen una tarifa base de $9,75. Para entregas más allá de 5 millas, la tarifa es de $0,75 adicionales por cada milla, hasta un máximo 15 millas. Esta tarifa tiene en cuenta que las propinas son opcionales.

Para los desarrolladores que crean para nuestra API original (es decir, Drive Classic), DoorDash cobra una tarifa fija de $7,00 por entrega, más todas las propinas pagadas por el usuario final. Las propinas se pagan directamente al Dasher y se requieren en la interfaz de usuario para todos los desarrolladores que crean en esta API. Esta tarifa asume que DoorDash es el proveedor exclusivo de entregas para tu negocio o que DoorDash tiene el derecho de preferencia en todas las entregas. Toma en cuenta que Drive (Classic) solo está disponible para un grupo limitado de usuarios.

### ¿Hay artículos que no pueden entregarse a través de DoorDash?[​](#hay-artículos-que-no-pueden-entregarse-a-través-de-doordash "Enlace directo al encabezado")

Sí. La siguiente lista ofrece ejemplos de artículos restringidos, pero no de forma exhaustiva.

* Personas, vida silvestre, animales o restos humanos/partes de animales
* Artículos ilegales; mercaderías robadas
* Fuegos artificiales, explosivos, armas de fuego, armamento, municiones y sus componentes; información sobre cómo fabricar dichos dispositivos
* Artículos que fomenten una actividad violenta o ilegal
* Artículos o materiales sexualmente explícitos u obscenos para adultos
* Cualquiera de los siguientes artículos sin un anexo firmado con DoorDash:
  + Alcohol
  + Productos con tabaco/para vapeo
  + Medicamentos para el resfrío, productos farmacéuticos, medicamentos de venta libre, vitaminas, dispositivos médicos o suplementos
  + Drogas para uso recreativo o parafernalia relacionada con drogas, que incluyen, entre otros, cannabis o productos con CBD, Kratom o inhalantes, incluido el óxido nitroso
* Sustancias tóxicas y veneno
* Cualquier artículo que pese más de 50 libras
* Cualquier otro artículo cuya entrega esté prohibida sin un permiso o licencia según las leyes locales aplicables
* Materiales peligrosos, incluidos desechos médicos, o artículos venenosos o inflamables, excepto los materiales que:
  + (i) se consideren ORM-D
  + (ii) se envíen en cantidades limitadas Y sean un producto de consumo
  + Se envíen en cantidades que no requieran rotulación
* Dinero, tarjetas de regalo, billetes de lotería o valores transferibles
* Productos falsificados
* Carnes o mariscos crudos
* Productos animales o provenientes de la vida silvestre en peligro de extinción; artículos elaborados con productos animales o de la vida silvestre en peligro de extinción (incluyendo, de manera enunciativa mas no limitativa, marfil, cuerno de rinoceronte, caviar euroasiático, carne de animales silvestres)
* Artículos que promuevan el odio o los grupos terroristas
* Productos que afirman o promueven resultados médicos específicos
* Cualquier artículo que pueda ser percibido como amenazante, obsceno, acosador, inapropiado o que de alguna otra manera infrinja los términos y condiciones aplicables que rigen tu relación con DoorDash

### ¿Es necesario firmar un contrato para integrarse en Drive?[​](#es-necesario-firmar-un-contrato-para-integrarse-en-drive "Enlace directo al encabezado")

Para solicitar el acceso a la producción, deberás leer y aceptar nuestros términos. Los términos para la API estándar de Drive se pueden encontrar [aquí](https://developer.doordash.com/terms/v2/2/) y los términos para Drive Classic, [aquí](https://developer.doordash.com/terms/v1/1/).

### ¿Puedo realizar un seguimiento de las entregas?[​](#puedo-realizar-un-seguimiento-de-las-entregas "Enlace directo al encabezado")

Sí, DoorDash proporciona un enlace de seguimiento para cada entrega que puedes exponer dentro de tu interfaz de usuario.

### ¿Qué es UTC y las zonas horarias locales?[​](#qué-es-utc-y-las-zonas-horarias-locales "Enlace directo al encabezado")

UTC está 8 horas por delante de PST, 9 MST, 10 CST y 11 EST.

### ¿Cómo se me notificará la interrupción de un servicio?[​](#cómo-se-me-notificará-la-interrupción-de-un-servicio "Enlace directo al encabezado")

[Aquí](https://doordash.statuspage.io/) se informan todos los incidentes del sistema, junto con los resultados. No dudes en suscribirte a las actualizaciones por correo electrónico cuando lo necesites. Para notificar un incidente o problema que no aparezca en la página de estado, puedes ponerte en contacto con el equipo de DoorDash a través de la página de asistencia en el Portal para desarrolladores.

### ¿Hay límites en las tarifas?[​](#hay-límites-en-las-tarifas "Enlace directo al encabezado")

El límite está establecido en aproximadamente 300 solicitudes en un periodo de 60 segundos. Si estás planeando llevar a cabo pruebas de carga o resiliencia, ponte en contacto con el equipo de DoorDash a través de la página de asistencia con al menos 3 días de anticipación. Si no nos avisas, podemos desactivar tus credenciales de la API.

### Si la entrega se retrasa, ¿DoorDash me devolverá el dinero?[​](#si-la-entrega-se-retrasa-doordash-me-devolverá-el-dinero "Enlace directo al encabezado")

El equipo de asistencia para tiendas de DoorDash revisa todas las solicitudes de reembolso relacionadas con las entregas de Drive caso por caso. Si DoorDash puede reembolsar, y cuánto, depende del tipo de problema. Puedes consultar nuestra matriz de reembolsos aquí.

### ¿Quién entrega artículos a través de DoorDash?[​](#quién-entrega-artículos-a-través-de-doordash "Enlace directo al encabezado")

Puedes leer sobre los requisitos de los Dashers [aquí](https://help.doordash.com/dashers/s/article/Requirements-for-Dashing).

[Anterior

Notas de la versión](/es-US/docs/drive/overview/release_notes)[Siguiente

Comenzar (API)](/es-US/docs/drive/tutorials/get_started)

* [¿Qué es el Portal para desarrolladores de DoorDash?](#qué-es-el-portal-para-desarrolladores-de-doordash)
* [¿Qué es DoorDash Drive?](#qué-es-doordash-drive)
* [¿Cuáles son las diferencias entre DoorDash Drive y DoorDash Marketplace?](#cuáles-son-las-diferencias-entre-doordash-drive-y-doordash-marketplace)
* [¿En qué países opera DoorDash Drive?](#en-qué-países-opera-doordash-drive)
* [¿Quién puede crear una cuenta de desarrollador?](#quién-puede-crear-una-cuenta-de-desarrollador)
* [¿Todos los integrantes de mi equipo de desarrollo tienen que crear su propia cuenta?](#todos-los-integrantes-de-mi-equipo-de-desarrollo-tienen-que-crear-su-propia-cuenta)
* [¿Qué necesito para comenzar?](#qué-necesito-para-comenzar)
* [¿Cómo sé si estoy desarrollando en Drive o en Drive Classic? ¿Cuál es la diferencia?](#cómo-sé-si-estoy-desarrollando-en-drive-o-en-drive-classic-cuál-es-la-diferencia)
* [¿Cuánto tiempo se tarda en desarrollar una integración con DoorDash?](#cuánto-tiempo-se-tarda-en-desarrollar-una-integración-con-doordash)
* [¿Cuánto cuestan las entregas a través de DoorDash Drive?](#cuánto-cuestan-las-entregas-a-través-de-doordash-drive)
* [¿Hay artículos que no pueden entregarse a través de DoorDash?](#hay-artículos-que-no-pueden-entregarse-a-través-de-doordash)
* [¿Es necesario firmar un contrato para integrarse en Drive?](#es-necesario-firmar-un-contrato-para-integrarse-en-drive)
* [¿Puedo realizar un seguimiento de las entregas?](#puedo-realizar-un-seguimiento-de-las-entregas)
* [¿Qué es UTC y las zonas horarias locales?](#qué-es-utc-y-las-zonas-horarias-locales)
* [¿Cómo se me notificará la interrupción de un servicio?](#cómo-se-me-notificará-la-interrupción-de-un-servicio)
* [¿Hay límites en las tarifas?](#hay-límites-en-las-tarifas)
* [Si la entrega se retrasa, ¿DoorDash me devolverá el dinero?](#si-la-entrega-se-retrasa-doordash-me-devolverá-el-dinero)
* [¿Quién entrega artículos a través de DoorDash?](#quién-entrega-artículos-a-través-de-doordash)