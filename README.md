# atlys-assesment
To Run-
 EXECUTE FILE setup.sh
   ./setup.sh
   
Usage-
  Scrape Products:
    The scraper.scrape() method fetches the product data and returns it as a list of dictionaries.

  Save Data:
    The scraper.save_data() method saves the scraped data to the database if there are changes detected in the product price.

  Notify:
    The scraper.notify() method provides a simple printout of how many products were scraped and saved.

Structure
  scraper.py: Contains the main scraping logic.
  database/: Holds models and schemas for database interaction.
  utils/: Utility functions such as retry decorators and caching logic.
  config.py: Configuration settings for the project.
