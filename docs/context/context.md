# Контекст решения
<!-- Окружение системы (роли, участники, внешние системы) и связи системы с ним. Диаграмма контекста C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783261
-->
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(doc, "Докладчик", "Человек, который предоставляет доклад")
Person(rew, "Рецензент", "Человек, который оценивает доклад и предоставляет отзыв на него")
Person(lis, "Слушатель", "Человек, который посещает конференцию в качестве слушателя")
Person(adm, "Администратор", "Человек, который осуществляет управление конференцией")
Person(sup, "Инженер техподдержки", "Человек, который осуществляет техническое сопровождение системы")

System(rep, "Система конференций", "Система, предоставляющая возможность организации конференции")
System_Ext(onl, "Система видеоконференций", "Система, позволяющая проводить видеоконференции")

Rel(doc, rep, "Uses")
Rel(rew, rep, "Uses")
Rel(lis, rep, "Uses")
Rel(adm, rep, "Uses")
Rel(sup, rep, "Supports")
Rel(rep, onl, "Scheduling conferencies")
@enduml
```
