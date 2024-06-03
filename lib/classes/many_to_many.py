class Article:
    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError("author must be an instance of Author")

        if isinstance(magazine, Magazine):
            self.magazine = magazine
        else:
            raise ValueError("magazine must be an instance of Magazine")
        
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self.title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    def title(self):
        return self._title
 

class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def name(self):
        return self._name

    name = property(name)

    def articles(self):
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self.name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")  
        
    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return contributors

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

