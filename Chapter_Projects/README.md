# Chapter Projects Setup Guide

This guide will help you set up your environment variables to successfully work with Chapter Projects.

## Environment Variables

1. Search for "Environment Variables" on your computer.
2. Select "Environment Variables" from the search results.
3. Locate the "PATH" variable in the "User variables" section.

In your "PATH" variable, ensure you have added the following three paths:

- `C:\Users\USER\AppData\Local\Programs\Python\Python3XX\Scripts\`
- `C:\Users\USER\AppData\Local\Programs\Python\Python3XX\`
- `C:\Users\USER\BatchFiles`

Replace `USER` with your username and `XX` with the Python version you have installed on your machine. Additionally, create a folder named "BatchFiles" at the specified location. This is where you should store all your Python scripts. Make sure to follow these instructions precisely.

## Storage Location

It's advisable to avoid storing your "PATH" to the files in an iCloud folder such as OneDrive. It's preferred to store it on your local machine. This guide assumes this storage arrangement.

## Mu Editor

Please note that this guide does not provide instructions for running programs in Mu Editor. If you want to use Mu Editor, consider reviewing Appendices A and B, as the Mu environment variables and third-party packages may differ from those on your local machine.

## Running Programs

Once you've set up your environment variables, you should be able to run your programs successfully both from the command prompt (`cmd`) and by pressing `WIN + r`. The batch files content should match the examples provided in the book.







