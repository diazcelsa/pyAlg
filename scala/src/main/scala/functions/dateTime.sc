import java.time._

object dateTime {
  val zonedDateTime = ZonedDateTime.now
  val timestamp: Long = System.currentTimeMillis / 1000
  println(zonedDateTime)
  //DateTimeZone.setDefault(DateTimeZone.UTC)
  //DateTime.now.toString
}