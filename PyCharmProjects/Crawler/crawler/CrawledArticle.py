class CrawledArticle:

    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

    def __str__(self):
        return self.emoji + ": " + self.title

    def to_csv(self):
        return [self.emoji, self.title, self.content, self.image]

    @staticmethod
    def csv_header():
        return ["Emoji", "Title", "Content", "ImageUrl"]
