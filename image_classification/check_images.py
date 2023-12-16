#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Niloy Farhan
# DATE CREATED: Thu 14 Dec 2023
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir


# Main program function defined below
def main():
    start_time = time()
    end_time = time()
    tot_time = end_time - start_time

    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type=str, default='my_folder/',
                        help='path to the folder my_folder')

    parser.add_argument('--num', type=int, default=1,
                        help='Number (integer) input')
    in_args = parser.parse_args()

    print("Argument 1:", in_args.dir, " Argument 2:", in_args.num)

    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + str(int((tot_time % 3600) % 60)))


if __name__ == "__main__":
    main()


