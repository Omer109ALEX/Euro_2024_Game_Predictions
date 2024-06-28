import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from tqdm import tqdm




def get_game_guesses(driver, game_id, rank):
    # Wait for the main content to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cycle'))
    )

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the game element by ID
    game_div = soup.find('div', {'id': game_id})
    if game_div:
        # Extract the game details
        data = game_div.find_all('span', {'class': 'ng-binding'})
        team1_name = data[1].text.strip()
        guess = data[2].text.strip()
        result = data[3].text.strip()
        team2_name = data[4].text.strip()

        guesses = {
            'rank': rank,
            #'team1': team1_name,
            #'team2': team2_name,
            #'result': result,
            'guess': guess
        }
    else:
        guesses = None

    return guesses


def navigate_and_collect_guesses(game_id, group, total_pages=50):
    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())

    all_guesses = []
    url = ""
    next_button_xpath = ""
    if group != "top" and group != "109":
        print("group need to be top or 109 only")
        return []
    if group == "top":
        url = "https://hevre.sport5.co.il/#/top-score"
        driver = webdriver.Chrome(service=service)
    elif group == "109":
        url = "https://hevre.sport5.co.il/#/group/665cc63c9e6263f82409e092"
        total_pages = 10
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("user-data-dir=C:\\Users\\97254\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("profile-directory=Default")  # Use the profile you want
        driver = webdriver.Chrome(service=service, options=options)




    try:
        rank = 1
        for page_num in tqdm(range(total_pages), desc=f'Processing'):
            if group == "top":
                next_button_xpath = f'/html/body/div[6]/div/div[2]/table/tbody/tr[{rank}]/td[3]'

            elif group == "109":
                next_button_xpath = f'/html/body/div[6]/div[1]/div[3]/div[{rank}]'


            driver.get(url)

            # Click the "Next" button to go to the next page
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, next_button_xpath))
            )
            next_button.click()

            # Wait for the page to load
            WebDriverWait(driver, 10).until(
                EC.staleness_of(next_button)
            )

            # Get guesses for the current page
            guesses = get_game_guesses(driver, game_id, rank)
            if guesses:
                all_guesses.append(guesses)

            # Prepare for the next rank
            rank = rank + 1


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

    return all_guesses


def plot_guesses(guesses, team1_name, team2_name, scheduled, save_path, game_id, to_show=False):
    # Extract the 'guess' values and 'rank' values
    guess_values = [guess['guess'] for guess in guesses]
    guess_ranks = [guess['rank'] for guess in guesses]

    # Count the occurrences of each guess
    guess_counts = Counter(guess_values)

    # Create a dictionary to store ranks for each guess
    guess_rank_dict = {guess: [] for guess in guess_values}
    for guess, rank in zip(guess_values, guess_ranks):
        guess_rank_dict[guess].append(rank)

    # Data for pie chart
    labels = list(guess_counts.keys())
    sizes = list(guess_counts.values())

    # Remove '- : -' from labels and sizes
    if '- : -' in labels:
        index = labels.index('- : -')
        labels.pop(index)
        sizes.pop(index)

    # Categorize labels
    equal_labels = []
    greater_labels = []
    less_labels = []
    special_labels = []

    for label in labels:
        if ' : ' in label:
            score1, score2 = map(int, label.split(' : '))
            if score1 == score2:
                equal_labels.append(label)
            elif score1 > score2:
                greater_labels.append(label)
            else:
                less_labels.append(label)
        else:
            special_labels.append(label)

    # Sort labels within each category
    equal_labels.sort()
    greater_labels.sort()
    less_labels.sort()

    # Combine sorted labels
    sorted_labels = equal_labels + greater_labels + less_labels + special_labels

    # Get sorted sizes
    sorted_sizes = [guess_counts[label] for label in sorted_labels]

    # Define color maps for each condition
    color_map_equal = plt.cm.Blues(np.linspace(0.3, 0.7, len(equal_labels)))
    color_map_greater = plt.cm.Greens(np.linspace(0.3, 0.7, len(greater_labels)))
    color_map_less = plt.cm.Reds(np.linspace(0.3, 0.7, len(less_labels)))
    color_special = plt.cm.Purples(np.linspace(0.3, 0.7, len(special_labels)))  # Color for special cases

    # Combine color maps
    colors = np.concatenate([color_map_equal, color_map_greater, color_map_less, color_special])

    scheduled = scheduled.split(" ")[0]
    title = f"{team1_name}_{team2_name}_{scheduled}"

    # Create pie chart
    plt.figure(figsize=(10, 7))
    wedges, texts, autotexts = plt.pie(sorted_sizes, labels=sorted_labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Annotate the ranks for each guess outside the pie chart
    for i, label in enumerate(sorted_labels):
        rank_info = f"Ranks: {guess_rank_dict[label]}"
        angle = (wedges[i].theta2 + wedges[i].theta1) / 2
        x = np.cos(np.radians(angle))
        y = np.sin(np.radians(angle))
        plt.annotate(rank_info, xy=(x, y), xytext=(1.3 * x, 1.3 * y),
                     textcoords='data', ha='center', va='center', fontsize=8,
                     bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

    # Construct the file name and save the plot
    game_name = f"{game_id}.png"
    full_path = os.path.join(save_path, game_name)
    plt.savefig(full_path)

    if to_show:
        # Show the pie chart
        plt.show()

