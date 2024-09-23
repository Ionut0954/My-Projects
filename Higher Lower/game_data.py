"""
The list below contains 50 celebrities, each represented by a dictionary with the following keys:

name: The name of the celebrity.

follower_count: The number of followers the celebrity has on Instagram, ranging between 10 and 30 million, expressed as exact integers.

description: A short description of the celebrity's profession (e.g., "actor", "singer", "footballer").

country: The celebrity's country of origin.

"""

data = [
    {
        'name': 'Dua Lipa',
        'follower_count': 29182739,
        'description': 'Singer',
        'country': 'UK'
    },
    {
        'name': 'Jason Momoa',
        'follower_count': 18026392,
        'description': 'Actor',
        'country': 'USA'
    },
    {
        'name': 'Bruno Mars',
        'follower_count': 25839128,
        'description': 'Singer',
        'country': 'USA'
    },
    {
        'name': 'Chris Hemsworth',
        'follower_count': 26394018,
        'description': 'Actor',
        'country': 'Australia'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 29183927,
        'description': 'Model',
        'country': 'USA'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 27182736,
        'description': 'Singer',
        'country': 'Canada'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 29284027,
        'description': 'Model',
        'country': 'USA'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 22837192,
        'description': 'Actress',
        'country': 'UK'
    },
    {
        'name': 'Priyanka Chopra',
        'follower_count': 21384729,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Gal Gadot',
        'follower_count': 22176493,
        'description': 'Actress',
        'country': 'Israel'
    },
    {
        'name': 'David Beckham',
        'follower_count': 25837281,
        'description': 'Former footballer',
        'country': 'UK'
    },
    {
        'name': 'Will Smith',
        'follower_count': 19283746,
        'description': 'Actor',
        'country': 'USA'
    },
    {
        'name': 'LeBron James',
        'follower_count': 29982736,
        'description': 'Basketball player',
        'country': 'USA'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 20472839,
        'description': 'Media personality',
        'country': 'USA'
    },
    {
        'name': 'Drake',
        'follower_count': 27983147,
        'description': 'Rapper',
        'country': 'Canada'
    },
    {
        'name': 'Zendaya',
        'follower_count': 24836271,
        'description': 'Actress and singer',
        'country': 'USA'
    },
    {
        'name': 'Shakira',
        'follower_count': 19746281,
        'description': 'Singer',
        'country': 'Colombia'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 22782931,
        'description': 'Rapper and singer',
        'country': 'USA'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 20937461,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Chris Evans',
        'follower_count': 19837481,
        'description': 'Actor',
        'country': 'USA'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 28374612,
        'description': 'Comedian and actor',
        'country': 'USA'
    },
    {
        'name': 'Gordon Ramsay',
        'follower_count': 19384726,
        'description': 'Chef',
        'country': 'UK'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 22192736,
        'description': 'Singer',
        'country': 'USA'
    },
    {
        'name': 'Conor McGregor',
        'follower_count': 17392746,
        'description': 'MMA fighter',
        'country': 'Ireland'
    },
    {
        'name': 'Zlatan Ibrahimović',
        'follower_count': 19923761,
        'description': 'Footballer',
        'country': 'Sweden'
    },
    {
        'name': 'Hugh Jackman',
        'follower_count': 17736281,
        'description': 'Actor',
        'country': 'Australia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 21284726,
        'description': 'Singer',
        'country': 'Cuba'
    },
    {
        'name': 'Snoop Dogg',
        'follower_count': 18192745,
        'description': 'Rapper',
        'country': 'USA'
    },
    {
        'name': 'Mark Wahlberg',
        'follower_count': 17284631,
        'description': 'Actor',
        'country': 'USA'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 19837461,
        'description': 'Singer',
        'country': 'USA'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 19837491,
        'description': 'Actor',
        'country': 'USA'
    },
    {
        'name': 'Cristina Ferreira',
        'follower_count': 18472619,
        'description': 'TV Presenter',
        'country': 'Portugal'
    },
    {
        'name': 'Tom Holland',
        'follower_count': 19384736,
        'description': 'Actor',
        'country': 'UK'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 21738291,
        'description': 'Singer and actor',
        'country': 'USA'
    },
    {
        'name': 'Post Malone',
        'follower_count': 20192736,
        'description': 'Rapper and singer',
        'country': 'USA'
    },
    {
        'name': 'Khabib Nurmagomedov',
        'follower_count': 22384716,
        'description': 'MMA fighter',
        'country': 'Russia'
    },
    {
        'name': 'Vanessa Hudgens',
        'follower_count': 15182736,
        'description': 'Actress and singer',
        'country': 'USA'
    },
    {
        'name': 'Lili Reinhart',
        'follower_count': 12483716,
        'description': 'Actress',
        'country': 'USA'
    },
    {
        'name': 'Anitta',
        'follower_count': 16293746,
        'description': 'Singer',
        'country': 'Brazil'
    },
    {
        'name': 'Ashley Tisdale',
        'follower_count': 11192746,
        'description': 'Actress and singer',
        'country': 'USA'
    },
    {
        'name': 'Cara Delevingne',
        'follower_count': 21736282,
        'description': 'Model and actress',
        'country': 'UK'
    },
    {
        'name': 'Millie Bobby Brown',
        'follower_count': 16837491,
        'description': 'Actress',
        'country': 'UK'
    },
    {
        'name': 'Eva Longoria',
        'follower_count': 17482736,
        'description': 'Actress',
        'country': 'USA'
    },
    {
        'name': 'Jessica Alba',
        'follower_count': 19682736,
        'description': 'Actress and businesswoman',
        'country': 'USA'
    },
    {
        'name': 'Blake Lively',
        'follower_count': 18372629,
        'description': 'Actress',
        'country': 'USA'
    },
    {
        'name': 'Orlando Bloom',
        'follower_count': 13746283,
        'description': 'Actor',
        'country': 'UK'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 29283719,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Ellie Goulding',
        'follower_count': 12938471,
        'description': 'Singer',
        'country': 'UK'
    },
]
