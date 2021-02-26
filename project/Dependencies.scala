import sbt._

object Dependencies {

  object Akka {
    private val version = "2.6.8"
    val akkaActor = "com.typesafe.akka" %% "akka-actor-typed" % version
    val akkaActorTestkit = "com.typesafe.akka" %% "akka-actor-testkit-typed" % version % Test
    val akkaStream = "com.typesafe.akka" %% "akka-stream" % version
  }

  object AkkaHttp {
    private val version = "10.2.4"
    val akkaHttp = "com.typesafe.akka" %% "akka-http" % version
    val akkaHttpTestkit = "com.typesafe.akka" %% "akka-http-testkit" % version % Test
  }

  val logback = "ch.qos.logback" % "logback-classic" % "1.2.3"
  val scalatest = "org.scalatest" %% "scalatest" % "3.1.4" % Test
}
