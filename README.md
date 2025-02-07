## Abstract

We will investigate playlists from various radios over the last few years.

This will involve scraping data from their websites, and transforming that data into a format suitable for analysis, possibly using some music website's API to normalize song/singer names and to find more details about the songs.

We will then create visualizations for various questions one can ask about music. Possible examples include:

- Are there songs or singers that appear much more often than others? If so, do they have something in common?
- Which languages do radios play songs in? Does this change for various countries? (for instance, do French radios play as much Italian music as Italian radios play French music?)
- Looking at playlists over time, did some characteristics change? For instance, can we spot trends in music styles?
- Some radios claim to play "nostalgic" music; what do they mean by that? Do they play from a moving window over the past, or is it always the same "old" songs?
- Can we find interesting trends by correlating this information with other websites, such as how many songs, albums or singers have an entry on Wikipedia?
- Some radio have program where they claim to be avant-garde, but do we see these songs in the main playlist a few month after?
- Also, in specific program, is the evolution similar to the main playlist or is it slower/faster?

## Data description

Depending on what the radios provide, we may have more or less information about songs. We will therefore use some music APIs such as Spotify to find out more details.

Ideally, we'd like to have:
- Song name
- Release information (name, date, type, ...)
- Artist data (name, creation date, usual type of music, famous or not, ...)
- Music type (rock, pop, folk, ...)
- Language

## Feasibility and Risks

We already investigated some Swiss radios, and thus know that it is possible to fetch their information using HTML scraping.

Time permitting, we will look into other radios, most likely by using HTML scraping as well.

## Deliverables

We will deliver data visualizations answering interesting, fun and random questions.

The challenge for visualizations is to make a human-friendly view of many variables: song type, popularity, language, release date, time at which they are played, ...

We can have a sort of sliding view overtime of the popularity of a song or an artist. Or the evolution of the most played song on each or every station.

## Timeplan

We hope to have finished parsing radio playlists by the end of classes, i.e. before Christmas.

We will then focus on analyzing data and visualizing it during the holidays.
