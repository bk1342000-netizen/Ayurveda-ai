
# scraper_charaka.py - Extract shlokas from public domain Charaka Samhita
import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_charaka_archive():
    """
    Scrapes Charaka Samhita from archive.org
    Source: https://archive.org/details/CharakaSamhita (public domain)
    """
    base_url = "https://archive.org/stream/CharakaSamhita"
    shlokas = []
    
    # Example: scrape Chikitsa Sthana chapters 1-30
    for chapter in range(1, 31):
        try:
            # This is template - actual URLs vary
            url = f"{base_url}/page/n{100 + chapter*10}/mode/1up"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                
                # Extract Sanskrit verses (Devanagari pattern)
                sanskrit_pattern = r'([\u0900-\u097F]+।[\u0900-\u097F।\s]+॥)'
                matches = re.findall(sanskrit_pattern, text)
                
                for i, verse in enumerate(matches[:10]):  # limit per chapter
                    shlokas.append({
                        "id": f"charaka_chi_{chapter}_{i}",
                        "sanskrit": verse.strip(),
                        "source": f"Charaka Samhita, Chikitsa Sthana {chapter}",
                        "chapter": chapter,
                        "verse_number": i,
                        "verification_needed": True,
                        "scraped_from": url
                    })
                    
            print(f"Chapter {chapter}: {len(matches)} verses found")
            
        except Exception as e:
            print(f"Error chapter {chapter}: {e}")
    
    return shlokas

def save_to_json(shlokas, filename="charaka_full_2000.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(shlokas, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(shlokas)} shlokas to {filename}")

if __name__ == "__main__":
    print("Starting Charaka Samhita scraper...")
    print("NOTE: This scrapes public domain text from archive.org")
    print("You must verify each shloka with a BAMS scholar")
    
    shlokas = scrape_charaka_archive()
    save_to_json(shlokas)
    
    # Also create CSV for easy review
    import pandas as pd
    df = pd.DataFrame(shlokas)
    df.to_csv("charaka_for_review.csv", index=False, encoding='utf-8')
    print("CSV created for Vaidya review")
