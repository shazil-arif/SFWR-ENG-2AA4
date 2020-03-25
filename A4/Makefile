######################################
# Author: 	Joost Vandorp, S. Smith	 #
# Revised: 	Thursday, Feb 24, 2017	 #
# Description:	"MAKEFILE"		 #
######################################

# Assumes JUnit is installed
# Assumes CLASSPATH has been set for Junit

JFLAGS = -g
JCLASS = -cp ./src;.;%CLASSPATH%;/C:/Shazil/2AA4/arifs2/A3/src/junit-4.5.jar
#JCLASS = -cp ./src:.:$(CLASSPATH):/usr/share/java/junit4-4.5.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
	src/Board.java \
	src/PointT.java \
	src/TwoDotsBoard.java \
        src/Strategy.java \
        src/TimedStrategy.java \
        src/MovesStrategy.java \
        src/Color.java \
        src/BoardMoves.java \
        src/BoardController.java \
	src/BoardView.java \

MAIN = AllTests

default: classes

classes: $(CLASSES:.java=.class)

doc:
	doxygen doxConfig
	cd latex && $(MAKE)

test: src/$(MAIN).class
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

dots: src/BoardView.java
	$(JC) $(JCLASS) $(JFLAGS) src/BoardView.java
	$(JVM) $(JCLASS) BoardView

clean:
	rm -rf html
	rm -rf latex
	cd src
	rm **/*.class
