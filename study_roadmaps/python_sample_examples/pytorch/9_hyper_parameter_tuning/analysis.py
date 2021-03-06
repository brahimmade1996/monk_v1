import os
import sys
sys.path.append("../../../monk/");
import psutil

from pytorch_prototype import prototype



################################################## Foldered - Train Dataset #########################################################
ptf = prototype(verbose=1);
ptf.Prototype("sample-project-1", "sample-experiment-1");


ptf.Default(dataset_path="../../../monk/system_check_tests/datasets/dataset_cats_dogs_train", 
    			model_name="resnet18", freeze_base_network=True, num_epochs=2);


ptf.Train();

######################################################################################################################################





################################################Learning Rate Analysis################################################################
# Analysis Project Name
analysis_name = "analyse_learning_rates"

# Learning rates to explore																			
lrs = [0.1, 0.05, 0.01, 0.005, 0.0001];		

# Num epochs for each experiment to run														
epochs=2				

# Percentage of original dataset to take in for experimentation																			
percent_data=100	

# "keep_all" - Keep all the sub experiments created
# "keep_non" - Delete all sub experiments created																				
analysis = ptf.Analyse_Learning_Rates(analysis_name, lrs, percent_data, num_epochs=epochs, state="keep_none"); 


#As per results set the apropriate learning rate
ptf.update_learning_rate(0.005);
######################################################################################################################################




################################################ Input Size analysis #################################################################
# Analysis Project Name
analysis_name = "analyse_input_sizes";

# Input sizes to explore	
input_sizes = [128, 256, 512];

# Num epochs for each experiment to run	
epochs=5;

# Percentage of original dataset to take in for experimentation
percent_data=60;

# "keep_all" - Keep all the sub experiments created
# "keep_non" - Delete all sub experiments created	
analysis = ptf.Analyse_Input_Sizes(analysis_name, input_sizes, percent_data, num_epochs=epochs, state="keep_none"); 


#As per results set the apropriate input size
ptf.update_input_size(256);
######################################################################################################################################




################################################ Batch Size analysis #################################################################
# Analysis Project Name
analysis_name = "analyse_batch_sizes";

# Batch sizes to explore
batch_sizes = [4, 8, 16, 32];

# Num epochs for each experiment to run	
epochs = 5;

# Percentage of original dataset to take in for experimentation
percent_data = 70;

# "keep_all" - Keep all the sub experiments created
# "keep_non" - Delete all sub experiments created	
analysis = ptf.Analyse_Batch_Sizes(analysis_name, batch_sizes, percent_data, num_epochs=epochs, state="keep_none"); 


#As per results set the apropriate batch size
ptf.update_batch_size(256);
######################################################################################################################################



################################################ Model analysis #################################################################
# Analysis Project Name
analysis_name = "analyse_models";

# Models to analyse
# First element in the list- Model Name
# Second element in the list - Boolean value to freeze base network or not
# Third element in the list - Boolean value to use pretrained model as the starting point or not
models = [["resnet18", True, True], ["resnet34", False, True], ["resnet50", True, False]];  

# Num epochs for each experiment to run	
epochs=10;

# Percentage of original dataset to take in for experimentation
percent_data=90;

# "keep_all" - Keep all the sub experiments created
# "keep_non" - Delete all sub experiments created
analysis = ptf.Analyse_Models(analysis_name, models, percent_data, num_epochs=epochs, state="keep_none"); 


#As per results set the apropriate model
ptf.update_model_name("resnet50_v1");
ptf.update_freeze_base_network(True);
ptf.update_use_pretrained(True);
######################################################################################################################################





################################################ Optimizers analysis #################################################################
# Analysis Project Name
analysis_name = "analyse_optimizers";

# Optimizers to explore
optimizers = ["sgd", "adam", "adagrad"];   #Model name, learning rate

# Num epochs for each experiment to run	
epochs = 10;

# Percentage of original dataset to take in for experimentation
percent_data = 90;

# "keep_all" - Keep all the sub experiments created
# "keep_non" - Delete all sub experiments created
analysis = ptf.Analyse_Optimizers(analysis_name, optimizers, percent_data, num_epochs=epochs, state="keep_none"); 


#As per results set the appropriate 
ptf.optimizer_adam(0.005);
######################################################################################################################################




#################################################### Train the experiment with set parameters ########################################
ptf.Train();
######################################################################################################################################
