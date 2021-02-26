name := "michel"
organization := "net.rouly"
description := "michel.rouly.net"

homepage := Some(url("https://michel.rouly.net"))

scalaVersion := "2.13.5"

libraryDependencies ++= Seq(
  Dependencies.Akka.akkaActor,
  Dependencies.Akka.akkaActorTestkit,
  Dependencies.Akka.akkaStream,
  Dependencies.AkkaHttp.akkaHttp,
  Dependencies.AkkaHttp.akkaHttpTestkit,
  Dependencies.logback,
  Dependencies.scalatest,
)

artifactoryConnection := artifactoryCloud("jrouly")
