import os
import time
import tqdm
import requests 
import pandas as pd 
from bs4 import BeautifulSoup
import banner

def get_images_urls(query):
    '''Parameters: (str) query: Description of the item.
    Construct a request and send it to google image, convert to 
    a soup in order to find the images and then extract links
    Return: List of google's icon image's link'''
    
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&tbm=isch"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    images = soup.find_all("img")
    return [link.get("src") for link in images][1:10]


def single_save_list_of_images(query, save_to_path=None):
    '''Parameters: (str) query: Description of the item
                    (save_to_path): Saving destination path
    Create a folder and save downloaded images inside, if not
    informed, will save to Pictures users folder'''
    
    links = get_images_urls(query)

    if save_to_path == None:
        save_to_path = os.path.expanduser('~\Pictures')
        print("\nNo destination folder informed, saving to 'Picture' user's folder")
    else:
        print(f'\nSaving images to destination folder:\n {save_to_path}/{query}')
    if not query in os.listdir(save_to_path):
        os.mkdir(os.path.join(save_to_path, query))
        
    for i in range(len(links)):
        f = open(f"{save_to_path}/{query}/{query}-{i}.jpg", "wb")
        f.write(requests.get(links[i]).content)
        f.close()
    return f'\n\nSuccessfully saved images to {save_to_path}'


def multiple_save_list_of_images(skus_csv, save_to_path):
    '''Parameters: (str) skus_csv: Csv file of one column,
                    (save_to_path): Saving destination path
    Create a folder and save downloaded images inside, if not
    informed, will save to Pictures users folder'''
    
    list_of_skus = [i for i in pd.read_csv(skus_csv, names=['0'])['0']]
    
    for i in tqdm.tqdm(range(len(list_of_skus))):
        links = get_images_urls(list_of_skus[i])
       
        if not list_of_skus[i] in os.listdir(save_to_path):
            os.mkdir(os.path.join(save_to_path, list_of_skus[i].replace(' ', '_')))
            
        for j in range(len(links)):
            f = open(f"{save_to_path}/{list_of_skus[i].replace(' ', '_')}/{list_of_skus[i].replace(' ', '_')}-{j}.jpg", "wb")
            f.write(requests.get(links[j]).content)
            f.close()
    
    return f'\nSuccessfully saved images to {save_to_path}'
        

if __name__ == "__main__":
    n_layout = 100
    # DESTINATION FOLDER PATH
    print('-'*n_layout)
    save_to_path = input("What is the destination folder's path?\nIf no path is provided, images will be saved in the 'Pictures' user's folder.\n")
    print('-'*n_layout)
    
    if (save_to_path == "") or (save_to_path == None):
        try:
            save_to_path = os.path.expanduser('~\Pictures').replace('\\', '/')
            print("Did not received destination folder. Saving to 'Picture' user's folder")
        except:
            print("Can not access to 'Pictures' folder. Maybe your OS language is not set on English")
            save_to_path = os.getcwd()
            print("Saving images at program file's location.")
    else:    
        try:
            os.listdir(save_to_path)
            print(f'Saving images to destination folder:\n {save_to_path}')
        except:
            print('Error in the destination folder path. Please double check and try again')
            print('Images will be saved at file\'s location')
            save_to_path = os.getcwd()
    
    
    # SINGLE OR MULTIPLE
    print('-'*n_layout)
    single_or_multiple = input("Are you looking for a single product or for multiple products?\n")
    print('-'*n_layout)
    while single_or_multiple not in ['single', 'multiple']:
        print('-'*n_layout)
        single_or_multiple = input("Not sure to understand your answer. Please respond with 'single' or 'multiple' and then hit 'Enter'.\nAre you looking for a single image product or for multiple images products?\n")
    
    if single_or_multiple == 'single':    
        # QUERY SINGLE
        try:
            print('-'*n_layout)
            query = input("What image are you looking for ?\n")
            print('-'*n_layout)
            query = str(query.strip().lower())
            single_save_list_of_images(query, save_to_path)
        except:
            print("Error: The query for the images is incorrect")
    
    
    if single_or_multiple == 'multiple':
        # LIST MULTIPLE
        print('-'*n_layout)
        list_skus = input("Insert your SKU list full path name, as a .csv file with 1 column\n")
        print('-'*n_layout)
        try:
            pd.read_csv(list_skus)
        except:
            print("Error with the file name path, please double check and try again")
            exit(0)
        
        multiple_save_list_of_images(list_skus, save_to_path)

    print('\n','#'*n_layout)
    print(' Program finished !')

