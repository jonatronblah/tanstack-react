
# build the model
source("functions.R")

#* @get /endpoint
get_output <- function(user_input){
  
  # convert the input to a number
  user_input <- as.numeric(user_input)
  
  test(user_input)
}