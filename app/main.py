from fastapi import FastAPI, Depends, HTTPException, status
from .scraping import Scraper
from utils.authentication import authenticate
from utils.cache import Cache
from .database.main import Database
app = FastAPI()
cache = Cache()
db = Database()

@app.post("/scrape")
async def start_scraping(pages: int = 1, proxy: str = None, token: str = Depends(authenticate)):
    global cache,db
    scraper = Scraper(pages=pages, proxy=proxy, cache=cache, db=db)
    scraped_data = scraper.scrape()
    scraper.save_data(scraped_data)
    scraper.notify(scraped_data)
    return {"message": "Scraping completed successfully"}
