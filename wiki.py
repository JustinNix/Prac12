import wikipedia

def get_page_summary():
    page = input("enter a title or search phrase: ")
    while page.strip != "":
        try:
            wiki_page = wikipedia.page(page)
            print(wiki_page.title)
            print(wikipedia.summary(page))
            print(wiki_page.url)
            page = input("\n enter a title or search phrase: ")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    else:
        print("the end")

get_page_summary()