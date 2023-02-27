#!/usr/bin/env python
# coding: utf-8
# Created by Jithin Mathew on 02/27/2023

from glob import glob
from tqdm import tqdm
import random as r
from termcolor import colored
import os
from shutil import copy


def create_outputFolder_structure(output_folder):
    print(colored("creating YOLO train directory structure", "yellow"))
    if os.path.exists(output_folder+"\\"+"images"):
        pass
    else:
        os.mkdir(output_folder+"\\"+"images")
        os.mkdir(output_folder+"\\"+"images"+"\\"+"train")
        os.mkdir(output_folder+"\\"+"images"+"\\"+"val")
        
    if os.path.exists(output_folder+"\\"+"labels"):
        pass
    else:
        os.mkdir(output_folder+"\\"+"labels")
        os.mkdir(output_folder+"\\"+"labels"+"\\"+"train")
        os.mkdir(output_folder+"\\"+"labels"+"\\"+"val")
    print(colored("Directories created", "green"))

def remove_mismatch(images, labels, input_folder):
    images_ = set([os.path.basename(_).rstrip('.jpg') for _ in images])
    labels_ = set([os.path.basename(_).rstrip('.txt') for _ in labels])

    if images_ - labels_ is not None:
        temp = images_ - labels_
        for _ in temp:
            os.remove(input_folder+"\\"+_+".jpg") #change the image file extension
            print(_+".jpg files removed")
    if labels_ - images_ is not None:
        temp = labels_ - images_
        for _ in temp:
            os.remove(input_folder+"\\"+_+".txt") #change the xml file extension
            print(_+".txt files removed")
            
def validate_dataset(output_folder):
    train_images = glob(output_folder+"\\"+"images\\train\\"+"*.jpg")
    train_labels = glob(output_folder+"\\"+"labels\\train\\"+"*.txt")
    
    val_images = glob(output_folder+"\\"+"images\\val\\"+"*.jpg")
    val_labels = glob(output_folder+"\\"+"labels\\val\\"+"*.txt")
    
    if len(train_images) & len(train_labels) & len(val_images) & len(val_labels) > 0:
        if len(train_images) == len(train_labels):
            print(colored("Training data is validated :"+str(len(train_images)),"green"))
        else:
            print(colored("Training data is corrupt","red"))
        if len(val_images) == len(val_labels):
            print(colored("Validation data is validated :" +str(len(val_images)),"green"))
        else:
            print(colored("Validation data is corrupt","red"))
    else:
        print(colored(r"Data missing from one of the folders [train images:"+ str(len(train_image)+ "train labels :"+ str(len(train_labels))+ "val images :"+  len(val_images) + "val labels :"+  len(val_labels)), "red"))
    

# reading the files from folder
input_folder = r"enter_input source folder here"
output_folder = r"enter desired output folder here"
# set the train test ratio here
ratio = 0.9 
    
def generate_dataset(input_folder, output_folder, ratio):
    #default ration for splitting data into training and testing will be 90:10
    
    # read imgaes from the input folder 
    images = glob(input_folder+"\\"+"*.jpg") 
    # read labels from the input folder 
    labels = glob(input_folder+"\\"+"*.txt")
    
    # create a temp list ot hold the images/label names to avoid copying the same data twice
    temp_list = []
    val_list = []
    train_sample_no = round((len(images)*(ratio*100))/100)

    if len(images) == len(labels): 
        if len(images) & len(labels) > 0:
            print(colored("creating dataset with 90:10 ratio...","yellow"))
            print(colored("Validating directory structure","yellow"))
            create_outputFolder_structure(output_folder)
            val_list = images
            print(colored(str(train_sample_no) + " random images and labels picked for training set","yellow"))
            for _ in tqdm(range(train_sample_no)):
                src = r.choice(images)
                val_list.remove(src)
                copy(src, os.path.join(output_folder+"\\"+"images\\train\\"+os.path.basename(src)))
                copy(os.path.dirname(src)+"\\"+os.path.basename(src).rstrip('.jpg')+".txt", os.path.join(output_folder+"\\"+"labels\\train\\"+os.path.basename(src).rstrip('.jpg')+'.txt'))
            print(colored("Generating Val dataset with remaining "+str(len(images)-round((len(images)*(ratio*100))/100)),"green"))
            print(colored(str(len(val_list)) + " images and labels picked for validation set","yellow"))
            for _ in tqdm(val_list):
                copy(_, os.path.join(output_folder+"\\"+"images\\val\\"+os.path.basename(_)+'.jpg'))
                copy(os.path.dirname(_)+"\\"+os.path.basename(_).rstrip('.jpg')+".txt", os.path.join(output_folder+"\\"+"labels\\val\\"+os.path.basename(_).rstrip('.jpg')+'.txt'))
            print(colored(r"data generation complete \n validating generated dataset","green"))
            validate_dataset(output_folder)
        else:
            print(colored(r"no images or labels found","red"))
    elif len(images) != len(labels):
        print(colored("images and labels mismatch found, \n make sure the no images and no of labels match + [images:" + str(len(images))+ " labels :"+ str(len(labels)) + r"]", "red"))
        clean_folder = input(r"remove mismatching files and proceed? [Y\N]")
        if clean_folder.lower() == "y":
            remove_mismatch(images, labels, input_folder)
            print(colored("repeating the dataset generation...","green"))
            generate_dataset(input_folder, output_folder, ratio)
        else:
            pass
    else:
        print(colored(r"no images or labels found","red"))
        print(len(images), len(labels))

generate_dataset(input_folder, output_folder, ratio)