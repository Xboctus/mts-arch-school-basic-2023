# Модель предметной области
<!-- Логическая модель, содержащая бизнес-сущности предметной области, атрибуты и связи между ними. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375782602

Используется диаграмма классов UML. Документация: https://plantuml.com/class-diagram 
-->

```plantuml
@startuml
' Логическая модель данных в варианте UML Class Diagram (альтернатива ER-диаграмме).
namespace Report {

 class Report
 {
  id : long
  version : int
  topic : string
  createDate : datetime
  artifacts : Artifact[]
  status : ReportStatus
  author : User
 }
 
 class Review
 {
  id : uuid
  createDate : datetime
  updateDate : datetime
  report : Report
  artifacts : Artifact[]
  status : ReviewStatus
  author : User
 }
 
 enum ReviewStatus
 {
  started
  submitted
 }

 enum ReportStatus
 {
  submitted
  onReview
  rejected
  approved
  candidate
  scheduled
  done
 }

 class Artifact
 {
  id : string
  type : ArtifactType
  link : string
 }
 
 class User
 {
  id : string
  login : string
  name : string
  role : string[]
 }
 
 enum ArtifactType
 {
  presentation
  thesis
  preparationRunVideo
  review
 }
 
 Report *-- "1..*" Artifact
 Report -- ReportStatus
 Report -- User
 Review -- ReviewStatus
 Review -- Report
 Review -- User
 Artifact -- ArtifactType
}

namespace Conference {

class Conference {
    id: uuid
    title: string
    reports: ReportRef[]
    status: ConferenceStatus
    schedule: Schedule
    onlineLink: string
    offlinePlace: OfflinePlace
}

class Schedule {
    id: uuid
    title: string
    scheduleItem: ScheduleItem[]
    status: ScheduleStatus
}

class ScheduleItem {
    id: uuid
    report: Report
    startTime: datetime
    duration: datetime
    feedback: Feedback[]
}

class Feedback {
    id: uuid
    user: User
    text: string
}


enum ScheduleStatus
 {
  created
  considered
  approved
  rejected
 }


enum ConferenceStatus
 {
  created
  prepared
  started
  finished
 }
 
 class OfflinePlace {
    id: uuid
    title: string
    address: Address
    contacts: Contact[]
    documents: Document[]
    bookingDate: datetime
}

class Address {
    id: uuid
    city: string
    index: string
    street: string
    building: string
    room: string
}

class Contact {
    id: uuid
    name: string
    phone: string
    email: string
}

class Document {
    id: uuid
    link: string
}

 Conference.Conference *--"1..*" Conference.ReportRef
 Conference.ReportRef ..> Report.Report : ref
 Conference -- ConferenceStatus
 Conference *-- "0..*" Schedule 
 Schedule -- ScheduleStatus
 Schedule *-- "0..*" ScheduleItem
 Conference.ScheduleItem -- Conference.ReportRef
 Conference -- OfflinePlace
 OfflinePlace -- Address
 OfflinePlace *-- "1..*" Contact
 OfflinePlace *-- "0..*" Document
 ScheduleItem *-- "0..*" Feedback
}

@enduml
```
