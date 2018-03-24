#random forest classifier in R
install.packages('rfPermute')
install.packages('randomForest')
library(randomForest)
library(rfPermute)

infile <- read.table(file="/path/to/input/trainingset.csv", header=TRUE, sep=",")
trainingset <- as.matrix(infile)
c1 <- c("positive", "positive", "positive", "positive", "positive", "negative", "negative", "negative", "negative", "negative")
classifications <- as.factor(c1)

set.seed(24)

clf.rfP <- rfPermute(x=trainingset, y=classifications, ntree=5000, importance=TRUE)

clf.rfP
plot(clf.rfP)
varImpPlot(clf.rfP)

plotNull(clf.rfP)
plot(rp.importance(clf.rfP, scale = FALSE))
