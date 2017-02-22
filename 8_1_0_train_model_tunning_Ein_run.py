import os
import csv
import sys
import random
import scipy
import numpy as np



workspace_path = '/home/irashadow/python_workspace/Kaggle_Comp/Santander/'

#train_read = open(workspace_path + '/train/model_pf02/cust_product_'+str(model_no)+'.train', 'r')
#Ein_read = open(workspace_path + '../liblinear-2.1/output/cust_product_'+str(model_no)+'_inv.Ein', 'r')

#model_no = 19
#if True:
for model_no in range(1, 25):

    train_data_path = './train/model_pf04/cust_product_'+str(model_no)+'.train'
    model_path = '../liblinear-2.1/model_save/cust_product_'+str(model_no)+'_inv.model'
    Ein_path = '../liblinear-2.1/output/cust_product_'+str(model_no)+'_inv.Ein'

    train_command = '../liblinear-2.1/./train -s 2 -c 2'
    predi_command = '../liblinear-2.1/./predict'


    #print os.system("pwd");
    os.system(train_command +' '+ train_data_path +' '+ model_path);
    os.system(predi_command +' '+ train_data_path +' '+ model_path +' '+ Ein_path);

