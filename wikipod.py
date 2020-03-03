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
    fg.podcast.itunes_subtitle('Subtitle of the podcast')
    fg.podcast.itunes_summary('Summary of the podcast')
    fg.podcast.itunes_author('Max Mustermann')
    fg.language('de-DE')
    fg.copyright('MIT')

    fe = fg.add_item()
    fe.id('http://lernfunk.de/media/654321/1/file.mp3')
    fe.title('The First Episode')
    fe.description('Enjoy our first episode.')
    fe.enclosure('http://lernfunk.de/media/654321/1/file.mp3', '15', 'audio/mpeg')
    fe.podcast.itunes_duration('00:01:30')
    fe.podcast.itunes_subtitle('Episode subtitle')
    fe.podcast.itunes_image('episode_cover1.png')
    fe.podcast.itunes_author('Max Mustermann 1')
    fe.podcast.itunes_summary('Summary 1')
    fe.pubDate('2017-02-05 13:26:58+01:00')

    fe = fg.add_item()
    fe.id('http://lernfunk.de/media/654321/2/file.mp3')
    fe.title('The Second Episode')
    #fe.podcast.itunes_title(fe.title())
    fe.description('Enjoy our second episode.')
    fe.enclosure('http://lernfunk.de/media/654321/2/file.mp3', '15', 'audio/mpeg')
    fe.podcast.itunes_duration('00:01:30')
    fe.podcast.itunes_subtitle('Episode subtitle')
    fe.podcast.itunes_image('episode_cover1.png')
    fe.podcast.itunes_author('Max Mustermann 2')
    fe.podcast.itunes_summary('Summary 2')
    fe.pubDate('2017-02-05 13:26:58+01:00')    

    #fg.rss_str(pretty=True)

    fg.rss_file('podcast.xml', pretty=True)

    '''
        channel/itunes:type
        item/itunes:title
        item/itunes:episodeType
        item/itunes:episode
        item/content:encoded
    '''


def main():
    demo()


if __name__ == '__main__':
    main()