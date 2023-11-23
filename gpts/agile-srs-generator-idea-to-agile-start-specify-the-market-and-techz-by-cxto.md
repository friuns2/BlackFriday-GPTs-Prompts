
[![Agile SRS Generator - idea to agile start | Specify the market and techz by cxto](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_11.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22jFR4qK5rl6Ljed271z-FP%22%2C%22flow%22%3Atrue%7D%7D)
# Agile SRS Generator - idea to agile start | Specify the market and techz by cxto | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22jFR4qK5rl6Ljed271z-FP%22%2C%22flow%22%3Atrue%7D%7D)
[BDD/TDD/ATDD]

- Software Requeriments Specification -

Template layers of generating an SRS document from a generated startup idea. The document is made in such a way that it is easy to export and import to other agile development environments.



lkdn: https://www.linkedin.com/in/ignaciodelcorro/

# Prompt

```
output requeriments: Generate a block code of markdown lang with all the generated document as output and witouth explain. In the ocurrence of cucumber and mermaid code blocks should be inside "~~~" instead of the classical notation of markdown sign block codes. The total generated text must be in the language {{ Lang }} the requirements must have an Index section with the different parts in the document named as an formal SRS but all the text is inside a single block of markdown code with markdown lang. 

- SRS of a Software product idea of the {{ Market Area }} using {{ Techsz }}. The document contain use case diagrams, cucumber gherkin description with reserved words in english language, sequence diagrams, and class diagrams in the specified syntax fact at the start of the request.
```

## Conversation

**ASSISTANT**: ~~~

# Índice

1. Introducción

2. Requisitos de usuario

3. Requisitos del sistema

4. Casos de uso

5. Diagramas

    - 5.1 Diagramas de casos de uso

    - 5.2 Diagramas de secuencia

    - 5.3 Diagramas de clases

6. Restricciones

7. Supuestos y dependencias

8. Apéndice



## 1. Introducción

Este documento describe los requisitos para el desarrollo de una plataforma de orientación vocacional utilizando SaaS, Next y API RoR.



## 2. Requisitos de usuario

- Los usuarios deben poder crear y personalizar perfiles.

- Los usuarios pueden buscar recursos educativos y profesionales en línea.

- Los usuarios pueden conectarse con mentores y otros usuarios para obtener asesoramiento y orientación.

- Los usuarios pueden programar y participar en eventos relacionados con la orientación vocacional.



## 3. Requisitos del sistema

- La plataforma debe ser accesible a través de un navegador web.

- La plataforma debe ser compatible con dispositivos móviles.

- La plataforma debe ser segura y proteger la información del usuario.

- La plataforma debe tener una interfaz de programación de aplicaciones (API) que permita la integración con otras aplicaciones.



## 4. Casos de uso

### CU-01: Crear perfil

Como un usuario nuevo, quiero crear un perfil para utilizar la plataforma y guardar mi información personal.



~~~gherkin

Dado que soy un usuario nuevo

Cuando accedo a la plataforma

Entonces veo un formulario para ingresar mis datos personales

Y puedo guardar mi información al hacer clic en "Guardar"

~~~



### CU-02: Buscar recursos

Como un usuario registrado, quiero buscar recursos educativos y profesionales para ayudarme en mi orientación vocacional.



~~~gherkin

Dado que soy un usuario registrado

Cuando ingreso a la plataforma

Entonces veo una barra de búsqueda donde puedo ingresar palabras clave para encontrar recursos relacionados con la orientación vocacional

Y puedo ver los resultados de búsqueda que coinciden con mis palabras clave

~~~



### CU-03: Conectar con mentores

Como un usuario registrado, quiero conectarme con mentores y otros usuarios para obtener asesoramiento y orientación.



~~~gherkin

Dado que soy un usuario registrado

Cuando ingreso a la plataforma

Entonces puedo buscar mentores disponibles y ver su información de contacto

Y puedo enviar mensajes a los mentores seleccionados

~~~



### CU-04: Programar eventos

Como un usuario registrado, quiero programar y participar en eventos relacionados con la orientación vocacional.



~~~gherkin

Dado que soy un usuario registrado

Cuando ingreso a la plataforma

Entonces puedo ver una lista de eventos disponibles y sus detalles

Y puedo registrarme para participar en el evento haciendo clic en "Registrarse"

~~~



## 5. Diagramas

### 5.1 Diagramas de casos de uso

![Diagrama de casos de uso](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBDeXN0TmFtZSAtLT4gQ3UtMDE6IFJlY2VpdmVyXG4gICAgQ3UtMDEgLS0-IEN1LTAyOiBBcHAvUmVzb3VyY2VzXG4gICAgQ3UtMDEgLS0-IEN1LTAzOiBTZXJ2aWNlcy9BZGRyZXNzXG4gICAgQ3UtMDIgLS0-IFN1YmplY3Q6IFRvcGljcy9EaWFncmFtXG4gICAgQ3UtMDMgLS0-IE1ldGFkYXRhczogU3RhcnRlZCBNYXAgRmlsZSBjb250cm9sbGVyIFJlbGVhc2VkXG4gICAgQ3UtMDQgLS0-IFN1cGVyQ29kZTogU3VwZXJDb2RlclxuICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRiLW1lcm1haWQifX0)



### 5.2 Diagramas de secuencia

~~~mermaid

sequenceDiagram

    participant Usuario

    participant Plataforma

    Usuario


