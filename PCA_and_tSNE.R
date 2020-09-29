####
# Le Gall Lab at Ragon Institute of MIT, MGH, and Harvard
# Ann Le
# Created: July 2018
# Updated: July 25, 2018
# R code to do PCA and T-SNE analyses and graphs
####

#directory path
path <- "/Users/Ann Le/Documents"
#set working directory
setwd(path)

#read in csv with header 
data <- read.csv(file="example.csv", header=TRUE, sep=",", stringsAsFactors=FALSE)
#print the data from the csv
data



#run pca on the data (no package needed because default "stats" package comes with this function)
data_pca <- prcomp(data, scale.=T)
#get summary of pca data
summary(data_pca)
#graph pca data
biplot(data_pca)



####install t-sne package and load it to make availabe
####more information on this package: https://cran.r-project.org/web/packages/Rtsne/Rtsne.pdf
####further information: https://www.rdocumentation.org/packages/Rtsne/versions/0.13/topics/Rtsne 
install.packages("Rtsne")
library(Rtsne)


#run t-sne algorithm on the data
data_tsne <- Rtsne(as.matrix(data))

#getting the 2 dimensional matrix
data_tsne_1 <- as.data.frame(data_tsne$Y)
data_tsne_1


####install ggplot2 package and load it to make avaliable
####more information on this package: https://cran.r-project.org/web/packages/ggplot2/ggplot2.pdf 
install.packages("ggplot2")
library(ggplot2)


####load RColorBrewer package to use
library(RColorBrewer)
#view all the different colors! :)
display.brewer.all()



#assign different colors based on first column types 
cols <- brewer.pal(n=7,"Set1")
cols


#graph t-sne data
plot(data_tsne_1, 
     col = cols,
     main="TSN-e Analysis", sub="Dataset for ...",
     col.main="red",
     xlab="tSNE 1", ylab="tSNE 2",
     pch = 1,
     cex = 2
)

#add a legend
legend("bottomleft", 
       title="Type",
       legend=c("beads","control","HDACi","IMA+beads","PKCa","IMA+PKCa","IMA"), 
       pch = 16,
       cex=0.75,
       col = cols,
       horiz=FALSE,
       text.col="black",
       ncol = 2
)


  