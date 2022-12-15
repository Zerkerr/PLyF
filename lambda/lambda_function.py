# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Iniciando la chamba"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Nos vemos"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
#-------------------------------------------------------------------------------
class getactoresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getactores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["actores"].value
        if name == "Kit Harrington":
            datos = " nació el 26 de diciembre de 1986 en Londres, Inglaterra. Es un actor y escritor, conocido por Game of Thrones (2011), Pompeya (2014) y Eternos (2021). Está casado con Rose Leslie desde el 23 de junio de 2018. Tienen un niño."
            
        if name == "Robert Pattinson":
            datos = " nació el 13 de mayo de 1986 en Londres, Inglaterra. Es un actor y escritor, conocido por Crepúsculo (2008), Eclipse (2010) y Batman (2022)."
            
        if name == "Charlie Cox":
            datos = " nació el 15 de diciembre de 1982 en Londres, Inglaterra. Es un actor, conocido por La teoría del todo (2014), Daredevil (2015) y Stardust: El misterio de la estrella (2007)."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getanfibiosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getanfibios")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["anfibios"].value
        if name == "lagartija":
            datos = " El aspecto de la lagartija suele inspirar simpatía, ya que es absolutamente inofensiva. Es por ello que hay personas que adoptan lagartijas como mascota. No obstante, tienen un carácter huidizo y prefieren esconderse entre grietas, matorrales o piedras que tener contacto directo con los humanos."
            
        if name == "sapo":
            datos = " carecen de dientes y tienen glándulas parotoides en la parte trasera de su cabeza. Estas glándulas contienen diversas toxinas que tienen diferentes efectos."
            
        if name == "rana":
            datos = " aunque muchas otras especies de otras familias reciben también este nombre popular; así, los ránidos son a veces denominados ranas verdaderas para diferenciarla de los miembros de las otras familias que también incluyen la palabra «rana» en su nombre común. Se distribuyen por todo el planeta excepto en las zonas polares, sur de África, Madagascar y gran parte de Australia."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getanimalesacuaticosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getanimalesacuaticos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["animalesacuaticos"].value
        if name == "ballena":
            datos = " Las ballenas son los animales más grandes que jamás hayan existido. Pertenecen a un grupo de mamíferos marinos conocidos como cetáceos. No son peces porque tienen sangre caliente, respiran aire a través de pulmones y dan a luz a crías vivas que se alimentan de leche materna."
            
        if name == "marsopa":
            datos = " Si bien son similares a los delfines, están de hecho relacionados de manera más cercana a los narvales y a las belugas. Las marsopas varían en tamaño desde la vaquita marina, con 1,4 metros de longitud y 54 kilogramos de peso, hasta la marsopa de Dall, con 2,3 m y 220 kg."
            
        if name == "delfin":
            datos = " mamíferos de una familia de cetáceos odontocetos muy heterogénea, que comprende 37 especies actuales. Miden entre 2 y 8 metros de largo, con el cuerpo fusiforme y la cabeza de gran tamaño, el hocico alargado y solo un espiráculo en la parte superior de la cabeza (orificio respiratorio que muchos animales marinos tienen como contacto del aire o agua con su sistema respiratorio interno)."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getanimalesaereosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getanimalesaereos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["animalesaereos"].value
        if name == "paloma":
            datos = " Son aves dotadas de gran inteligencia (si se las compara con otras aves), se distribuyen por todo el mundo, excepto la Antártida y el Ártico, y con centro de dispersión en América Central. La mayor diversidad de especies la tienen la ecozona indomalaya y la ecozona de Australasia."
            
        if name == "zopilote":
            datos = " es conocida por ser carroñera; en áreas pobladas por humanos hurga en basureros, come huevos y material vegetal en descomposición y puede matar o lesionar a mamíferos recién nacidos o incapacitados."
            
        if name == "aguila":
            datos = " poseen un pico grande, poderoso y puntiagudo para desprender la carne de su presa. Cuentan también con tarsos y garras poderosas. Llama también la atención la fuerza de las águilas, que les posibilita alzar en vuelo a presas mucho más pesadas que ellas."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getanimalesterrestresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getanimalesterrestres")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["animalesterrestres"].value
        if name == "canguro":
            datos = " poseen grandes y poderosas patas traseras, grandes pies aptos para saltar, una cola larga y musculosa para mantener el equilibrio y una cabeza pequeña. Los canguros son herbívoros, alimentándose de pasto y raíces."
            
        if name == "koala":
            datos = " fácilmente reconocible por su cuerpo robusto sin cola, cabeza grande con orejas redondas y peludas y nariz grande en forma de cuchara. Mide entre 60 y 85 cm y pesan de 4 a 15 kg."
            
        if name == "cocodrilo":
            datos = " reptiles con forma de grandes lagartos, de cuerpo robusto, morro prominente largo y plano, cola comprimida lateralmente y ojos, oídos y fosas nasales en la parte superior de la cabeza. Buenos nadadores, pueden moverse en tierra andando separando el cuerpo de tierra o arrastrando el cuerpo, mientras que las especies de menor tamaño incluso pueden galopar."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getarteIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getarte")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["arte"].value
        if name == "renacentista":
            datos = " movimiento cultural y artístico europeo basado en el renacer de los valores de la Antigüedad clásica. Alcanzó su auge en el siglo XV y se extendió hasta la primera mitad del siglo XVI, cuando dio paso al período barroco. Tuvo su origen en la región de Italia, desde donde se extendió al resto de Europa."
            
        if name == "barroco":
            datos = " se puede definir como el “arte de parecer”, ya en las artes, ya en la literatura. Tres elementos pueden ser considerados fundamentales de su estética: el efectismo, la espectacularidad y la emocionalidad."
            
        if name == "abstracto":
            datos = " forma de expresión de sentimientos artísticos que prescinde de toda figuración y propone una nueva realidad distinta a la natural. Usa un lenguaje visual de forma, color y línea para crear una composición que puede existir con independencia de referencias visuales del mundo real."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getbailesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getbailes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["bailes"].value
        if name == "flamenco":
            datos = " es conocido por su intensidad emocional, su porte orgulloso, el uso expresivo de los brazos y el zapateado rítmico de los pies, a diferencia del claqué o la danza irlandesa, que utilizan técnicas diferentes."
            
        if name == "salsa":
            datos = " conjunto de ritmos afrocaribeños fusionados con jazz y otros estilos. Su nacimiento ha sido muy debatido, pero se sabe que procede de una fusión que llevaron a cabo los habitantes del Caribe cuando escucharon la música europea para luego mezclarla con sus tambores."
            
        if name == "tango":
            datos = " anza de pareja enlazada estrechamente surgida a partir de la fusión de danzas y ritmos afro-rioplatenses, gauchos y europeos. Es un baile característico de la región del Río de la Plata, principalmente de Buenos Aires, Argentina."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getbanderasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getbanderas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["banderas"].value
        if name == "marruecos":
            datos = " La estrella verde de cinco puntas en el centro, que es el símbolo del Islam, representa el gobierno marroquí y el fondo rojo representa la tierra del pueblo marroquí."
            
        if name == "polonia":
            datos = " está formada por dos franjas horizontales de iguales dimensiones. La franja superior es blanca y la inferior, carmesí. Posee unas proporciones de 5:8."
            
        if name == "australia":
            datos = " está compuesta por un fondo de color azul, con la bandera del Reino Unido en el cantón. Bajo este, se ubica una estrella blanca de siete puntas, conocida como la Estrella de la Mancomunidad, o también llamada Estrella de la Federación (Commonwealth Star o Federation Star, seis puntas representan a los seis estados originales y la séptima por los territorios y futuros estados de Australia)."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getbasuratiposIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getbasuratipos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["basuratipos"].value
        if name == "vidrios":
            datos = " material inorgánico duro, frágil, transparente y amorfo que se encuentra en la naturaleza, aunque también puede ser producido por el ser humano."
            
        if name == "organica":
            datos = " todos los desechos y residuos de origen biológico. Por ejemplo, basura de origen alimenticio, papel o cartón, restos de plantas, desechos corporales de animales y de humanos."
            
        if name == "inorganica":
            datos = " todo aquello que no viene de organismos vivos. Puede provenir de procesos de transformación firmados por el ser humano. Por ejemplo, botellas de vidrio, plásticos, PVC, latas, pilas, basura sanitaria."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getbebidasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getbebidas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["bebidas"].value
        if name == "cebada":
            datos = " es una bebida refrescante que se suele preparar como una infusión de granos de cebada (Hordeum vulgare) a fuego lento de casi tres cuartos de hora de cocción. El agua así obtenida se suele colar y endulzar ligeramente con azúcar o miel. Posee un color ligeramente lechoso."
            
        if name == "horchata":
            datos = " Agua fresca que en México se prepara normalmente con granos de arroz remojados en agua que después se muelen y se mezclan con agua endulzada, al final se aromatiza con canela."
            
        if name == "coca cola":
            datos = " es un refresco usualmente saborizado con caramelo colorado, y que frecuentemente posee cafeína."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getbotanasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getbotanas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["botanas"].value
        if name == "pretzels":
            datos = " galleta o bollo horneado, y retorcido en forma de lazo, con un sabor ligeramente salado."
            
        if name == "papitas":
            datos = " es una fina rodaja de patata frita, horneada o frita al aire hasta que queda crujiente. Se suelen servir como tentempié, guarnición o aperitivo."
            
        if name == "cacahuates":
            datos = " hierba anual, erecta o con tallo ascendente de 30-80 cm de altura, con tallos pubescentes de color amarillento, glabrescentes. Estípulas de 2-4 cm, pilosas. De este fruto se obtienen alimentos como la crema o mantequilla de maní, y se extrae su aceite, muy empleado en la cocina de la India y del sureste de Asia."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getcalzadoIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getcalzado")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["calzado"].value
        if name == "chanclas":
            datos = " tipo de calzado ligero y muy cómodo, que se caracteriza por llevar el talón suelto, sujetándose al pie por la parte anterior."
            
        if name == "tenis":
            datos = " tipo de calzado que se utiliza para realizar distintos tipos de deporte. Generalmente posee un cuerpo fabricado en piel, lona y/o materiales sintéticos, y una suela de caucho que ofrece una mayor adherencia, así como flexibilidad."
            
        if name == "zapatillas":
            datos = " tipo de calzado que se caracteriza por elevar el talón sobre la altura de los dedos de los pies femeninos."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getcampingtiposIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getcampingtipos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["campingtipos"].value
        if name == "rural":
            datos = " establecimiento de alojamiento turístico en un medio rural destinado a la vida al aire libre."
            
        if name == "campo":
            datos = " estos ofrecen a los campistas conexiones eléctricas en al menos el 70% de las instalaciones, agua caliente en parte de las duchas y en todos los baäos, areas verdes y piscina."
            
        if name == "playa":
            datos = " Por lo general están más alejados del mejor lugar de la ciudad o localidad, siendo ésta la principal diferencia con el camping de primera."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getcarnecortesIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getcarnecortes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["carnecortes"].value
        if name == "vacio":
            datos = " Se sitúa en la parte lateral, junto a las costillas, donde ya no hay hueso. Es una carne fibrosa recubierta de dos capas de grasa externa que retiene sus jugos al cocinarla."

        if name == "tomahawk":
            datos = " Es lo mismo que un chuletón pero dejando todo el hueso de la costilla totalmente limpio de grasa. Suele proceder de animales de gran tamaño y su nombre viene de las hachas que utilizaban los antiguos indígenas norteamericanos, que tenían una forma parecida."

        if name == "rib eye":
            datos = " Es el lomo alto limpio, sin tapilla y sin intercostal. La traducción es ojo de costilla por ser eso, el centro del lomo, y muy posiblemente lo encontrarás en las cartas como ojo de bife. También es un corte típico americano y tiene un gran sabor y jugosidad. En Australia y Nueva elanda sí suelen servirlo con el hueso."

        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getciudadesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getciudades")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["ciudades"].value
        if name == "madrid":
            datos = " es la capital y la ciudad más poblada de España. Cuenta con casi 3,4 millones de habitantes y un área metropolitana de aproximadamente 6,7 millones."
            
        if name == "singapur":
            datos = " es un país soberano insular de Asia, formado por sesenta y tres islas, cuya forma de gobierno es la república parlamentaria."
            
        if name == "new york":
            datos = " es la ciudad más poblada de los Estados Unidos de América y una de las más pobladas del mundo, con un área urbana de 24 millones de habitantes."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getcoloresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getcolores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["colores"].value
        if name == "verde":
            datos = " color característico de la vegetación y se puede definir por su semejanza a la coloración de las hojas de la hierba fresca o de la piedra esmeralda."
            
        if name == "morado":
            datos = " es un color púrpura o violeta, oscuro y profundo, cuya referencia originaria es el color de la mora, es decir la infrutescencia del moral (Morus nigra ), o un color entre carmín y azul"
            
        if name == "azul":
            datos = " se percibe ante la fotorrecepción de una luz cuya longitud de onda mide entre 460 y 482 nm. Se asemeja a la coloración más característica del lapislázuli."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getcontinentesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getcontinentes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["continentes"].value
        if name == "europa":
            datos = " continente ubicado enteramente en el hemisferio norte y mayoritariamente en el hemisferio oriental. Las fronteras de Europa están situadas en la mitad occidental del hemisferio norte, limitada por el océano Ártico en el norte, hasta el mar Mediterráneo por el sur."
            
        if name == "oceania":
            datos = " continente insular de la Tierra constituido por la plataforma continental de Australia, las islas de Nueva Guinea, Nueva Zelanda y los archipiélagos coralinos y volcánicos de Melanesia, Micronesia y Polinesia."
            
        if name == "america":
            datos = " es el segundo continente más grande de la Tierra, después de Asia. Ocupa gran parte del hemisferio occidental del planeta."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdeportesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdeportes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["deportes"].value
        if name == "volleyball":
            datos = " deporte que se juega con una pelota y en el que dos equipos, integrados por seis jugadores cada uno, se enfrentan sobre un área de juego separada por una red central."
            
        if name == "tenis":
            datos = " deporte de raqueta practicado sobre una pista rectangular (compuesta por distintas superficies como lo pueden ser el cemento, la tierra batida o hierba), delimitada por líneas y dividida por una red."
            
        if name == "futbol":
            datos = " deporte de equipo jugado entre dos conjuntos de once jugadores cada uno, mientras los árbitros se ocupan de que las normas se cumplan correctamente."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdesayunosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdesayunos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["desayunos"].value
        if name == "occidental":
            datos = " suele consistir en huevos fritos, alubias, champiñones, salchichas pequeñas y tomate a la plancha. Este también incluye tostadas, café o té y zumo."
            
        if name == "americano":
            datos = " suele estar compuesto por dos huevos, beicon, salchichas pequeñas, panqueques y salsa de arce. Este también incluye tostadas, café o té y zumo. Con la leche también se pueden tomar cereales."
            
        if name == "continental":
            datos = " ormato de desayuno ligero que se compone de café o té, panecillos, mantequilla, mermeladas, bollería, jugo (zumos) de fruta, etc. y que es un estándar en la hostelería de origen occidental."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdibujoIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdibujo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["dibujo"].value
        if name == "animado":
            datos = " Se consiguen dibujando secuencialmente cada fotograma que componen a las obras, generando una secuencia y representación de imágenes en movimiento."
            
        if name == "geometrico":
            datos = " es aquello vinculado a la geometría, que es la especialidad de las matemáticas orientada al análisis de las magnitudes y las propiedades de las figuras en el espacio o en un plano."
            
        if name == "mano alzada":
            datos = " técnica que se emplea para expresar con inmediatez las ideas necesarias para la elaboración de una determinada pieza, objeto o proceso."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdinosauriosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdinosaurios")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["dinosaurios"].value
        if name == "velociraptor":
            datos = " género con 2 especies conocidas de dinosaurios terópodos dromeosáuridos que vivieron hacia finales del período Cretácico, entre 75 a 71 millones de años durante el Campaniaense, en lo que es hoy Asia."
            
        if name == "triceratops":
            datos = " género con dos especies conocidas de dinosaurios ceratopsianos ceratópsidos, que vivieron a finales del período Cretácico, hace aproximadamente entre 68 y 66 millones de años, durante el Maastrichtiense, en lo que hoy es Norteamérica."
            
        if name == "t-rex":
            datos = " única especie conocida del género fósil Tyrannosaurus de dinosaurio terópodo tiranosáurido, que vivió a finales del período Cretácico, hace aproximadamente entre 68 y 66 millones de años."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdirectoresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdirectores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["directores"].value
        if name == "Jordan Peele":
            datos = " es un actor, comediante, director y guionista estadounidense. Es conocido por protagonizar la serie de Comedy Central, Key & Peele y por ser parte del elenco de MADtv. En 2014 tuvo un rol recurrente en la serie de FX, Fargo."
            
        if name == "George Lucas":
            datos = " es un cineasta, escritor, filántropo y empresario estadounidense. Lucas es más conocido por crear las franquicias de Star Wars e Indiana Jones y fundar Lucasfilm, LucasArts e Industrial Light & Magic."
            
        if name == "Christopher Nolan":
            datos = " director de cine, guionista, productor y editor británico-estadounidense. Nacido y criado en Londres, Nolan desarrolló un interés por el cine desde una edad temprana."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getdragonesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getdragones")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["dragones"].value
        if name == "drogon":
            datos = " dragón que aparece en la serie de novelas Canción de hielo y fuego, de George R. R. Martin. Es eclosionado por Daenerys Targaryen junto con sus dos hermanos Viserion y Rhaegal. Fue nombrado en memoria del difunto Khal Drogo."
            
        if name == "smaug":
            datos = " dragón que aparece en la novela El hobbit, de J. R. R. Tolkien. En ella se cuenta que era el último de los grandes dragones que quedaban en la Tierra Media y que expulsó a los enanos de la Montaña Solitaria tomando su tesoro."
            
        if name == "wyvern":
            datos = " tipo de dragón que se distinguía por poseer una cola puntiaguda la cual se decía que era venenosa."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getelementosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getelementos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["elementos"].value
        if name == "tierra":
            datos = " elemento Tierra, junto con el fuego, el agua y el aire, es uno de los cuatro elementos de las cosmogonías tradicionales en Occidente y está presente en todas las religiones y sus rituales, en la filosofía esotérica, en la alquimia y en la astrología. Se considera «pasivo y femenino», al igual que el elemento agua, frente al aire y el fuego, «activos y masculinos»."
            
        if name == "aire":
            datos = " elemento aire, junto con el fuego, la tierra y el agua, es uno de los cuatro elementos de las cosmogonías tradicionales en Occidente y Oriente. Está presente en todas las religiones y sus rituales, en la filosofía esotérica, en la alquimia y en la astrología."
            
        if name == "fuego":
            datos = " elemento fuego, junto con el agua, la tierra y el aire, es uno de los cuatro elementos de las cosmogonías tradicionales en Occidente, «presente en todas las grandes religiones», en la alquimia, en la astrología, en la filosofía esotérica y en la masonería. Es masculino, al igual que el elemento aire, frente a los elementos tierra y agua, que se consideran femeninos."
        
        if name == "agua":
            datos = " elemento agua, junto con el fuego, la tierra y el aire, es uno de los cuatro elementos de las cosmogonías tradicionales en Occidente y Oriente. Está presente en todas las religiones y sus rituales, en la filosofía esotérica, en la alquimia y en la astrología."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getescritoresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getescritores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["escritores"].value
        if name == "Frank Herbert":
            datos = " fue un escritor estadounidense de ciencia ficción, famoso por la novela de 1965 Dune y sus cinco secuelas. Aunque ganó reconocimiento por sus novelas, también escribió cuentos y trabajó como periodista, fotógrafo, crítico literario, consultor ecológico y conferenciante."
            
        if name == "Stephen King":
            datos = " es un escritor estadounidense de novelas de terror, ficción sobrenatural, misterio, ciencia ficción y literatura fantástica. Sus libros han vendido más de 350 millones de ejemplares."
            
        if name == "George R. R. Martin":
            datos = " es un escritor y guionista estadounidense de literatura fantástica, ciencia ficción y terror. Es conocido especialmente por ser el autor de la serie de novelas Canción de hielo y fuego."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getestadosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getestados")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["estados"].value
        if name == "Tamaulipas":
            datos = " es uno de los treinta y un estados que, junto con la Ciudad de México, forman los Estados Unidos Mexicanos. Su capital es Ciudad Victoria y su ciudad más poblada es Reynosa. Fue fundado el 7 de febrero de 1824."
            
        if name == "Guanajauto":
            datos = " Su capital es la ciudad homónima y su ciudad más poblada es León. Se divide en cuarenta y seis municipios."
            
        if name == "Sinaloa":
            datos = " Está ubicado en la región noroeste del país, limitando al norte con Sonora y Chihuahua, al este con Durango, al sur con Nayarit y al oeste con el golfo de California (océano Pacífico). Fue fundado el 14 de octubre de 1830."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getetniasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getetnias")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["etnias"].value
        if name == "egipcios":
            datos = " La civilización de los Egipcios dependía en gran parte del río Nilo. Debido a que la abundante agua de este fomentaba el desarrollo de su agricultura. Generalmente construían sus ciudades sobre las zonas elevadas cerca del Nilo, considerando de esta manera el peligro de las posibles inundaciones."
            
        if name == "judios":
            datos = " colectividad étnico-religiosa y cultural descendiente del pueblo hebreo y de los antiguos israelitas del levante mediterráneo. La religión constituye un posible aspecto de pertenencia al pueblo judío así como las tradiciones, prácticas culturales, sociales y lingüísticas."
            
        if name == "arabes":
            datos = " es originalmente una persona natural de la península arábiga y otros territorios circundantes de lengua árabe, o alguien de este origen."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getfloresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getflores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["flores"].value
        if name == "tulipanes":
            datos = " tipo de planta que pertenece a la familia de las liliáceas, por su gran belleza estos sean convertido en unas las flores ornamentales mas populares del mundo."
            
        if name == "girasoles":
            datos = " son conocidos como las flores del verano y además son unas de las plantas más populares para decorar los espacios interiores durante la temporada."
            
        if name == "gardenias":
            datos = " Estas hermosas plantas se cultivan como arbustos ornamentales en jardines de regiones cálidas y como plantas de interior en zonas frías."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getfrutasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getfrutas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["frutas"].value
        if name == "papaya":
            datos = " crecen en climas tropicales y también se conocen como papaya o papayón. Su sabor dulce, color vibrante y el aporte de una amplia variedad de beneficios para la salud la convierten en una fruta popular."
            
        if name == "manzana":
            datos = " fruto comestible de la especie Malus domestica, el manzano común. Es una fruta pomácea de forma redonda y sabor muy dulce, dependiendo de la variedad."
            
        if name == "banana":
            datos = " fruto comestible, de varios tipos de grandes plantas herbáceas del género Musa (de origen indomalayo)."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getfrutosrojosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getfrutosrojos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["frutosrojos"].value
        if name == "fresa":
            datos = " Son cultivadas por su fruto comestible (eterio) llamado de la misma manera: fresa o, en algunos países hispanoamericanos, frutilla."
            
        if name == "frambuesa":
            datos = " su fruto comestible, la frambuesa roja, es un eterio formado por varias drupas, al igual que la frambuesa negra (Rubus occidentalis) y la frambuesa azul (Rubus leucodermis) oriundas de América."
            
        if name == "cereza":
            datos = "  fruta diversa en vitaminas y minerales. Si bien todos los cerezos son del género Prunus, a este género también pertenecen especies que no lo son."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getgalaxiasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getgalaxias")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["galaxias"].value
        if name == "triangulo":
            datos = " También conocida como M33 o NGC 598, se ubica en la constelación del triángulo (triangulum) a unos 2,8 millones de años luz de la Tierra."
            
        if name == "via lactea":
            datos = " Nuestra galaxia espiral presenta un diámetro de unos 100.000 años luz y contiene alrededor de unas 200.000 a 400.000 millones de estrellas distintas, de las cuales el Sol es apenas una de las más pequeñas, ubicada a una distancia de 25.756 años luz del centro galáctico."
            
        if name == "andromeda":
            datos = " También conocida como M31 o NGC 224, esta es nuestra galaxia vecina, con la que la Vía Láctea colisionará y se fusionará dentro de cinco mil millones de años aproximadamente."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getgatosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getgatos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["gatos"].value
        if name == "sphynx":
            datos = " La característica principal del sphynx es que no tiene pelaje. Este gato no tiene bigotes ni pestañas. Las patas son largas y delgadas; las delanteras parecen arqueadas por la anchura del pecho. La cola es larga, estrecha y dura al tacto."
            
        if name == "felix":
            datos = " son conocidos como las flores del verano y además son unas de las plantas más populares para decorar los espacios interiores durante la temporada."
            
        if name == "garfield":
            datos = " Estas hermosas plantas se cultivan como arbustos ornamentales en jardines de regiones cálidas y como plantas de interior en zonas frías."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getgenerolibroIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getgenerolibro")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["generolibro"].value
        if name == "misterio":
            datos = " La dama de blanco, Wilkie Collins, Los crímenes de la calle Morgue, Edgar Allan Poe, Otra vuelta de tuerca, Henry James"
            
        if name == "romance":
            datos = " Orgullo y prejuicio, de Jane Austen, El ruiseñor, de Kristin Hannah, Edenbrooke, de Julianne Donaldson"
            
        if name == "terror":
            datos = " El resplandor, Stephen King, Entrevista con el vampiro, Anne Rice, Guerra Mundial Z, Max Brooks."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gethaircutsIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gethaircuts")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["haircuts"].value
        if name == "bowl":
            datos = " corte de pelo sencillo en el que la parte delantera del cabello se corta con un flequillo recto (véase flequillo) y el resto del cabello se deja más largo, de la misma longitud en todo el contorno, o bien los lados y la parte trasera se cortan a la misma longitud corta."
            
        if name == "mullet":
            datos = " es un peinado en el que el pelo se corta más corto por delante, arriba y a los lados, pero es más largo por detrás."
            
        if name == "buzz":
            datos = " es un término que se utiliza para referirse a cualquiera de una variedad de peinados cortos, especialmente cuando la longitud del pelo es la misma en todas las partes de la cabeza."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gethogwartscasasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gethogwartscasas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["hogwartscasas"].value
        if name == "Hufflepuff":
            datos = " valora el trabajo duro, la dedicación, la paciencia, la lealtad y el juego limpio. Su animal emblemático es el tejón, su piedra preciosa representativa son los diamantes amarillos y sus colores el amarillo y el negro."
            
        if name == "Slytherin":
            datos = " valora la ambición, el liderazgo, la autoconservación, la astucia y el ingenio, y fue fundada por Salazar Slytherin. Su animal emblemático es la serpiente, su piedra preciosa representativa la esmeralda y sus colores el verde esmeralda y el plateado."
            
        if name == "Gryffindor":
            datos = " valora la valentía, la audacia, el valor y la caballerosidad. Su animal emblemático es el león, su piedra preciosa representativa, el rubí, y sus colores, el escarlata y el oro."
        
        if name == "Ravenclaw":
            datos = " valora la inteligencia, el conocimiento, la curiosidad, la creatividad y el ingenio. Su animal emblemático es el águila, su piedra preciosa representativa los zafiros y sus colores el azul y el bronce."
        
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gethojasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gethojas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["hojas"].value
        if name == "A4":
            datos = " formato estándar de uso internacional y es el que se usa más a menudo en nuestro día a día en nuestra vida escolar o laboral. La mayoría del papel multifunción o cuadernos y libretas que vendemos en nuestra papelería es en ese formato."
            
        if name == "oficio":
            datos = " 216 mm × 330 mm, de uso en: Colombia, Chile, Guatemala, El Salvador, Perú, Paraguay; distinto a legal u oficio americano."
            
        if name == "carta":
            datos = " 216 mm × 279 mm, algunas papeleras la denominan letter o carta americano."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getidiomasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getidiomas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["idiomas"].value
        if name == "polaco":
            datos = " es una lengua eslava del grupo occidental hablado principalmente en Polonia. Se escribe con el alfabeto latino, con gran uso de dígrafos y signos diacríticos extras."
            
        if name == "arabe":
            datos = " es una macrolengua de la familia semítica, como el arameo, el hebreo, el acadio, el maltés y similares. Es el quinto idioma más hablado en el mundo (número de hablantes nativos) y es oficial en veinte países y cooficial en al menos otros seis."
            
        if name == "estoniano":
            datos = " es una lengua fino-ugria hablada por alrededor de 1 100 000 personas que, en su gran mayoría, viven en Estonia."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getlibrosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getlibros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["libros"].value
        if name == "It":
            datos = " Cuenta la historia, en un juego de correspondencias con el pasado y el presente, de un grupo de siete amigos que son perseguidos por una entidad sobrenatural, al que llaman «Eso», que es capaz de cambiar de forma y se alimenta principalmente del terror que produce en sus víctimas."
            
        if name == "Armada":
            datos = " La historia sigue a un adolescente que juega un juego en línea sobre la defensa contra una invasión alienígena, sólo para descubrir que el juego es un simulador para prepararlo a él y a la gente de todo el mundo para la defensa en contra de una verdadera invasión alienígena."
            
        if name == "Dune":
            datos = " La historia comienza a más de 10 000 años en el futuro, en nuestra galaxia, en un gran imperio galáctico de estructura feudal. El Imperio se divide en cuasi-feudos o señoríos planetarios que son controlados por familias nobles, conocidas como Las Grandes Casas, que se agrupan en un gran consejo, llamado Landsraad, y rinden tributo al Emperador Padishah Shaddam IV, de la Casa Corrino. Otra de las instituciones es la Combine Honnete Ober Advancer Mercantiles, o CHOAM, una corporación universal para el desarrollo comercial controlada por el Emperador y las Grandes Casas, con la Cofradía Espacial y la Hermandad Bene Gesserit como socios sin derecho a voto."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmaderasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmaderas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["maderas"].value
        if name == "cedro":
            datos = " madera de color rojizo y un agradable olor dulce. Muy utilizada en cajoneras, cubiertas, tejas y en la construcción."
            
        if name == "pino":
            datos = " la madera de pino fácil de trabajar, barata y textura uniforme. Es habitualmente usada carpintería, paneles, muebles y molduras."
            
        if name == "abeto":
            datos = " madera de características similares a la del pino, ligera, alta resistencia a los químicos, buena elasticidad y sin resinas. Muy utilizada en revestimientos de paredes y techos."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmangakasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmangakas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["mangakas"].value
        if name == "Gege Akutami":
            datos = " mangaka japonés de la prefectura de Iwate en Japón y es mejor conocido por ser el creador de la serie Jujutsu Kaisen."
            
        if name == "Hirohiko Araki":
            datos = " mangaka japonés, principalmente es conocido por ser el creador de Jojo's Bizarre Adventure, el cual empezó a ser publicado en la revista Shōnen Jump de Shūeisha en 1986 y aún continúa en la revista Ultra Jump de la misma editorial."
            
        if name == "Hajime Isayama":
            datos = " mangaka japonés. Su primera serie, Shingeki no Kyojin (2009–2021), se convirtió en una de las series de manga más vendidas de todos los tiempos con 110 millones de copias en circulación hasta septiembre de 2022."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmariscosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmariscos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["mariscos"].value
        if name == "langosta":
            datos = " es un crustáceo decápodo de la familia Nephropidae. Generalmente habitan en aguas oscuras y frías, en donde hay rocas y otros lugares que les permite ocultarse de sus depredadores."
            
        if name == "pulpo":
            datos = " tiene simetría bilateral, con la boca y el pico situados en el punto central de sus ocho extremidades. Su cuerpo blando puede cambiar rápidamente de forma y textura, permitiendo que el animal se escurra a través de pequeños conductos o grietas."
            
        if name == "camaron":
            datos = " Son relativamente fáciles de encontrar en todo el mundo, tanto en agua dulce, como en agua salada. Como ejemplo, unas doscientas cuarenta especies de camarones viven tan solo en las aguas costeras tropicales del pacífico de América."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmueblesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmuebles")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["muebles"].value
        if name == "sillon":
            datos = " asiento con respaldo, implicando apoyos laterales para los brazos, comúnmente llamados con el nombre de brazos o apoyabrazos, y que adicionalmente aporta una mayor comodidad y espacio al usuario que un asiento convencional."
            
        if name == "silla":
            datos = " mueble que suele tener un respaldo, generalmente cuenta con tres o cuatro apoyos y su finalidad es la de servir de asiento a una persona."
            
        if name == "mesa":
            datos = " mueble compuesto de un tablero horizontal liso y sostenido a la altura conveniente, generalmente por una o varias patas, para diferentes usos."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmunicipiosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmunicipios")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["municipios"].value
        if name == "La Paz":
            datos = " se encuentra situado en la zona sur del estado y por consiguiente la Península de Baja California, tiene una extensión territorial total de 20.274,98 kilómetros cuadrados que representan el 27,51% de la extensión total de Baja California Sur."
            
        if name == "Los Cabos":
            datos = " Se localiza en el extremo sur de la península de Baja California, a 220 km al sur de La Paz. Su clima es desértico semiseco, caluroso en verano y templado en invierno; con una temperatura promedio anual de 26 °C."
            
        if name == "Loreto":
            datos = " se ubica en la parte central del estado mexicano de Baja California Sur. Su cabecera municipal es la ciudad de Loreto."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getmusicagenerosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getmusicageneros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["musicageneros"].value
        if name == "pop":
            datos = " Locked out of Heaven de Bruno Mars, Hold On de Justin Bieber, Save Your Tears de The Weeknd."
            
        if name == "rock":
            datos = " Here Comes The Sun de The Beatles, Under Pressure de Queen, Something In The Way de Nirvana."
            
        if name == "rap":
            datos = " Nonstop de Drake, Money Trees de Kendrick Lamar, Perfect de Logic."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getososIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getosos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["osos"].value
        if name == "grizzly":
            datos = " Es un animal solitario, excepto durante la temporada del desove del salmón, cuando se junta un enorme número de osos en arroyos y zonas costeras para alimentarse."
            
        if name == "pardo":
            datos = " Es un habitante característico de los bosques maduros de Europa, Asia templada y América del Norte."
            
        if name == "polar":
            datos = " Vive en el medio polar y zonas heladas del hemisferio norte. Es el único superdepredador del Ártico."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpaisesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpaises")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["paises"].value
        if name == "Canada":
            datos = " es un país soberano en América del Norte, cuya forma de gobierno es la monarquía parlamentaria federal. Su territorio está organizado en diez provincias y tres territorios."
            
        if name == "Turquia":
            datos = " es un país transcontinental, con la mayor parte de su territorio situado en Asia Occidental y una menor (al oeste del mar de Mármara) en Europa Oriental, que se extiende por toda la península de Anatolia y Tracia Oriental en la zona de los Balcanes."
            
        if name == "Finlandia":
            datos = " Está situado en el noreste de Europa. Tiene fronteras al oeste con Suecia, al este con Rusia y al norte con Noruega. Por el oeste y el sur está rodeada por el mar Báltico, que la separa de Suecia y Estonia, cruzando los golfos de Botnia y Finlandia."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpajarosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpajaros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pajaros"].value
        if name == "guacamaya":
            datos = " son aves del orden Psittaciformes y de la familia Psittacidae, muy llamativos por su colorido plumaje."
            
        if name == "carpintero":
            datos = " Tienen una distribución cosmopolita, con la excepción de Australia, Madagascar y las regiones polares extremas."
            
        if name == "colibri":
            datos = " seres nativos de casi todos los ecosistemas, bosques templados, selvas húmedas, desiertos, incluso en los picos más montañosos y altos de todo el continente americano."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpantallasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpantallas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pantallas"].value
        if name == "LG":
            datos = " Creada en 1947, asumió el nombre abreviado de LG en 1995. LG es una abreviatura de Lucky Goldstar en Corea del Sur, que ha sido traducido al inglés como Lucky Venus (Goldstar, estrella dorada en inglés)."
            
        if name == "Toshiba":
            datos = " compañía japonesa, con sede en Tokio, dedicada a la manufactura de aparatos eléctricos y electrónicos."
            
        if name == "Samsung":
            datos = " Se trata del mayor grupo empresarial surcoreano, con numerosas filiales que abarcan negocios como la electrónica de consumo, tecnología, finanzas, aseguradoras, construcción, biotecnología y sector servicios."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpapelIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpapel")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["papel"].value
        if name == "papel crepe":
            datos = " Las hebras se tuercen en S o en Z. Las irregularidades del tejido hacen que no se pueda estampar y que sea reversible."
            
        if name == "papel higienico":
            datos = " Su formato más común es el de un rollo, pero también es posible encontrarlo en paquetes formados por hojas rectangulares de un tamaño preestablecido."
            
        if name == "papel china":
            datos = " Es de textura lisa y es ideal para manualidades, envolturas, y decoración."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpeinadosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpeinados")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["peinados"].value
        if name == "afro":
            datos = " producido naturalmente por la textura de cabello afro que se caracteriza por formar una masa abultada de cabello que se mantiene sobre la parte superior del cráneo en una forma redonda."
            
        if name == "trenzas":
            datos = " tipo de estructura o patrón que se caracteriza por entrecruzar dos o más tiras de algún material fácilmente manipulable o flexible como alambre, material textil o cabello."
            
        if name == "cola alta":
            datos = " tipo de peinado sencillo en la estética del hombre y la mujer que se caracteriza por el agrupamiento de una sección de cabello en la parte trasera de la cabeza."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpelisgenerosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpelisgeneros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pelisgeneros"].value
        if name == "accion":
            datos = " John Wick, Logan, Batman Begins"
            
        if name == "suspenso":
            datos = " Jurassic Park, Inception, Signs"
            
        if name == "comedia":
            datos = " Toy Story, Back to the Future, Kingsman"
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getperifericosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getperifericos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["perifericos"].value
        if name == "monitor":
            datos = " principal dispositivo de salida (interfaz), que muestra datos o información a todos los usuarios."
            
        if name == "mouse":
            datos = " es un dispositivo apuntador utilizado para facilitar el manejo de un entorno gráfico en una computadora."
            
        if name == "teclado":
            datos = " dispositivo de entrada, en parte inspirado en el teclado de las máquinas de escribir, que utiliza un sistema de puntadas o márgenes, para que actúen como palancas mecánicas o interruptores electrónicos que envían toda la información a la computadora."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getperrosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getperros")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["perros"].value
        if name == "husky":
            datos = " Perros energéticos y atléticos, normalmente tienen un manto grueso doble que puede ser gris, negro, rojizo-cobre o blanco."
            
        if name == "corgi":
            datos = " Se ha desempeñado durante siglos como perro pastor, y se le considera uno de los perros más antiguos de Gran Bretaña."
            
        if name == "pug":
            datos = " Es un perro bajo y de aspecto cuadrado y compacto, la cabeza grande, redondeada y de aspecto sólido, está cubierta de pliegues; el hocico es cuadrado y chato; los ojos, grandes y oscuros; tiene las patas rectas y la cola rizada."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getplanetasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getplanetas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["planetas"].value
        if name == "Marte":
            datos = " es el cuarto planeta en orden de distancia al Sol y el segundo más pequeño del sistema solar, después de Mercurio."
            
        if name == "Jupiter":
            datos = " es el planeta más grande del sistema solar y el quinto en orden de lejanía al Sol."
            
        if name == "Saturno":
            datos = " es el sexto planeta del sistema solar contando desde el Sol, el segundo en tamaño y masa después de Júpiter y el único con un sistema de anillos visible desde la Tierra."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpokemongenIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpokemongen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pokemongen"].value
        if name == "pokemon tercera generacion":
            datos = " En estas nuevas versiones aparece una nueva región llamada Hoenn, y 135 nuevas especies de pokémon (desde Treecko hasta Deoxys), elevando el total de hasta 386 pokémon."
            
        if name == "pokemon segunda generacion":
            datos = " En estas versiones aparece una nueva región conocida como Johto, donde se habían descubierto 100 pokémon nuevos (desde Chikorita hasta Celebi), llevando un total de 251 hasta en ese entonces."
            
        if name == "pokemon primera generacion":
            datos = " La aventura en estas versiones transcurre en la región de Kanto, por lo que el nombre de esta región suele verse asociado a estos videojuegos de la primera generación. El número de pokémon de estas versiones es de 151, desde Bulbasaur hasta Mew."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpokemonjuegosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpokemonjuegos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pokemonjuegos"].value
        if name == "Pokemon Diamante":
            datos = " videojuego de rol que representa la cuarta generación de la saga de Pokémon, desarrollado por Game Freak y distribuido por Nintendo"
            
        if name == "Pokemon Rojo Fuego":
            datos = " videojuego lanzado para la consola portátil Game Boy Advance de Nintendo en octubre de 2004, siendo remake de Pokémon Rojo, lanzado en 1996."
            
        if name == "Pokemon HeartGold":
            datos = " videojuego para la videoconsola portátil Nintendo DS. Fue lanzado en septiembre de 2009 en Japón, y en marzo de 2010 en Europa y América. Se trata de un remake en conmemoración al décimo aniversario del lanzamiento de la version Pokémon Oro de 1999, que fue lanzado para la consola Game Boy Color."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getpokemontipoIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getpokemontipo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["pokemontipo"].value
        if name == "Veneno":
            datos = " Nidorina, Ekans, Gengar"
            
        if name == "Volador":
            datos = " Articuno, Scyther, Doduo"
            
        if name == "Dragon":
            datos = " Dratini, Bagon, Rayquaza"
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getprefecturasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getprefecturas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["prefecturas"].value
        if name == "Tokyo":
            datos = " ubicada en el centro este de la isla de Honshu, concretamente en la región de Kantō. Es actualmente la ciudad más poblada del mundo, en conjunto es una de las 47 prefecturas de Japón."
            
        if name == "Miyagi":
            datos = " está ubicada en la isla Honshu, Japón. La capital es Sendai. La prefectura de Miyagi fue parte de la provincia de Mutsu."
            
        if name == "Nagano":
            datos = " está ubicada en la isla de Honshū, Japón. La capital es la ciudad de Nagano. Nagano es una prefectura del interior y limita con más prefecturas que cualquier otra en Japón."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getreptilesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getreptiles")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["reptiles"].value
        if name == "tortuga":
            datos = " Reptiles caracterizados por tener un tronco ancho y corto, y un caparazón que protege los órganos internos de su cuerpo."
            
        if name == "caiman":
            datos = " Se distribuyen en las regiones subtropicales y tropicales de América, desde Florida hasta el sur de Sudamérica."
            
        if name == "serpiente":
            datos = " Algunas realizan mordeduras venenosas, como las cobras (Elapidae) y las víboras, para matar a sus presas y posteriormente ingerirlas."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getroedoresIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getroedores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["roedores"].value
        if name == "ardilla":
            datos = " especies de roedores esciuromorfos de la familia Sciuridae."
            
        if name == "hamster":
            datos = " e caracterizan por las bolsas expansibles, llamadas abazones, ubicadas en el interior de la boca y que van desde las mejillas hasta los hombros."
            
        if name == "raton":
            datos = " Su distribución original abarca Eurasia, África y Australia, aunque ahora es cosmopolita por su introducción por parte del hombre."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gettelasIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gettelas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["telas"].value
        if name == "poliester":
            datos = " es muy resistente a la humedad, a los productos químicos y a las fuerzas mecánicas. Se usa en la fabricación de fibras, recubrimientos de láminas, etc."
            
        if name == "algodon":
            datos = " fibra natural más importante que se produce en el mundo, su importancia empezó en el siglo XIX con el proceso de industrialización y hoy en día todavía representa casi la mitad del consumo mundial de fibras textiles."
            
        if name == "seda":
            datos = " fibra natural formada por proteínas, producidas por diversos gusanos al tejer capullos dentro de los cuales sus cuerpos sufren metamorfosis a polillas."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gettenisbrandsIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gettenisbrands")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["tenisbrands"].value
        if name == "Puma":
            datos = " empresa alemana fabricante de accesorios, ropa y calzado deportivo, cuya sede principal está en Herzogenaurach, Alemania."
            
        if name == "Adidas":
            datos = " compañía multinacional alemana fundada en 1949, con sede en Herzogenaurach, ciudad ubicada en Baviera."
            
        if name == "Nike":
            datos = " empresa multinacional estadounidense dedicada al diseño, desarrollo, fabricación y comercialización de equipamiento deportivo: balones, calzado, ropa, equipo, accesorios y otros artículos deportivos."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gettiposmangaIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gettiposmanga")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["tiposmanga"].value
        if name == "shojo":
            datos = " Las chicas jóvenes también tienen su propio estilo de manga, dirigido a un público femenino hasta los 18 años."
            
        if name == "seinen":
            datos = " Dirigidos a hombres mayores de edad, este tipo de historietas contiene mucha acción y aventura, con un contenido más violento e incluso algunos relatos eróticos y explícitos."
            
        if name == "shonen":
            datos = " Se trata de uno de los tipos de manga y anime más consumidos en Japón, dirigido a un público adolescente masculino."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class gettuberculosIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("gettuberculos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["tuberculos"].value
        if name == "zanahoria":
            datos = " La mayoría de sus variedades son de color naranja y lo que se consume habitualmente es la raíz tuberosa, aunque sus hojas también son aptas como alimento."
            
        if name == "rabano":
            datos = " Raiz carnosa que se obtiene de la planta que tiene el mismo nombre. Posee un sabor picante y se consume como hortaliza."
            
        if name == "patata":
            datos = " Originaria de los Andes y de nombre científico Solanum tuberosum, actualmente es uno de los alimentos más extendidos del planeta y el cuarto cultivo alimentario más extendido del mundo."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class getvegetalesIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type : (HandlerInput) -> bool
        return ask_utils.is_intent_name("getvegetales")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        name = handler_input.request_envelope.request.intent.slots["vegetales"].value
        if name == "betabel":
            datos = " Perteneciente a la familia de las amarantáceas, el betabel posee un sabor muy dulce que se aprovecha para la obtención de azúcar y su pulpa para colorantes. Esta hortaliza puede consumirse cruda o cocida, en jugos, licuados, ensaladas y postres."
            
        if name == "apio":
            datos = " Posee tallos estriados que forman una gruesa penca con hojas acuñadas. Toda la planta tiene un fuerte sabor acre, es decir, agrio. Aunque el blanqueo de los tallos en el cultivo hace que pierdan estas cualidades, adquiriendo un sabor más dulce y el característico aroma que al probarlo tiene un sabor diferente lo que lo convierte en un buen ingrediente de ensaladas y sopas."
            
        if name == "lechuga":
            datos = " aporta abundantes vitaminas y pequeñas dosis de minerales que enriquecen la dieta sin aportar apenas calorías. En las ensaladas es la reina y combina casi con todo."
            
        speak_output = datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

#-------------------------------------------------------------------------------

sb = SkillBuilder()

sb.add_request_handler(getactoresIntentHandler())
sb.add_request_handler(getanfibiosIntentHandler())
sb.add_request_handler(getanimalesacuaticosIntentHandler())
sb.add_request_handler(getanimalesaereosIntentHandler())
sb.add_request_handler(getanimalesterrestresIntentHandler())
sb.add_request_handler(getarteIntentHandler())
sb.add_request_handler(getbailesIntentHandler())
sb.add_request_handler(getbanderasIntentHandler())
sb.add_request_handler(getbasuratiposIntentHandler())
sb.add_request_handler(getbebidasIntentHandler())
sb.add_request_handler(getbotanasIntentHandler())
sb.add_request_handler(getcalzadoIntentHandler())
sb.add_request_handler(getcampingtiposIntentHandler())
sb.add_request_handler(getcarnecortesIntentHandler())
sb.add_request_handler(getciudadesIntentHandler())
sb.add_request_handler(getcoloresIntentHandler())
sb.add_request_handler(getcontinentesIntentHandler())
sb.add_request_handler(getdeportesIntentHandler())
sb.add_request_handler(getdesayunosIntentHandler())
sb.add_request_handler(getdibujoIntentHandler())
sb.add_request_handler(getdinosauriosIntentHandler())
sb.add_request_handler(getdirectoresIntentHandler())
sb.add_request_handler(getdragonesIntentHandler())
sb.add_request_handler(getelementosIntentHandler())
sb.add_request_handler(getescritoresIntentHandler())
sb.add_request_handler(getestadosIntentHandler())
sb.add_request_handler(getetniasIntentHandler())
sb.add_request_handler(getfloresIntentHandler())
sb.add_request_handler(getfrutasIntentHandler())
sb.add_request_handler(getfrutosrojosIntentHandler())
sb.add_request_handler(getgalaxiasIntentHandler())
sb.add_request_handler(getgatosIntentHandler())
sb.add_request_handler(getgenerolibroIntentHandler())
sb.add_request_handler(gethaircutsIntentHandler())
sb.add_request_handler(gethogwartscasasIntentHandler())
sb.add_request_handler(gethojasIntentHandler())
sb.add_request_handler(getidiomasIntentHandler())
sb.add_request_handler(getlibrosIntentHandler())
sb.add_request_handler(getmaderasIntentHandler())
sb.add_request_handler(getmangakasIntentHandler())
sb.add_request_handler(getmariscosIntentHandler())
sb.add_request_handler(getmueblesIntentHandler())
sb.add_request_handler(getmunicipiosIntentHandler())
sb.add_request_handler(getmusicagenerosIntentHandler())
sb.add_request_handler(getososIntentHandler())
sb.add_request_handler(getpaisesIntentHandler())
sb.add_request_handler(getpajarosIntentHandler())
sb.add_request_handler(getpantallasIntentHandler())
sb.add_request_handler(getpapelIntentHandler())
sb.add_request_handler(getpeinadosIntentHandler())
sb.add_request_handler(getpelisgenerosIntentHandler())
sb.add_request_handler(getperifericosIntentHandler())
sb.add_request_handler(getperrosIntentHandler())
sb.add_request_handler(getplanetasIntentHandler())
sb.add_request_handler(getpokemongenIntentHandler())
sb.add_request_handler(getpokemonjuegosIntentHandler())
sb.add_request_handler(getpokemontipoIntentHandler())
sb.add_request_handler(getprefecturasIntentHandler())
sb.add_request_handler(getreptilesIntentHandler())
sb.add_request_handler(getroedoresIntentHandler())
sb.add_request_handler(gettelasIntentHandler())
sb.add_request_handler(gettenisbrandsIntentHandler())
sb.add_request_handler(gettiposmangaIntentHandler())
sb.add_request_handler(gettuberculosIntentHandler())
sb.add_request_handler(getvegetalesIntentHandler())

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
