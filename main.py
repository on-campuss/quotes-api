import typer

from web.app import app as web_app

app = typer.Typer()


@app.command()
def run(mode: bool = False):
    if mode:
        import uvicorn
        uvicorn.run(web_app, host="0.0.0.0", port=8000) 

    else:
        from scraper.quotes import fetch_quotes
        quotes = fetch_quotes()
        print(quotes)
        return {"quotes": quotes}





if __name__ == "__main__":
    app()