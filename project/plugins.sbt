resolvers += Resolver.url("ivy-release-local", url(s"https://jrouly.jfrog.io/artifactory/ivy-release-local"))(Resolver.ivyStylePatterns)
addSbtPlugin("io.jrouly" % "sbt-artifactory" % "0.2.0")

addSbtPlugin("com.dwijnand" % "sbt-dynver" % "4.1.1")
