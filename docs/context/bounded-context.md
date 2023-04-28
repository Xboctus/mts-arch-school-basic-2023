# Контекст решения
<!-- Окружение системы (роли, участники, внешние системы) и связи системы с ним. Диаграмма контекста C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783261
-->
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(doc, "Докладчик", "Человек, который предоставляет доклад")
Person(rew, "Рецензент", "Человек, который оценивает доклад и предоставляет отзыв на него")
Person(lis, "Слушатель", "Человек, который посещает конференцию в качестве слушателя")
Person(adm, "Администратор", "Человек, который осуществляет управление конференцией")
Person(sup, "Инженер техподдержки", "Человек, который осуществляет техническое сопровождение системы")

System_Boundary(c, "Система конференций") {
    System(report_service, "Report Service", "Сервис управления докладами")      
    System(conference_service, "Conference Service", "Сервис управления конференцией")      
}

System_Ext(onl, "Система видеоконференций", "Система, позволяющая проводить видеоконференции")

Rel(doc, report_service, "Uses")
Rel(rew, report_service, "Uses")
Rel(lis, conference_service, "Uses")
Rel(adm, conference_service, "Uses")
Rel(sup, conference_service, "Supports")
Rel(conference_service, onl, "Планирование конференций")
Rel(conference_service, report_service, "Получение информации о докладах")

Lay_R(conference_service, report_service)
Lay_R(doc, rew)
Lay_R(rew, lis)
Lay_R(lis, adm)
Lay_R(adm, sup)

SHOW_LEGEND()
@enduml
```
