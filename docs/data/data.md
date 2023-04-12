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
  id : int
  version : int
  topic : string
  createDate : datetime
  artifacts : Artifact[]
  status : ReportStatus
  author : User
 }
 
 class Review
 {
  id : int
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
 
 enum ArtifactType
 {
  presentation
  thesis
  preparationRunVideo
  review
 }
 
 Report *-- "1..*" Artifact
 Report -- ReportStatus
 Review -- ReviewStatus
 Review -- Report
 Artifact -- ArtifactType
}

namespace Ordering {
 ProductOrder *-- OrderItem
 OrderItem *-- Product
 Product *-- ProductSpecificationRef
 ProductOrder *-- Party
}

namespace ProductCatalog {
 ShoppingCart.ProductSpecificationRef ..> ProductSpecification : ref
 Ordering.ProductSpecificationRef ..> ProductSpecification : ref
}

namespace CX {
 ShoppingCart.Customer ..> Customer : ref
 Ordering.Party ..> Customer : ref
}
@enduml
```
