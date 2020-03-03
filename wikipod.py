from feedgen.feed import FeedGenerator
import urllib3

def demo():
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title('Leonids Podcast')
    fg.description('New Podcast from Leonid Lezner')
    fg.link(href='https://wohnzimmer.fm/playground')
    fg.generator('Woowo')
    fg.podcast.itunes_explicit('no')
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.podcast.itunes_owner('John Doe', 'john@example.com')
    fg.podcast.itunes_image('cover.png')

    fe = fg.add_entry()
    fe.id('http://lernfunk.de/media/654321/1/file.mp3')
    fe.title('The First Episode')
    fe.description('Enjoy our first episode.')
    fe.enclosure('http://lernfunk.de/media/654321/1/file.mp3', '15', 'audio/mpeg')

    #fg.rss_str(pretty=True)

    fg.rss_file('podcast.xml', pretty=True)


def main():
    demo()


if __name__ == '__main__':
    main()