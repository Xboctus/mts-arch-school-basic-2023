# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783368
-->
## Контейнерная диаграмма

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="microservice")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")
AddElementTag("file_storage", $shape=RoundedBoxShape(), $bgColor="lightGrey", $fontColor="white")

Person(doc, "Докладчик", "Человек, который предоставляет доклад")
Person(rew, "Рецензент", "Человек, который оценивает доклад и предоставляет отзыв на него")
Person(lis, "Слушатель", "Человек, который посещает конференцию в качестве слушателя")
Person(adm, "Администратор", "Человек, который осуществляет управление конференцией")

System_Boundary(c, "Система конференций") {
Container_Boundary(report_context, "Сервис управления докладами") {
   Container(app_doc, "Клиентское веб-приложение", "html, JavaScript, Angular", "Портал докладчика")
   Container(app_rew, "Клиентское веб-приложение", "html, JavaScript, Angular", "Портал рецензента")
   Container(report_service, "Report Service", "Java, Spring Boot", "Сервис управления докладами", $tags = "microService")      
   ContainerDb(report_db, "Report Catalog", "PostgreSQL", "Хранение докладов", $tags = "storage")
   ContainerDb(report_s3, "Artifact Storage", "S3 (minio)", "Хранение артифактов", $tags = "file_storage")
  } 
  
 Container_Boundary(conference_context, "Сервис управления конференцией") {
   Container(app_adm, "Клиентское веб-приложение", "html, JavaScript, Angular", "Портал администратора конференции")
   Container(conference_service, "Conference Service", "Java, Spring Boot", "Сервис управления конференцией", $tags = "microService")      
   ContainerDb(conference_db, "Conference Inventory", "PostgreSQL", "Хранение метаданных конференции", $tags = "storage")
   
   Container(app_lis, "Клиентское веб-приложение", "html, JavaScript, Angular", "Портал слушателя")
  } 
}

System_Ext(video_system, "Streaming provider", "Платформа для онлайн стриминга видео")

Rel(doc, app_doc, "Работа с докладом", "HTTPS")
Rel(app_doc, report_service, "Управление докладом", "JSON, HTTPS")

Rel(rew, app_rew, "Работа с рецензией", "HTTPS")
Rel(app_rew, report_service, "Управление рецензией", "JSON, HTTPS")

Rel(report_service, report_db, "Сохранение метаданных докладов", "JDBC, SQL")
Rel(report_service, report_s3, "Сохранение артифактов докладов", "S3, HTTPS")

Rel(adm, app_adm, "Работа с параметрами конференции", "HTTPS")
Rel(app_adm, conference_service, "Управление рецензией", "JSON, HTTPS")

Rel(conference_service, report_service, "Включение докладов в конференцию", "JSON, HTTPS")
Rel(conference_service, conference_db, "Сохранение метаданных конференции", "JDBC, SQL")

Rel(lis, app_lis, "Просмотр конференции", "HTTPS")
Rel(lis, conference_service, "Сохранение комментариев", "HTTPS")
Rel(app_lis, video_system, "Встраивание плеера", "HTTPS")
Rel(conference_service, video_system, "Настройка видеоконференции по расписанию", "HTTPS")

Lay_R(doc, rew)
Lay_R(lis, adm)
Lay_D(rew, doc)

SHOW_LEGEND()
@enduml
```

## Список компонентов
| Компонент             | Роль/назначение                                                                                                                                  |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| Портал докладчика | Предоставляет интерфейс управления докладами (загрузка новых версий, просмотр рецензий, получения подтверждения включения доклада в конференцию) |
| Портал рецензента | Предоставляет интерфейс управления рецензиями (просмотр доклада, создание рецензии, обновление рецензии)                                         |
| Report Service | Предоставляет инструменты работы с докладами и рецензиями (сохранение, изменение, выгрузка)                                                      |
| Report Catalog | Хранилище метаинформации о докладах и рецензиях                                                                                                  |
| Artifact Storage | Хранилище артифактов (докладов, рецензий)                                                                                                        |
| Портал администратора конференции | Предоставляет интерфейс управления конференцией (отбор докладов, составление расписаний, заказ площадок)                                         |
| Conference Service | Предоставляет инструменты работы с конференцией                                                                                                  |
| Conference Inventory | Хранение данных о конференции                                                                                                                    |
| Портал слушателя | Предоставляет интерфейс для слушателя (подключение к конференции, обратная связь)                                                                |