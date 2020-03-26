a <- strftime(Sys.time(), "%a %b %d %Y %H %M")
write.csv(a, paste0('D:\\doc\\Amazon Work\\Jenkins\\Testing\\',a,"\\",a,'.csv'))